#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

for name_1, coords_1 in sites.items():
    distances[name_1] = {}
    for name_2, coords_2 in sites.items():
        if name_1 != name_2:
            x1 = coords_1[0]
            y1 = coords_1[1]
            x2 = coords_2[0]
            y2 = coords_2[1]
            distances[name_1][name_2] = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

print(distances)




