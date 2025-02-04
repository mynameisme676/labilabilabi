#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.
##
decks_q_a = store[goods['Стол']][0]['quantity']
decks_q_b = store[goods['Стол']][1]['quantity']
decks_cost_a = decks_q_a * store[goods['Стол']][0]['price']
decks_cost_b = decks_q_b * store[goods['Стол']][1]['price']

print("Стол -", decks_q_a + decks_q_b, 'шт, стоимость', decks_cost_a + decks_cost_b, 'руб')
##
divan_q_a = store[goods['Диван']][0]['quantity']
divan_q_b = store[goods['Диван']][1]['quantity']
divan_cost_a = divan_q_a * store[goods['Диван']][0]['price']
divan_cost_b = divan_q_b * store[goods['Диван']][1]['price']

print("Диван -", divan_q_a + divan_q_b, 'шт, стоимость', divan_cost_a + divan_cost_b, 'руб')
##
stul_q_a = store[goods['Стул']][0]['quantity']
stul_q_b = store[goods['Стул']][1]['quantity']
stul_q_c = store[goods['Стул']][2]['quantity']
stul_cost_a = stul_q_a * store[goods['Стул']][0]['price']
stul_cost_b = stul_q_b * store[goods['Стул']][1]['price']
stul_cost_c = stul_q_c * store[goods['Стул']][2]['price']

print("Стул -", stul_q_a + stul_q_b + stul_q_c, 'шт, стоимость', stul_cost_a + stul_cost_b + stul_cost_c, 'руб')