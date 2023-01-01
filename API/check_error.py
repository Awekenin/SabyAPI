def check(res):
    if res.get('error') == 'Not authorized.':
        print(f'{res.get("error")}')
    elif type(res.get('error')) == dict:
        for key, item in res.get('error').items():
            if key == 'message' or key == 'details':
                print(f'{key} --> {item}')
            elif key == 'data':
                # i = item["classid"].replace("{", '').replace("}", '')
                print(f'https://sbis.ru/help/search?q='
                      f'{item["classid"].replace("{", "").replace("}", "")}')
            # else:
            #     print(f'Непредвиденная ошибка')
    else:
        print(res.get('error'), type(res.get('error')))
        print(f'Неизведонная ошибка')

# di = {'jsonrpc': '2.0', 'error': {'code': -32000, 'message': "Не найден документ с идентификатором '984'",
#                                    'details': "Не найден документ с идентификатором '984'", 'type': 'warning',
#                                    'data': {'classid': '{00000000-0000-0000-0000-1fa000010000}',
#                                             'error_code': -1, 'addinfo': None}}, 'id': 0}
#
# print(*di.get('error'))