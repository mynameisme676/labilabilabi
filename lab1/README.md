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

# 01_circle.py
## Задание 1. Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой.
### INPUT
```python
radius = 42
```
### OUTPUT
```python
print(round(3.1415926 * (radius ** 2), 4))
```

### Выполнение задачи
Формула для подсчета площади круга = Pi * R^2
После подсчета, округялем значение.

### Решение
```python
print(round(3.1415926 * (radius ** 2), 4))
```

### Вывод программы
![alt text](screenshots/image1.png)
## Задание 2. Если точка point лежит внутри того самого круга [центр в начале координат (0, 0), radius = 42], то выведите на консоль True, Или False, если точка лежит вовне круга.
### INPUT
```python
point_1 = (23, 34)
point_2 = (30, 30)
```
### OUTPUT
```python
point_in_1 = (point_1[0]**2 + point_1[1]**2)**0.5
point_in_2 = (point_2[0]**2 + point_2[1]**2)**0.5
```

### Выполнение задачи
Мы определяем расстояние от точки до начала координат, затем сверяем попадает ли она в наш радиус или нет.
### Решение
```python
print(point_in_1 <= radius)
print(point_in_2 <= radius)
```
### Вывод программы
![alt text](screenshots/image2.png)

# 02_operations.py
## Расставьте знаки операций "плюс", "минус", "умножение" и скобки между числами "1 2 3 4 5" так, что бы получилось число "25".
### Решение
```python
result = 1 * (2 + 3) * 4 + 5
print(result)
```
### Вывод программы
![alt text](screenshots/image3.png)

# 03_favorite_movies.py
## Выведите на консоль с помощью индексации строки, последовательно: первый фильм, последний, второй, второй с конца.
### INPUT
```python
my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
```

### OUTPUT
```python
first_film = my_favorite_movies[0:10]
last_film = my_favorite_movies[42:60]
second_film = my_favorite_movies[12:25]
second_from_end_film = my_favorite_movies[35:40]
```

### Выполнение задачи
В данной задаче мы можем использовать только срезы. Цифра **x** в [x:y] означает начало среза, **y** означает конец среза. Срез идет посимвольно.

### Решение
```python
first_film = my_favorite_movies[0:10]
last_film = my_favorite_movies[42:60]
second_film = my_favorite_movies[12:25]
second_from_end_film = my_favorite_movies[35:40]

print(f'первый: {first_film}\nпоследний: {last_film}\nвторой: {second_film}\nвторой с конца: {second_from_end_film}')
```

### Вывод программы
![alt text](screenshots/image4.png)

# 04_my_family.py
## Выведите на консоль рост отца в формате "Рост отца - ХХ см".
### INPUT
```python
my_family = ['Мама', 'Папа', 'Сестра']
my_family_height = [
    ['Мама', 160],
    ['Папа', 171],
    ['Сестра', 140],
]
```

### OUTPUT
```python
print(f"Рост отца - {my_family_height[1][1]} см")
```

### Выполнение задачи
Нам нужно составить два списка, в первом списке - наша семья, в другом их соответствие с ростом. Затем нам нужно вычленить отца и найти его рост.

### Решение
```python
print(f"Рост отца - {my_family_height[1][1]} см")
```

### Вывод программы
![alt text](screenshots/image5.png)
## Выведите на консоль общий рост вашей семьи как сумму ростов всех членов.
### INPUT
```python
my_family = ['Мама', 'Папа', 'Сестра']
my_family_height = [
    ['Мама', 160],
    ['Папа', 171],
    ['Сестра', 140],
]
```
### OUTPUT
```python
print(f"Общий рост моей семьи - {amount} см")
```

### Выполнение задачи
Нам нужно пройтись по списку my_family_height и сложить все росты в переменную amount.

### Решение
```python
amount = 0
for people in my_family_height:
    amount += people[1]
```
### Вывод программы
![alt text](screenshots/image6.png)

# 05_zoo.py
## Задание 1. Посадите медведя (bear) между львом и кенгуру.
### INPUT
```python
zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
```
### OUTPUT
```python
zoo = ['lion', 'bear' ,'kangaroo', 'elephant', 'monkey', ]
```

### Выполнение задачи
Используем встроенный метод работы со списками **insert**. Первый аргумент задает позицию.

### Решение
```python
zoo.insert(1, 'bear')
```

### Вывод программы
![alt text](screenshots/image7.png)
## Задание 2. Добавьте птиц из списка birds в последние клетки зоопарка.
### INPUT
```python
zoo = ['lion', 'bear' ,'kangaroo', 'elephant', 'monkey', ]
birds = ['rooster', 'ostrich', 'lark', ]
```
### OUTPUT
```python
zoo = ['lion', 'bear', 'kangaroo', 'elephant', 'monkey', 'rooster', 'ostrich', 'lark']
```

### Выполнение задачи
Используем встроенный метод работы со списками **extend**.

### Решение
```python
zoo.extend(birds)
```

### Вывод программы
![alt text](screenshots/image8.png)

## Задание 3. Убрать слона.
### INPUT
```python
zoo = ['lion', 'bear', 'kangaroo', 'elephant', 'monkey', 'rooster', 'ostrich', 'lark']
```

### OUTPUT
```python
zoo = ['lion', 'bear', 'kangaroo', 'monkey', 'rooster', 'ostrich', 'lark']
```

### Выполнение задачи
Используем встроенный метод работы со списками **remove**.
### Решение
```python
zoo.remove('elephant')
```
### Вывод программы
![alt text](screenshots/image9.png)
## Задание 4. Вывести номера клеток льва и жаворонка.
### INPUT
```python
zoo = ['lion', 'bear', 'kangaroo', 'monkey', 'rooster', 'ostrich', 'lark']
```
### Выполнение задачи
Используем встроенный метод работы со списками **index**. Добавляем единицу, так как номера при выводе должны быть понятны простому человеку, не программисту.

### Решение
```python
print(f"В клетке {zoo.index('lion') + 1} сидит лев")
print(f"В клетке {zoo.index('lark') + 1} сидит жаворонок")
```

### Вывод программы 
![alt text](screenshots/image10.png)