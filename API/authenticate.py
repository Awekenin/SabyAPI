import requests
from datetime import datetime

# # url для прочих команд https://sbis.ru/help/integration/api/all_methods
# linkComm = "https://fix-online.sbis.ru/service/?srv=1 HTTP/1.1"

# url для авторизации https://sbis.ru/help/integration/api/all_methods
linkAuth = 'https://fix-online.sbis.ru/auth/service/ HTTP/1.1'


def start_auth(url: str) -> str:


   def auth(url: str) -> str:
      print(f'Адрес запроса: POST {url}')
      headers = {'Content-Type': 'application/json-rpc;charset=utf-8', 'User-Agent': 'AWE'}
      print(f'Шапка запроса: {headers}')
      json = {
         "jsonrpc": "2.0",
         "method": "СБИС.Аутентифицировать",
         "params": {
            "Параметр": {
               "Логин": "покупательфикс",
               "Пароль": "покупательфикс123"
            }
         },
         "id": 0
      }

      #  Выводит в интерфейс пользователю информацию о запросе
      print(f'Запрос: {json}')
      res = requests.post(url=url, headers=headers, json=json)
      print(f'Ответ: {res.json()}')
      SBISSessionID = res.json()["result"]
      print(f'Полученный идентификатор сессии:  {SBISSessionID}')
      input(f'Нажми ')

      #  Читаем документ с идентификаторами
      file = open('X-SBISSessionID.log', 'a')
      file.write(f'{datetime.now()} X-SBISSessionID: {SBISSessionID}\n')
      file.close()

      return SBISSessionID

   #  Диалоговое окно с пользователем
   print('______________________________________')
   if input(f'Введите "y" - что бы пройти авторизацию: ') == 'y':
      SBISSessionID = auth(url)
   else:
      print(f'Завершение операции')


#  Вывод последнего сеанса сессии
#  Жизнь ключа 21 день с последней сессии
def check_ssid() -> str:
   try:
      with open('X-SBISSessionID.log', 'r') as file:
         SBISSessionID = file.read().split()[-1]
         # print(f'Текущий идентификатор сессии: {SBISSessionID}')
         return SBISSessionID
   except FileNotFoundError:
      print('Файл не найден')
   except IndexError:
      start_auth(linkAuth)


#  Вывод информации о текущем пользователе
def you(url: str) -> str:
   #  Заголовок запроса
   headers = {'Content-Type': 'application/json-rpc;charset=utf-8',
              'User-Agent': 'AWE', 'X-SBISSessionID': check_ssid()}
   json = {
         "jsonrpc": "2.0",
         "method": "СБИС.ИнформацияОТекущемПользователе",
         "params": {
            "Параметр": {}
         },
         "id": 0
      }
   res = requests.post(url=url, headers=headers, json=json)
   print(f'Информация о пользователе: {res.json()}')


#  Метод завершения сеанса
def exit(url: str) -> dict:
   print(f'Адрес запроса: POST {url}')
   headers = {'Content-Type': 'application/json-rpc;charset=utf-8',
              'User-Agent': 'AWE', 'X-SBISSessionID': check_ssid()}
   print(f'Заголовок: {headers}')
   json = {
      "jsonrpc": "2.0",
      "method": "СБИС.Выход",
      "params": {},
      "id": 0
   }
   print(f'Тело запроса Выход: {json}')

   res = requests.post(url=url, headers=headers, json=json)
   print(f'Выход: {res.json()}')
   return input(f'Нажми ')


