class Doc:
    name = None
    age = None

    def __init__(self, name, age):
        self.set_data(name, age)
        self.get_data()

    def set_data(self, name = None, age = " "):
        self.name = name
        self.age = age

    def get_data(self):
        print(self.name, "Номер документа:", self.age, "Контрагент")

doc1 = Doc("ID123", 123)
doc1.set_data("ID255")
doc1.get_data()

doc2 = Doc("ID321", 321)

x = 10
print(str(x), type(x), id(x))
# doc4 = Doc("ID321")

x = {"name": "pupa", "age": "12"}
print("Ключи: ", x.keys())
print("Значение: ", x.items())
for key, volume in x.items():
    print(volume)
print(x.get("name"))
print(x['name'])
x['name'] = "buba"
print(x)



# doc3 = Doc
# doc3.set_data("ID345")
# doc3.get_data()
