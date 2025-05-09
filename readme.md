# README

## Опис проекту

Цей проект реалізує графову модель мережі метро Дніпра, включає візуалізацію графа, аналіз його характеристик, а також алгоритми для пошуку шляхів і найкоротших маршрутів.

### Завдання 1

**Файл:** `task_1.py`

1. **Створення графа:**
   - Граф представляє модель мережі метро Дніпра, де вершинами є станції, а ребрами — активні та неактивні маршрути між станціями.
2. **Візуалізація графа:**
   - Активні маршрути відображені червоними суцільними лініями, а неактивні — сірими пунктирними лініями.
3. **Аналіз характеристик графа:**
   - Визначено кількість вершин і ребер.
   - Проаналізовано ступені вершин (кількість зв'язків кожної станції).

### Завдання 2

**Файл:** `task_2.py`

1. **Реалізація алгоритмів:**
   - **DFS (глибина перший):** Алгоритм досліджує граф у глибину, проходячи по вершинах рекурсивно.
   - **BFS (ширина перший):** Алгоритм проходить граф у ширину, використовуючи чергу для відстеження вершин.
2. **Порівняння результатів:**
   - Результати алгоритмів різняться через відмінності у порядку обходу сусідніх вершин. DFS досліджує маршрути максимально глибоко перед поверненням, тоді як BFS досліджує всі сусідні вершини перед переходом до наступного рівня.
3. **Висновок:** Шляхи для алгоритмів залежать від структури графа і способу його обходу.

### Завдання 3

**Файл:** `task_3.py`

1. **Додавання ваг:**
   - Ребра графа отримали ваги, які відображають відстань між станціями (в метрах).
2. **Алгоритм Дейкстри:**
   - Реалізовано для знаходження найкоротших шляхів між усіма вершинами графа.
   - Алгоритм використовує ваги для розрахунку мінімальних відстаней.
3. **Візуалізація графа:**
   - Ваги ребер підписані на графі для наочності.

---

## Як запустити проект

1. Встановіть необхідні бібліотеки:
   ```bash
   pip install networkx matplotlib
   ```
2. Запустіть окремо кожен файл для виконання завдань:
   - Завдання 1: `python task_1.py`
   - Завдання 2: `python task_2.py`
   - Завдання 3: `python task_3.py`

---

## Результати

### Завдання 1

- Граф успішно створено та візуалізовано.
- Основні характеристики графа:
  - Кількість вершин: 12
  - Кількість ребер: 11
  - Ступені вершин:
    ```
    {'Parus': 1, 'Pokrovska': 2, 'Prospekt Svobody': 2, 'Zavodska': 2, 'Metalurgiv': 2, 'Metrobudivnykiv': 2, 'Vokzalna': 3, 'Zaliznychnyy vokzal': 1, 'Teatralna': 2, 'Centralna': 2, 'Muzejna': 2, 'Dnipro': 1}
    ```

## Завдання 2

Програмно реалізовано два алгоритми для обходу графа:

1. **DFS (глибина-спочатку)**: `['Pokrovska', 'Prospekt Svobody', 'Zavodska', 'Metalurgiv', 'Metrobudivnykiv', 'Vokzalna', 'Zaliznychnyy vokzal', 'Teatralna', 'Centralna', 'Muzejna', 'Dnipro', 'Parus']`
2. **BFS (ширина-спочатку)**: `['Pokrovska', 'Prospekt Svobody', 'Parus', 'Zavodska', 'Metalurgiv', 'Metrobudivnykiv', 'Vokzalna', 'Teatralna', 'Zaliznychnyy vokzal', 'Centralna', 'Muzejna', 'Dnipro']`

### Результати

- **DFS (глибина-спочатку):** Алгоритм обирає один з можливих шляхів і досліджує його до кінця, перш ніж повернутися до вузлів, які залишилися необробленими. У випадку графа Дніпровського метро, шлях DFS залежить від порядку сусідніх вершин у списку суміжності.

- **BFS (ширина-спочатку):** Алгоритм проходить граф рівнями, досліджуючи всі сусідні вершини на одному рівні, перш ніж перейти до наступного. Це забезпечує знаходження найкоротшого шляху (за кількістю ребер) від стартової вершини до кожної іншої вершини.

### Порівняння

| Характеристика   | DFS                                                              | BFS                                                             |
| ---------------- | ---------------------------------------------------------------- | --------------------------------------------------------------- |
| **Підхід**       | Рекурсивний (глибокий обхід)                                     | Ітеративний (пошук по рівнях)                                   |
| **Результат**    | Може не бути найкоротшим шляхом                                  | Завжди знаходить найкоротший шлях (за кількістю ребер)          |
| **Застосування** | Корисний для пошуку в глибину, наприклад, в лабіринтах або іграх | Ідеальний для пошуку найкоротших шляхів у ненавантажених графах |

### Обґрунтування різниці

- **DFS:** Шлях залежить від порядку, в якому додаються сусіди до списку суміжності. Оскільки алгоритм "поглинає" один шлях повністю до кінця, отриманий маршрут може бути не найкоротшим, якщо існують альтернативні коротші шляхи. У нашому графі, наприклад, DFS може обрати шлях через станцію, яка знаходиться далі, перш ніж повернутися до ближчих станцій.

- **BFS:** Оскільки BFS обробляє всі сусідні вузли рівня до переходу на глибший рівень, він гарантує, що знайдений шлях мінімізує кількість ребер між початковою та кінцевою точками. Для метро Дніпра це забезпечує оптимальні маршрути між станціями.

### Висновок

Для графа Дніпровського метро BFS надає практично корисні результати (найкоротший шлях), тоді як DFS може бути більш релевантним для специфічних задач, де глибокий пошук є пріоритетним.

---

### Завдання 3

- Найкоротші шляхи між усіма вершинами розраховані алгоритмом Дейкстри.
- Приклад результатів:
  ```
  Від Pokrovska до Prospekt Svobody: 1000 м
  Від Pokrovska до Zavodska: 2300 м
  ...
  ```

---
