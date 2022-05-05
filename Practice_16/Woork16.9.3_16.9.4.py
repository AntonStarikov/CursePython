class Klient:
    def __init__(self, name, last_name, city, balance):
        self.name = name
        self.last_name = last_name
        self.city = city
        self.balance = balance
    def __str__(self):
        return f'Klient: {self.name} {self.last_name}. {self.city}. Баланс:{self.balance} руб.'
    def get_gost(self):
        return f'Klient: {self.name} {self.last_name}. {self.city}.'

klient_1 = Klient('Иван', 'Петров', 'Москва', 50)
klient_2 = Klient('Мария', 'Морис', 'Лондон', 10500)
klient_3 = Klient('Эрнест', 'Хеменгуэй', 'Венесуэлла', 30000)

print(klient_1)

gost_list = [klient_1, klient_2, klient_3]
for gost in gost_list:
    print(gost.get_gost())