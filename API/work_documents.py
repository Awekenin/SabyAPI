class DocumentItem:
    id_doc = None
    inn = None
    kpp = None

    def __init__(self, id_doc=None, inn=None, kpp=None):
        self.id_doc = id_doc
        self.inn = inn
        self.kpp = kpp


    #  "0) СБИС.ВосстановитьДокумент"
    def restore_document(self):
        json = {
                "jsonrpc": "2.0",
                "method": "СБИС.ВосстановитьДокумент",
                "params": {
                    "Документ": {
                        "Идентификатор": self.id_doc
                    }
                },
                "id": 0
            }
        return json
    #  "1) СБИС.ВыполнитьДействие"
    #  "2) СБИС.ЗаписатьВложение"
    def write_attachment(self):
        json = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "СБИС.ЗаписатьВложение",
            "params": {
                "Документ": {
                    "Идентификатор": "e57411e2-98c3-4229-94c6-1db0dcb5bdc8",
                    "Вложение": [
                        {
                            "Файл": {
                                "ДвоичныеДанные": "MQ==",
                                "Имя": "test.txt"
                            }
                        }
                    ]
                }
            }
        }
        return json
    #  "3) СБИС.ЗаписатьДокумент"
    def write_document(self):
        json = {
            "jsonrpc": "2.0",
            "method": "СБИС.ЗаписатьДокумент",
            "params": {
                "Документ": {
                    "Вложение": [
                        {
                            "Идентификатор": "d8e74588-f9e9-4a50-a4f8-82753abc6eb8",
                            "Файл": {
                                "ДвоичныеДанные": "MQ==",
                                "Имя": "test.txt"
                            }
                        }
                    ],
                    "Дата": "17.12.2022",
                    "Номер": "12345621",
                    "Идентификатор": self.id_doc,
                    "Контрагент": {
                        "СвЮЛ": {
                            "ИНН": "7718280156",
                            "КПП": "773101001",
                            "Название": "Общество с ограниченной ответственностью \"АПТЕКА 36,6+\""
                        }
                    },
                    "НашаОрганизация": {
                        "СвЮЛ": {
                            "ИНН": "6000000001",
                            "КПП": "601001001"
                        }
                    },
                    "Примечание": "Здесь обычно указывают примечание",
                    "ДополнительныеПоля": {
                        "123": "Тест"
                    },
                    "Редакция": [
                        {
                            "ПримечаниеИС": "РеализацияТоваровУслуг:8bf669c4-042e-4854-b21b-673e8067e83d"
                        }
                    ],
                    "Тип": "ДокОтгрИсх"
                }
            },
            "id": 0
        }

        return json

    #  "4) СБИС.ИнформацияОСлужебныхЭтапах"
    #  "5) СБИС.ОтложитьСлужебныйЭтап"
    #  "6) СБИС.ПовторитьЭтап"
    def repeat_stage(self):
        json = {
           "jsonrpc": "2.0",
           "method": "СБИС.ПовторитьЭтап",
           "params": {
              "Документ": {
                 "Идентификатор": self.id_doc,
                 "Этап": {
                    "Название": "Утверждение",
                    "Идентификатор": ""
                 }
              }
           },
           "id": 0
        }

        return json
    #  "7) СБИС.ПодготовитьДействие"
    #  "8) СБИС.ПодписатьВложение"
    #  "9) СБИС.ПрочитатьДокумент"
    def read_document(self):
        json = {
           "jsonrpc": "2.0",
           "method": "СБИС.ПрочитатьДокумент",
           "params": {
              "Документ": {
                 "Идентификатор": self.id_doc,
                 "ДопПоля": "ДополнительныеПоля",
                 "Редакция":{
                     "Идентификатор": ""
                 }
              }
           },
           "id": 0
        }

        return json
    #  "10) СБИС.СгенерироватьВложение"
    #  "11) СБИС.СписокДокументов"
    def list_documents():
        json = {
           "jsonrpc": "2.0",
           "method": "СБИС.СписокДокументов",
           "params": {
              "Фильтр": {
                 "ДатаС": "18.08.2022",
                 "Тип": "ДокОтгрИсх",
                 "НашаОрганизация": {
                    "СвЮЛ": {
                       "ИНН": "3812065889",
                       "КПП": "381201001",
                       "Название": '!ЗАО "Иркутск-Кран-Сервис" (в акк. покупательфикс)'
                    }
                 }
              }
           },
           "id": 0
        }

        return json

    #  "12) СБИС.СписокДокументовПоСобытиям"
    def read_documents_by_events(self):
        json = {
           "jsonrpc": "2.0",
           "method": "СБИС.СписокДокументовПоСобытиям",
           "params": {
              "Фильтр": {
                 "ДатаС": "06.12.2022",
                 "ДатаПо":"06.12.2022",
                 "ТипРеестра": "Отправленные"
              }
           },
           "id": 0
        }
        return json

    #  "13) СБИС.СписокИзменений"
    def read_changes(self):
        json = {
            "jsonrpc": "2.0",
            "method": "СБИС.СписокИзменений",
            "params": {
                "Фильтр": {
                    "ИдентификаторСобытия": "",
                    "ДатаВремяС": "20.12.2022 10:00:00",
                    "ДатаВремяПо": "20.12.2022 13:00:00",
                    "НашаОрганизация": {
                        "СвЮЛ": {
                            "ИНН": "6000000001",
                            "КПП": "601001001"
                        }
                    },
                }
            },
            "id": 0
        }

        return json

    #  "14) СБИС.СписокСлужебныхЭтапов"
    def rad_service_stages(self):
        json = {
            "jsonrpc": "2.0",
            "method": "СБИС.СписокСлужебныхЭтапов",
            "params": {
                "Фильтр": {
                    "НашаОрганизация": {
                        "СвЮЛ": {
                            "ИНН": self.inn,
                            "КПП": self.KPP
                        }
                    }
                }
            },
            "id": 0
        }
        return json

    #  "15) СБИС.УдалитьДокумент"
    def delete_document(self):
        json = {
           "jsonrpc": "2.0",
           "method": "СБИС.УдалитьДокумент",
           "params": {
              "Документ": {
                 "Идентификатор": self.id_doc
              }
           },
           "id": 0
        }

        return json

    #  "16) СБИС.УдалитьВложение"
    def delete_attachment(self):
        json = {
              "jsonrpc": "2.0",
              "method": "СБИС.УдалитьВложение",
              "params": {
                "Документ": {
                  "Идентификатор": self.id_doc,
                  "Вложение": [
                    {
                      "Идентификатор": self.id_att
                    }
                  ]
                }
              },
              "id": 1,
              "protocol": 3
        }

        return json

    #  "17) СБИС.УдалитьСлужебныйЭтап"
    def delete_utility_stage(self):
        json = {
           "id": 1,
           "jsonrpc": "2.0",
           "method": "СБИС.УдалитьСлужебныйЭтап",
           "params": {
              "Параметры": {
                 "Документ": {
                    "Идентификатор": self.id_doc,
                    "Этап": {
                       "Идентификатор": "",
                       "Действие": {
                            "Идентификатор": "",
                            "Название": "Обработать служебное"
                       }
                    }
                 }
              }
           }
        }

        return json

    #  "18) СБИС.УничтожитьДокумент"
    def eliminate_document(self):
        json = {
            "jsonrpc": "2.0",
            "method": "СБИС.УничтожитьДокумент",
            "params": {
                 "Документ": {
                    "Идентификатор": self.id_doc
                }
            },
            "id": 0
        }

        return json