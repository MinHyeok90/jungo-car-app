def get_test_list_original():
    return [
        {'Id': '25167131', 'ModifiedDate': '2019-10-09 23:57:38.000 +09', 'Manufacturer': '현대', 'Price': 1950.0,
         'Year': 201402.0, 'Mileage': 79786.0, 'Model': '맥스크루즈', 'Badge': '디젤(e-VGT) 2.2 4WD 익스클루시브', '조회수': '200',
         '찜수': '2'},
        {'Id': '25479305', 'ModifiedDate': '2019-10-09 23:56:59.000 +09', 'Manufacturer': '현대', 'Price': 2270.0,
         'Year': 201708.0, 'Mileage': 8098.0, 'Model': '코나', 'Badge': '1.6 터보 4WD', '조회수': '720', '찜수': '6'},
        {'Id': '25109309', 'ModifiedDate': '2019-10-09 23:53:59.000 +09', 'Manufacturer': '현대', 'Price': 1750.0,
         'Year': 201302.0, 'Mileage': 33488.0, 'Model': '싼타페 DM', 'Badge': '디젤(e-VGT) 2.0 2WD 프리미엄', '조회수': '933',
         '찜수': '9'},
        {'Id': '25377212', 'ModifiedDate': '2019-10-01 20:18:39.000 +09', 'Manufacturer': '현대', 'Price': 2590.0,
         'Year': 201705.0, 'Mileage': 67541.0, 'Model': '더 뉴 맥스크루즈', 'Badge': '디젤 2.2 4WD', '조회수': '1042', '찜수': '3'},
    ]


def get_test_list_newer():
    return [
        {'Id': '99999999', 'ModifiedDate': '2019-10-09 23:57:38.000 +09', 'Manufacturer': '현대', 'Price': 1950.0,
         'Year': 201402.0, 'Mileage': 79786.0, 'Model': '맥스크루즈', 'Badge': '디젤(e-VGT) 2.2 4WD 익스클루시브', '조회수': '200',
         '찜수': '2'},
        {'Id': '25479305', 'ModifiedDate': '2019-10-09 23:56:59.000 +09', 'Manufacturer': '현대', 'Price': 2270.0,
         'Year': 201708.0, 'Mileage': 8098.0, 'Model': '코나', 'Badge': '1.6 터보 4WD', '조회수': '720', '찜수': '6'},
        {'Id': '25109309', 'ModifiedDate': '2019-10-09 23:53:59.000 +09', 'Manufacturer': '현대', 'Price': 1750.0,
         'Year': 201302.0, 'Mileage': 33488.0, 'Model': '싼타페 DM', 'Badge': '디젤(e-VGT) 2.0 2WD 프리미엄', '조회수': '933',
         '찜수': '9'},
        # {'Id': '25377212', 'ModifiedDate': '2019-10-01 20:18:39.000 +09', 'Manufacturer': '현대', 'Price': 2590.0,
        #  'Year': 201705.0, 'Mileage': 67541.0, 'Model': '더 뉴 맥스크루즈', 'Badge': '디젤 2.2 4WD', '조회수': '1042', '찜수': '3'},
    ]


def get_separated_by_status():
    return {
        'newer':
            [{'Id': '99999999', 'ModifiedDate': '2019-10-09 23:57:38.000 +09', 'Manufacturer': '현대', 'Price': 1950.0,
              'Year': 201402.0, 'Mileage': 79786.0, 'Model': '맥스크루즈', 'Badge': '디젤(e-VGT) 2.2 4WD 익스클루시브', '조회수': '200',
              '찜수': '2'}],
        'leave':
            [{'Id': '25109309', 'ModifiedDate': '2019-10-09 23:53:59.000 +09', 'Manufacturer': '현대', 'Price': 1750.0,
              'Year': 201302.0, 'Mileage': 33488.0, 'Model': '싼타페 DM', 'Badge': '디젤(e-VGT) 2.0 2WD 프리미엄', '조회수': '933',
              '찜수': '9'},
             {'Id': '25479305', 'ModifiedDate': '2019-10-09 23:56:59.000 +09', 'Manufacturer': '현대', 'Price': 2270.0,
              'Year': 201708.0, 'Mileage': 8098.0, 'Model': '코나', 'Badge': '1.6 터보 4WD', '조회수': '720', '찜수': '6'}],
        'deleted':
            [{'Id': '25377212', 'ModifiedDate': '2019-10-01 20:18:39.000 +09', 'Manufacturer': '현대', 'Price': 2590.0,
              'Year': 201705.0, 'Mileage': 67541.0, 'Model': '더 뉴 맥스크루즈', 'Badge': '디젤 2.2 4WD', '조회수': '1042',
              '찜수': '3'},
             {'Id': '25167131', 'ModifiedDate': '2019-10-09 23:57:38.000 +09', 'Manufacturer': '현대', 'Price': 1950.0,
              'Year': 201402.0, 'Mileage': 79786.0, 'Model': '맥스크루즈', 'Badge': '디젤(e-VGT) 2.2 4WD 익스클루시브', '조회수': '200',
              '찜수': '2'}]
    }


