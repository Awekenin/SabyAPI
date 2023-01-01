class Document:
    id = None
    number = None
    my_org = "you're not alone"
    partner = None

    def __init__(self, id = "ID", number = "Number", my_org = "you're not alone", partner = "KA"):
        self.id = id
        self.number = number
        self.my_org = my_org
        self.partner = partner

    def get_info(self):
        print("Номер документа:", self.number, " Контрагент:", self.partner)

class Doc_rouming(Document):
    operator = None

    def __init__(self, operator, number, partner):
        super(Doc_rouming, self).__init__(number, partner)
        self.operator = operator
        print("Оператор контрагента: ", self.operator, "номер", number, "контрагент", partner)





doc1 = Document(number = 100, partner = "СБП")
doc1.get_info()
doc_roum = Doc_rouming("1С-ЭДО", 101, "RTK",)

