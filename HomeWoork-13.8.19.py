ticket_number = int(input('Какое количество билетов на конференцию вы хотите приобрести? : '))
price_ticket = 0
for i in range(ticket_number):
    i += 1
    while True:
        try:
            age = int(input('Возраст посетителя? :'))
            if age < 18:
                print('Билет бесплатный')
            elif 18 <= age <= 25:
                price_ticket += 990
                print('Стоимость билета: 990 руб.')
            else:
                price_ticket += 1390
                print('Стоимость билета: 1390 руб.')
            if type(age) == int:
                break
        except ValueError:
            print('Введите целое число')
if ticket_number > 3:
    price_ticket = price_ticket *0.9
    print('Сумма к оплате с 10%-ой скидкой за регистрацию больше 3-х человек:', price_ticket)
else:
    print('Сумма к оплате:', price_ticket)