def get_separated_by_status_three_newer():
    return {
        'newer':
            [{'Id': '99999999', 'ModifiedDate': '2019-10-09 23:57:38.000 +09', 'Manufacturer': '현대', 'Price': 1950.0,
              'Year': 201402.0, 'Mileage': 79786.0, 'Model': '맥스크루즈', 'Badge': '디젤(e-VGT) 2.2 4WD 익스클루시브', '조회수': '200',
              '찜수': '2'},
             {'Id': '25109309', 'ModifiedDate': '2019-10-09 23:57:38.000 +09', 'Manufacturer': '현대', 'Price': 1950.0,
              'Year': 201402.0, 'Mileage': 79786.0, 'Model': '맥스크루즈', 'Badge': '디젤(e-VGT) 2.2 4WD 익스클루시브', '조회수': '200',
              '찜수': '2'},
             {'Id': '25167131', 'ModifiedDate': '2019-10-09 23:57:38.000 +09', 'Manufacturer': '현대', 'Price': 1950.0,
              'Year': 201402.0, 'Mileage': 79786.0, 'Model': '맥스크루즈', 'Badge': '디젤(e-VGT) 2.2 4WD 익스클루시브', '조회수': '200',
              '찜수': '2'}
             ],
        'leave': []
        ,
        'deleted':
            [{'Id': '25377212', 'ModifiedDate': '2019-10-01 20:18:39.000 +09', 'Manufacturer': '현대', 'Price': 2590.0,
              'Year': 201705.0, 'Mileage': 67541.0, 'Model': '더 뉴 맥스크루즈', 'Badge': '디젤 2.2 4WD', '조회수': '1042',
              '찜수': '3'},
             {'Id': '25167131', 'ModifiedDate': '2019-10-09 23:57:38.000 +09', 'Manufacturer': '현대', 'Price': 1950.0,
              'Year': 201402.0, 'Mileage': 79786.0, 'Model': '맥스크루즈', 'Badge': '디젤(e-VGT) 2.2 4WD 익스클루시브', '조회수': '200',
              '찜수': '2'}]
    }


def get_separated_by_status_only_leave():
    return {
        'newer': [],
        'leave':
            [{'Id': '99999999', 'ModifiedDate': '2019-10-09 23:57:38.000 +09', 'Manufacturer': '현대', 'Price': 1950.0,
              'Year': 201402.0, 'Mileage': 79786.0, 'Model': '맥스크루즈', 'Badge': '디젤(e-VGT) 2.2 4WD 익스클루시브', '조회수': '200',
              '찜수': '2'},
             {'Id': '25109309', 'ModifiedDate': '2019-10-09 23:57:38.000 +09', 'Manufacturer': '현대', 'Price': 1950.0,
              'Year': 201402.0, 'Mileage': 79786.0, 'Model': '맥스크루즈', 'Badge': '디젤(e-VGT) 2.2 4WD 익스클루시브', '조회수': '200',
              '찜수': '2'},
             {'Id': '25167131', 'ModifiedDate': '2019-10-09 23:57:38.000 +09', 'Manufacturer': '현대', 'Price': 1950.0,
              'Year': 201402.0, 'Mileage': 79786.0, 'Model': '맥스크루즈', 'Badge': '디젤(e-VGT) 2.2 4WD 익스클루시브', '조회수': '200',
              '찜수': '2'},
             {'Id': '25377212', 'ModifiedDate': '2019-10-01 20:18:39.000 +09', 'Manufacturer': '현대', 'Price': 2590.0,
              'Year': 201705.0, 'Mileage': 67541.0, 'Model': '더 뉴 맥스크루즈', 'Badge': '디젤 2.2 4WD', '조회수': '1042',
              '찜수': '3'},
             {'Id': '25167131', 'ModifiedDate': '2019-10-09 23:57:38.000 +09', 'Manufacturer': '현대', 'Price': 1950.0,
              'Year': 201402.0, 'Mileage': 79786.0, 'Model': '맥스크루즈', 'Badge': '디젤(e-VGT) 2.2 4WD 익스클루시브', '조회수': '200',
              '찜수': '2'}]
        ,
        'deleted': []
    }
    
    
def get_url():
    url = "http://api.encar.com/search/car/list/premium?count=true&q=(And.Hidden.N._.CarType.Y._.(Or.OfficeCityState.%EC%84%9C%EC%9A%B8._.OfficeCityState.%EA%B2%BD%EA%B8%B0.)_.Transmission.%EC%98%A4%ED%86%A0._.Category.SUV._.Trust.Inspection.)&sr=%7CModifiedDate%7C0%7C3"
    return url

def get_decoded_url():
    url = "http://api.encar.com/search/car/list/premium?count=true&q=(And.Hidden.N._.(C.CarType.Y._.Manufacturer.현대.)_.OfficeCityState.경기._.Trust.ExtendWarranty._.Options.브레이크+잠김+방지(ABS_)._.Options.후방+카메라._.Options.주차감지센서(전방_)._.Category.SUV.)&sr=|ModifiedDate|0|3"
    return url