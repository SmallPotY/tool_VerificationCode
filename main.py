# -*- coding: utf-8 -*-
import requests
import checkCode

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0',
}


def login():
    response = requests.get('https://vis.vip.com/login.php', headers=headers)
    # result = response.text

    code_url = 'https://vis.vip.com/checkCode.php'

    checkWord = checkCode.code(code_url)

    data = {
        'checkWord': checkWord,
        'passWord': '*',
        'userName': '*'
    }

    response = requests.post('https://vis.vip.com/login.php',
                             data=data, headers=headers)

    if '验证码输入错误' in response.text:
        print('验证码识别错误')
        return '验证码识别错误'
    else:
        print('验证通过')
        return response.cookies


def check(po, cookies):
    po_url = 'http://vis.vip.com/jit/delivery.php?mod=ajax&page=1&jdh_de_co=' + po + '&po=&st_actual_delivery_time=&et_actual_delivery_time=&st_estimate_arrive_time=&et_estimate_arrive_time=&st_arrive_time=&et_arrive_time=&jdh_wa=&jdh_ar_fl='

    po_data = {
        'et_actual_delivery_time': '',
        'et_arrive_time	': '',
        'et_estimate_arrive_time': '',
        'jdh_ar_fl': '',
        'jdh_de_co': po,
        'jdh_wa': '',
        'mod': 'ajax',
        'page': '1',
        'po': '',
        'st_actual_delivery_time	': '',
        'st_arrive_time	': '',
        'st_estimate_arrive_time': ''
    }

    response = requests.post(po_url, data=po_data, headers=headers, cookies=cookies)



    if '已出仓' in response.text:
        print(po + "状态：已出仓")
        return '1'
    else:
        print(po + "状态：等待出仓")
        return '0'


if __name__ == '__main__':

    for i in range(9):
        po_cookies = login()
        if po_cookies == '验证码识别错误':
            print('验证失败,准备重试,当前次数：' + str(i + 1))
        else:
            break

    if po_cookies != '验证码识别错误':

        po_list = input("输入查询出库单号','进行分隔：\n").split(',')

        if po_list:
            if i !='':
                for i in po_list:
                    po_state = check(i, po_cookies)

    else:
        print('验证码识别错误次数较多，暂停运行')

    while True:
        quit = input('\n\n按"q"键退出')
        if quit == 'q':
            break

