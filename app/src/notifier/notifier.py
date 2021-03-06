#!/usr/bin/env python
# encoding=utf-8
import telegram
import os
from model.division_state_cars import DivisionStateCars
import datetime
from dateutil.parser import parse

from string import Template


class DeltaTemplate(Template):
    delimiter = "%"


def strfdelta(tdelta, fmt):
    d = {"D": tdelta.days}
    d["H"], rem = divmod(tdelta.seconds, 3600)
    d["M"], d["S"] = divmod(rem, 60)
    t = DeltaTemplate(fmt)
    return t.substitute(**d)


def get_time_delta_from_now(modi_date):
    from_date = parse(modi_date).replace(tzinfo=None)
    now = datetime.datetime.now().replace(tzinfo=None)
    return strfdelta(now - from_date, "%D일  %H시간 %M분")


def get_dic():
    return os.path.dirname(os.path.abspath(__file__))


def get_bot():
    f = open(get_dic() + '/my_key', 'r')
    key = f.readline()
    bot = telegram.Bot(token=key)
    return bot


def get_chat_room():
    f = open(get_dic() + '/my_chat_room', 'r')
    chat_room_number = f.readline()
    return chat_room_number


def send(message):
    bot = get_bot()
    chat_room = get_chat_room()
    try:
        bot.sendMessage(chat_room, "[알림봇]\n" + message)
        pass
    except:
        print("전송실패 : " + message)
        pass


def send_contents_list(contents_list, type):
    for i in range(len(contents_list)):
        send(type + str(i + 1) + "번째\n" + contents_list[i])


def create_link(num):
    url_pre = 'www.encar.com/dc/dc_cardetailview.do?pageid=dc_carsearch&listAdvType=normal&carid='
    url_post = '&wtClick_korList=019&advClickPosition=kor_normal_p1_g1'
    return url_pre + num + url_post


def create_car_msg_basic(car):
    contents = car['Model'] + " / " + \
        str(format(round(car['Price']), ',')) + "만원 / " + \
        car['Badge'] + " / " + \
        str(round(car['Year'])) + " / " + \
        str(format(round(car['Mileage']), ',')) + " km /"
    return contents


def cut_limit(car_list):
    return car_list[0:10]


def notify_newer_cars(dsc: DivisionStateCars):
    newer = dsc.get_newer()
    newer = cut_limit(newer)
    contents_list = []
    for car in newer:
        contents = create_car_msg_basic(car) + \
            "\n" + create_link(car['Id'])
        contents_list.append(contents)
    send_contents_list(contents_list, "신규")


def notify_updated_cars(dsc: DivisionStateCars):
    updated = dsc.get_updated()
    updated = cut_limit(updated)
    contents_list = []
    for car in updated:
        contents = create_car_msg_basic(car) + \
            "\n" + create_link(car['Id'])
        contents_list.append(contents)
    send_contents_list(contents_list, "갱신")


def notify_deleted_cars(dsc: DivisionStateCars):
    deleted = dsc.get_deleted()
    deleted = cut_limit(deleted)
    contents_list = []
    for car in deleted:
        contents = create_car_msg_basic(car)
        contents += "\n" + car['Id'] + " / "
        contents += "\n등록 후 " + \
            get_time_delta_from_now(car['ModifiedDate']) + ""
        contents_list.append(contents)
    send_contents_list(contents_list, "삭제")


def notify_header(dsc: DivisionStateCars):
    title = "■■■■■■ 유효 매물" + str(dsc.get_len_exist_total()) + "개 ■■■■■■\n" + \
            "■ 신규: " + format(dsc.get_len_newer(), ',') + "\n" + \
            "■ 유지: " + format(dsc.get_len_leave(), ',') + "\n" + \
            "■ 갱신: " + format(dsc.get_len_updated(), ',') + "\n" + \
            "■ 삭제: " + format(dsc.get_len_deleted(), ',')
    send(title)


def notify_validator(dsc: DivisionStateCars):
    if dsc.get_len_newer() == 0 and dsc.get_len_deleted() == 0 and dsc.get_len_updated:
        return False
    return True


def notify(dsc: DivisionStateCars):
    if notify_validator(dsc):
        notify_header(dsc)
        notify_deleted_cars(dsc)
        notify_updated_cars(dsc)
        notify_newer_cars(dsc)
        print("송신완료")


def force_header_notify(dsc: DivisionStateCars):
    notify_header(dsc)


def force_header_notify_as_leave_by_list(leave):
    dsc = DivisionStateCars()
    dsc.set_leave(leave)
    notify_header(dsc)


def hello_notify():
    hello_message = "안녕하세요!\n저는 새롭게 업데이트 된 중고차 알림봇 입니다!\n새로운 매물을 누구보다 빠르게 알려드리겠습니다!\n감사합니다!"
    send(hello_message)


def test():
    from app import test
    # print("get bot")
    # get_bot()

    # print("converter_readability test")
    data = test.get_separated_by_status_three_newer()
    # print(x)

    print("send long message test")
    notify(data)


def test_path():
    import os
    stri = os.path.dirname(os.path.abspath(__file__))
    print(stri)


# if __name__ == "__main__":
    # test()
# test_path()
# pass
