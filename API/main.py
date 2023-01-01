import requests
from pprint import pprint
from datetime import datetime

#  Мои библиотеки
#  Библиотека для работы с документами
import work_documents as saby_doc
#  Библиотека с авторизацией
import authenticate as saby_auth
#  Библиотека по работе с карточкой организации
import our_organizations
import check_error


''' Модуль для работы с API SBIS ups
В нём частично реализованы методы по работе с документами
Методы аунтентификации по логину и паролю 
И метот Выход

Также частично наращивается технология SQL (PostgreSQL: 192.168.1.31)

И для удобной работы пользователю будет прикручена технология flask


Module for working with API SBIS
It partially implements methods for working with documents
Login and password authentication methods
And method Exit

SQL technology is also partially growing (PostgreSQL: 192.168.1.31)

And for convenient work, the flask technology will be screwed to the user
'''

#  Куда выполнятся запрос
url = 'https://fix-online.sbis.ru/service/?srv=1 HTTP/1.1'
# url для авторизации https://sbis.ru/help/integration/api/all_methods
linkAuth = 'https://fix-online.sbis.ru/auth/service/ HTTP/1.1'

#  Отображает текущего пользователя
saby_auth.you(url)

#  Метод для работы с методами СБИС
def work(url: str) -> dict:
    #  Заголовок запроса
    headers = {'Content-Type': 'application/json-rpc;charset=utf-8',
               'User-Agent': 'AWE', 'X-SBISSessionID': saby_auth.check_ssid()}
    #  Доступные методы
    methods = {
        'СБИС.ВосстановитьДокумент':'restore_document',
        'СБИС.ВыполнитьДействие':'execute_action',
        'СБИС.ЗаписатьВложение':'write_attachment',
        'СБИС.ЗаписатьДокумент':'write_document',
        'СБИС.ИнформацияОСлужебныхЭтапах':'read_service_stagesInfo',
        'СБИС.ОтложитьСлужебныйЭтап':'postpone_service_stage',
        'СБИС.ПовторитьЭтап':'repeat_stage',
        'СБИС.ПодготовитьДействие':'prepare_action',
        'СБИС.ПодписатьВложение':'sign_attachment',
        'СБИС.ПрочитатьДокумент':'read_document',
        'СБИС.СгенерироватьВложение':'generate_attachment',
        'СБИС.СписокДокументов':'list_documents',
        'СБИС.СписокДокументовПоСобытиям':'read_documents_by_events',
        'СБИС.СписокИзменений':'read_changes',
        'СБИС.СписокСлужебныхЭтапов':'read_service_stages',
        'СБИС.УдалитьДокумент':'delete_document',
        'СБИС.УдалитьВложение':'delete_attachment',
        'СБИС.УдалитьСлужебныйЭтап':'delete_utility_stage',
        'СБИС.УничтожитьДокумент':'eliminate_document',
        'СБИС.СписокНашихОрганизаций': 'list_our_organizations',
        'СБИС.Аутентифицировать':'authenticate',
        'СБИС.Выход': 'exit'
    }
    #  Превращяем значения и словаря в список
    methods_list = list(methods.values())

    print(f'______________________________________')

    #  Перебираем методы из словоря, что бы вывести пользователю
    for i, method in enumerate(methods):
        print(f'{i} --> {method}')

    print(f'______________________________________')


    #  Выбираем метод СБИС
    def choice_metod(method: int) -> dict:
        if method == 'restore_document':
            print(f'0) СБИС.ВосстановитьДокумент')
            print(f'метод ещё не готов')
            document = saby_doc.DocumentItem(input(f'Введите ид док-а: '))
            json = saby_doc.DocumentItem.restore_document(document)
            return json
        elif method == 'execute_action':
            print(f'1) СБИС.ВыполнитьДействие')
            print(f'метод ещё не готов')
            # json = saby_doc.execute_action(input("Введите ид док-а: "))
            return json
        elif method == 'write_attachment':
            print(f'2) СБИС.ЗаписатьВложение')
            document = saby_doc.DocumentItem(input(f'Введите ид док-а: '))
            json = saby_doc.DocumentItem.write_attachment(document)
            return json
        elif method == 'write_document':
            print(f'3) СБИС.ЗаписатьДокумент')
            document = saby_doc.DocumentItem(input(f'Введите ид док-а: '))
            json = saby_doc.DocumentItem.write_document(document)
            return json
        elif method == 'read_service_stages_info':
            print(f'4) СБИС.ИнформацияОСлужебныхЭтапах')
            print(f'метод ещё не готов')
            return json
        elif method == 'postpone_service_stage':
            print(f'5) СБИС.ОтложитьСлужебныйЭтап')
            print(f'метод ещё не готов')
            return json
        elif method == 'repeat_stage':
            print(f'6) СБИС.ПовторитьЭтап')
            document = saby_doc.DocumentItem(input(f'Введите ид док-а: '))
            json = saby_doc.DocumentItem.repeat_stage(document)
            return json
        elif method == 'prepare_action':
            print(f'7) СБИС.ПодготовитьДействие')
            print(f'метод ещё не готов')
            return json
        elif method == 'sign_attachment':
            print(f'8) СБИС.ПодписатьВложение')
            print(f'метод ещё не готов')
            return json
        elif method == 'read_document':
            print(f'9) СБИС.ПрочитатьДокумент')
            document = saby_doc.DocumentItem(input(f'Введите ид док-а: '))
            json = saby_doc.DocumentItem.read_document(document)
            return json
        elif method == 'generate_attachment':
            print(f'10) СБИС.СгенерироватьВложение')
            print(f'метод ещё не готов')
            return json
        elif method == 'list_documents':
            print(f'11) СБИС.СписокДокументов')
            json = saby_doc.DocumentItem.list_documents()
            return json
        elif method == 'read_documents_by_events':
            print(f'12) СБИС.СписокДокументовПоСобытиям')
            json = saby_doc.DocumentItem.read_documents_by_events(input(f'Введите ид док-а: '))
            return json
        elif method == 'read_changes':
            print(f'13) СБИС.СписокИзменений')
            json = saby_doc.DocumentItem.read_changes(input(f'Введите ид док-а: '))
            return json
        elif method == 'read_service_stages':
            print(f'14) СБИС.СписокСлужебныхЭтапов')
            print(f'Покупательфикс ИНН 6000000001 КПП 601001001')
            document = saby_doc.DocumentItem(inn=input(f'Введите ИНН: '),
                                             kpp=input(f'Введите КПП: '))
            json = saby_doc.DocumentItem.read_service_stages(document)
            return json
        elif method == 'delete_document':
            print(f'15) СБИС.УдалитьДокумент')
            document = saby_doc.DocumentItem(input(f'Введите ид док-а: '))
            json = saby_doc.DocumentItem.delete_document(document)
            return json
        elif method == 'delete_attachment':
            print(f'16) СБИС.УдалитьВложение')
            document = saby_doc.DocumentItem(input(f'Введите ид док-а: '))
            json = saby_doc.DocumentItem.delete_attachment(input(document))
            return json
        elif method == 'delete_utility_stage':
            print(f'17) СБИС.УдалитьСлужебныйЭтап')
            document = saby_doc.DocumentItem(input(f'Введите ид док-а: '))
            json = saby_doc.DocumentItem.delete_utility_stage(document)
            return json
        elif method == 'eliminate_document':
            print(f'18) СБИС.УничтожитьДокумент')
            document = saby_doc.DocumentItem(input(f'Введите ид док-а: '))
            json = saby_doc.DocumentItem.eliminate_document(document)
            return json
        elif method == 'list_our_organizations':
            print(f'19) СБИС.СписокНашихОрганизаций')
            json = our_organizations.list_our_organizations()
            return json
        elif method == 'authenticate':
            print(f'20) СБИС.Аутентифицировать')
            saby_auth.start_auth(linkAuth)
        elif method == 'exit':
            print(f'21) СБИС.Выход')
            saby_auth.exit(linkAuth)


    #  Вызываем выбранный метод
    def call(method: str) -> dict:
        #  json запрос выбранный в методе choice_metod
        json = choice_metod(method)

        if json != None:
            print(f'json-запрос {json}')
            #  Выполняем вызов json
            res = requests.post(url=url, headers=headers, json=json)
            print(res.json())
            if 'error' in res.json():
                check_error.check(res.json())
            else:
                print(f'______________________________________!')
                print(f'Адрес запроса: POST {url} \nШапка запроса: {headers}')
                print(f'Запрос: ')
                pprint(json)
                print(end='\n')
                input(f'Нажми ')
                print(f'______________________________________!!')
                print(f'Ответ: ')
                pprint(res.json())

                #  Имя файла лог
                log = f'logs/{datetime.today().strftime("%d-%m-%Y-%H_%H-%M-%S")} .txt'

                #  Записывает результат запроса/ответа в файл
                with open(log, 'w', encoding='utf-8') as file:
                    file.write(f'{datetime.now()} \n\nАдрес запроса: {url} \n\n'
                               f'Запрос: {json} \n\nОтвет: {res.json()}')
        else:
            work(url)

    #  Пользователь вводит значение и выбирает метод с проверкой
    try:
        call(method=methods_list[int((input(f'Введите цифру метода: ')))])
    except ValueError:
        print(f'Требуется ввести натуральное число')
        work(url)
    except IndexError:
        print(f'Метод с данным значением отсутсвует')
        work(url)


#  Цикл для повторения программы
status = True
while status == True:
    print(f'\n______________________________________')
    if input(f'Введите "q" чтобы выйти: ') == "q":
        print(f'\n Работа закончена')
        status = False
        break
    else:
        status == True
        work(url)