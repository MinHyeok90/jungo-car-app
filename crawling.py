from bs4 import BeautifulSoup
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.base import JobLookupError
import datetime
import time
import requests
import pandas
import json
import os
import pymongo

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_title = 'result.json'

search_url = 'http://api.encar.com/search/car/list/premium?count=true&q=(And.Hidden.N._.(C.CarType.Y._.Manufacturer.%ED%98%84%EB%8C%80.)_.OfficeCityState.%EA%B2%BD%EA%B8%B0._.Trust.ExtendWarranty._.Options.%EB%B8%8C%EB%A0%88%EC%9D%B4%ED%81%AC+%EC%9E%A0%EA%B9%80+%EB%B0%A9%EC%A7%80(ABS_)._.Options.%ED%9B%84%EB%B0%A9+%EC%B9%B4%EB%A9%94%EB%9D%BC._.Options.%EC%A3%BC%EC%B0%A8%EA%B0%90%EC%A7%80%EC%84%BC%EC%84%9C(%EC%A0%84%EB%B0%A9_)._.Category.SUV.)&sr=%7CModifiedDate%7C0%7C100'
item_url_pre = 'http://www.encar.com/dc/dc_cardetailview.do?pageid=dc_carsearch&listAdvType=normal&carid='
item_url_post = '&wtClick_korList=019&advClickPosition=kor_normal_p1_g1'

test_mode = True
test_limit_cnt = 3


def is_test_mode():
    return test_mode


def limiter_is_nedded_limit_for_test():
    if is_test_mode:
        return True
    else:
        return False


def save_data_title(data, title):
    with open(os.path.join(BASE_DIR, title), 'w+', encoding='UTF-8-sig') as json_file:
        json_file.write(json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4))


def save(data):
    save_data_title(data, file_title)


def crawling():
    req = requests.get(search_url)
    return req.json()


def crawling_and_save():
    json_data = crawling()
    save(json_data)
    return json_data


def from_file():
    with open(os.path.join(BASE_DIR, file_title), encoding='UTF-8-sig') as json_file:
        json_data = json.load(json_file)
    return json_data


def print_my_interests(title, results):
    print("Result!")
    print(title)
    print(results)


def my_interest_order():
    order = []
    order.append('Id')
    order.append('ModifiedDate')
    order.append('Manufacturer')
    order.append('Price')
    order.append('Year')
    order.append('Mileage')
    order.append('Model')
    order.append('Badge')
    return order


def my_interest_order_and_photodate_view():
    order = my_interest_order()
    order.append('Photos_updatedDate')
    return order


# {
#             "Badge": "디젤 2.0 4WD",
#             "BadgeDetail": "프레스티지",
#             "FormYear": "2019",
#             "FuelType": "디젤",
#             "Id": "25049206",
#             "Manufacturer": "현대",
#             "Mileage": 11923.0,
#             "Model": "싼타페 TM",
#             "ModifiedDate": "2019-10-03 19:31:00.000 +09",
#             "OfficeCityState": "경기",
#             "Photo": "/carpicture04/pic2504/25049206_",
#             "Photos": [
#                 {
#                     "location": "/carpicture04/pic2504/25049206_001.jpg",
#                     "ordering": 1.0,
#                     "type": "001",
#                     "updatedDate": "2019-07-08T03:31:11Z"
#                 }
#             ],
#             "Price": 3290.0,
#             "Separation": [
#                 "B"
#             ],
#             "Transmission": "오토",
#             "Trust": [
#                 "Warranty",
#                 "ExtendWarranty",
#                 "Inspection"
#             ],
#             "Year": 201806.0
#         },

def extract_my_interest(total_data):
    my_order = my_interest_order()
    records = []
    for item in total_data['SearchResults']:
        record = {}
        for key in my_order:
            record[key] = item[key]
        # record.append(item['Photos'][0]['updatedDate'])
        del item['Photos']
        records.append(record)
    return records


def add_photo_date(records):
    records_with_photodate = []
    # TODO: implement add photodate to records
    # for item in records:
    #
    return records_with_photodate


def get_additional_info_from_url_by_id(id):
    print("parsing: " + str(id) + "...");
    url = item_url_pre + str(id) + item_url_post
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find('ul', {'class': 'list_carinfo carinfo_etc'})
    more_specific_data = data.find_all('em')
    tmp = []
    i = 0
    for tag in more_specific_data:
        if i == 2 or i == 4:  # 조회수, 찜
            tmp.append(tag.text)
        i = i + 1
    return tmp


def get_additional_info_from_url_by_records(table):
    for item in table:
        cnt_and_zzim = get_additional_info_from_url_by_id(item['Id'])
        item['조회수'] = cnt_and_zzim[0]
        item['찜수'] = cnt_and_zzim[1]
    print(table)
    return table


def create_database():
    # myclient = pymongo.MongoClient("127.0.0.1", 27017)
    myclient = pymongo.MongoClient("mongodb://192.168.99.100:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    mydic = {"name": "John"}
    x = mycol.insert_one(mydic)
    print(x.inserted_id)


def get_added_ids(prev_ids, cur_ids):
    # TODO: 
    print("not impl")


def get_removed_ids(prev_ids, cur_ids):
    # TODO: 
    print("not impl")


def save_to_csv(json_data):
    df = pandas.read_json(json_data)
    df.to_csv("test.csv", encoding='utf-8')


def job():
    print("do job")


def repeat_job():
    sched = BackgroundScheduler()
    sched.start()
    sched.add_job(job, 'interval', seconds=3, id="test_interval_1")


def main():
    print("running jungo-car-app")
    # json_data = crawling_and_save()
    # json_data = from_file()
    # result_records = extract_my_interest(json_data)
    # result_table = get_additional_info_from_url_by_records(result_records)
    # print_my_interests(my_interest_order_and_photodate_view(), result_table)
    # save_data_title(result_table, "result_" + str(datetime.datetime.now()) + ".json")
    # save_to_csv(result_table)
    # create_database()
    repeat_job()

main()

# count = 0
# while True:
#     print("Running main process...............")
#     time.sleep(1)

