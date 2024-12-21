# Домашняя работа №1 Эмулятор оболочки ОС

## Описание проекта

Эмулятор оболочки ОС представляет собой консольное приложение, имитирующее сеанс командной строки в UNIX-подобной операционной системе. Он позволяет пользователю взаимодействовать с виртуальной файловой системой, упакованной в ZIP-архив, и выполнять базовые команды.

## Функциональные возможности

- **Поддерживаемые команды:**
  - `ls`: отображает список файлов и директорий в текущей директории.
  - `cd <directory>`: изменяет текущую директорию.
  - `exit`: завершает работу эмулятора.
  - `head <file>`: выводит первые строки указанного файла.
  - `whoami`: выводит имя текущего пользователя.

- **Конфигурация:**
  Эмулятор принимает конфигурационный файл в формате JSON, который содержит:
  - Имя пользователя для отображения в приглашении.
  - Путь к архиву виртуальной файловой системы.
  - Путь к лог-файлу.
  - Путь к стартовому скрипту.




# Домашняя работа №2 Инструмент командной строки для визуализации графа зависимостей

## Описание проекта

Данный проект представляет собой инструмент командной строки, предназначенный для визуализации графа зависимостей JavaScript-пакетов (npm), включая транзитивные зависимости. Визуализация осуществляется с использованием представления PlantUML, что позволяет пользователю получать наглядное представление о зависимостях пакета.

## Функциональные возможности

- **Анализ зависимостей:**
  - Инструмент анализирует указанный JavaScript-пакет и извлекает все его зависимости, включая транзитивные.

- **Визуализация:**
  - Граф зависимостей выводится на экран в виде кода PlantUML, что позволяет легко интегрировать его в другие системы или использовать для дальнейшей обработки.

- **Конфигурация:**
  Визуализатор принимает конфигурационный файл в формате INI, который содержит:
  - Путь к программе для визуализации графов.
  - Имя анализируемого пакета.
  - Путь к файлу-результату в виде кода.
  - URL-адрес репозитория.




# Домашняя работа №3 Инструмент командной строки для преобразования YAML в учебный конфигурационный язык

## Описание проекта

Данный проект представляет собой инструмент командной строки, который преобразует текст из формата YAML в учебный конфигурационный язык, описанный ниже. Инструмент выявляет синтаксические ошибки и выводит соответствующие сообщения. 

## Формат входных данных

- **Входной текст:** YAML, принимаемый из стандартного ввода.
- **Выходной текст:** Учебный конфигурационный язык, сохраняемый в файл по указанному пути.

## Синтаксис учебного конфигурационного языка

- **Массивы:** 
  ```
  [ значение значение значение ... ]
  ```

- **Словари:**
  ```
  @{
    имя = значение;
    имя = значение;
    имя = значение;
    ...
  }
  ```

- **Имена:** 
  - Состоит из заглавных букв: `[A-Z]+`

- **Значения:**
  - Числа
  - Строки
  - Массивы
  - Словари

- **Строки:**
  ```
  'Это строка'
  ```

- **Объявление константы на этапе трансляции:**
  ```
  const имя = значение;
  ```

- **Вычисление константы на этапе трансляции:**
  ```
  $имя$
  ```

## Функциональные возможности

- **Преобразование:** 
  Инструмент принимает YAML на стандартном вводе и преобразует его в указанный формат.

- **Обработка ошибок:**
  Все синтаксические ошибки выявляются с выводом соответствующих сообщений.




# Домашняя работа № 4 Ассемблер и интерпретатор для учебной виртуальной машины (УВМ)

## Описание проекта

Данный проект включает в себя разработку ассемблера и интерпретатора для учебной виртуальной машины (УВМ). Ассемблер преобразует текстовые команды в бинарный формат, а интерпретатор выполняет эти команды, сохраняя результаты в формате JSON.

## Формат команд УВМ

### 1. Загрузка константы
**Команда:** `A B C`  
- **Биты:** 0–7 (A), 8–26 (B), 27–38 (C)  
- **Размер команды:** 5 байт  
- **Описание:** Загружает константу C в память по адресу B.

**Тест:**  
- **A=10, B=709, C=158**  
- **Бинарный код:** `0x0A, 0xC5, 0x02, 0xF0, 0x04`

### 2. Чтение значения из памяти
**Команда:** `A B C D`  
- **Биты:** 0–7 (A), 8–26 (B), 27–45 (C), 46–50 (D)  
- **Размер команды:** 7 байт  
- **Описание:** Читает значение из памяти по адресу, который является суммой адреса (значение по адресу B) и смещения D, и сохраняет его по адресу C.

**Тест:**  
- **A=224, B=359, C=35, D=21**  
- **Бинарный код:** `0xE0, 0x67, 0x01, 0x18, 0x01, 0x40, 0x05`

### 3. Запись значения в память
**Команда:** `A B C`  
- **Биты:** 0–7 (A), 8–26 (B), 27–45 (C)  
- **Размер команды:** 6 байт  
- **Описание:** Записывает значение из памяти по адресу C в память по адресу B.

**Тест:**  
- **A=70, B=295, C=363**  
- **Бинарный код:** `0x46, 0x27, 0x01, 0x58, 0x0B, 0x00`

### 4. Бинарная операция: деление
**Команда:** `A B C D`  
- **Биты:** 0–7 (A), 8–26 (B), 27–45 (C), 46–64 (D)  
- **Размер команды:** 9 байт  
- **Описание:** Делит значение по адресу C на значение по адресу, который содержит значение по адресу B, и сохраняет результат по адресу D.

**Тест:**  
- **A=173, B=766, C=805, D=645**  
- **Бинарный код:** `0xAD, 0xFE, 0x02, 0x28, 0x19, 0x40, 0xA1, 0x00, 0x00`

## Функциональные возможности

### Ассемблер
- **Вход:** Файл с текстом исходной программы, путь к которому задается из командной строки.
- **Выход:** Бинарный файл в виде последовательности байт, путь к которому также задается из командной строки.
- **Лог:** Файл-лог, который содержит ассемблированные инструкции в формате "ключ=значение".

### Интерпретатор
- **Вход:** Бинарный файл с командами УВМ.
- **Выход:** Файл-результат, содержащий значения из указанного диапазона памяти УВМ в формате JSON.
