#  Метод СписокНашихОрганизаций
def list_our_organizations():
    json = {
       "jsonrpc": "2.0",
       "method": "СБИС.СписокНашихОрганизаций",
       "params": {
          "Фильтр": {}
       },
       "id": 0
    }

    return json
