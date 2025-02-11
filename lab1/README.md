# 00_distance.py
## Составить словарь словарей расстояний между ними
### INPUT

```python
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
```

### OUTPUT 
```python
distances = {}
```

### Выполнение задачи
Нам нужно пройтись по словарю sites, получая названия городов и их координаты, затем мы берем x1 y1 и x2 y2 координаты двух городов и высчитываем по формуле ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 их расстояние. 
Так как нам нужно обрабатывать два города, мы создаем два цикла for, которые проходятся по словарю.

### Решение
```python
for name_1, coords_1 in sites.items():
    distances[name_1] = {}
    for name_2, coords_2 in sites.items():
        if name_1 != name_2:
            x1 = coords_1[0]
            y1 = coords_1[1]
            x2 = coords_2[0]
            y2 = coords_2[1]
            distances[name_1][name_2] = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
```

### Вывод программы
![alt text](screenshots/image.png)