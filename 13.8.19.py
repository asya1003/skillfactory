quantity = int(input())  # количество билетов, которые он хочет приобрести на мероприятие
total_amount = 0
for i in range(quantity):
    age = int(input())
    if age < 18:
        total_amount = total_amount + 0
    elif 18 <= age < 25:
        total_amount = total_amount + 990
    else:
        total_amount = total_amount + 1390
if quantity >= 3:
    print(total_amount * 0.9)
else:
    print(total_amount)

# Если посетителю конференции менее 18 лет, то он проходит на конференцию бесплатно.
# От 18 до 25 лет — 990 руб.
# От 25 лет — полная стоимость 1390 руб.
# При этом, если человек регистрирует больше трёх человек на конференцию, то дополнительно получает 10% скидку на полную стоимость заказа.