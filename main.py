import json
# Функція для створення JSON файлу з початковими даними
def create_json_file(file_name):
    passengers = [
        {"name": "Ivanov", "items": 1, "weight": 4.5},
        {"name": "Petrov", "items": 3, "weight": 7.2},
        {"name": "Sidorov", "items": 5, "weight": 15.8},
        {"name": "Kuznetsova", "items": 2, "weight": 12.0},
        {"name": "Smirnov", "items": 4, "weight": 28.5},
        {"name": "Popov", "items": 1, "weight": 3.0},
        {"name": "Vasiliev", "items": 6, "weight": 45.3},
        {"name": "Fedorov", "items": 2, "weight": 10.0},
        {"name": "Nikolaev", "items": 3, "weight": 22.0},
        {"name": "Romanova", "items": 4, "weight": 5.5},
    ]
    with open(file_name, 'w') as file:
        json.dump(passengers, file, indent=4)
    print(f"Файл '{file_name}' створено.")


# Функція для читання JSON файлу та виведення вмісту
def read_json_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            print(json.dumps(data, indent=4))
    except FileNotFoundError:
        print(f"Файл '{file_name}' не знайдено.")
    except json.JSONDecodeError:
        print(f"Файл '{file_name}' не є коректним JSON.")


# Функція для додавання запису до JSON файлу
def add_record(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)

        name = input("Введіть прізвище пасажира: ")
        items = int(input("Введіть кількість речей: "))
        weight = float(input("Введіть вагу багажу: "))

        data.append({"name": name, "items": items, "weight": weight})

        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)

        print("Запис додано.")
    except FileNotFoundError:
        print(f"Файл '{file_name}' не знайдено.")
    except ValueError:
        print("Невірний формат введення даних.")


# Функція для видалення запису з JSON файлу
def delete_record(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)

        name = input("Введіть прізвище пасажира для видалення: ")

        updated_data = [record for record in data if record['name'] != name]

        with open(file_name, 'w') as file:
            json.dump(updated_data, file, indent=4)

        print("Запис видалено.")
    except FileNotFoundError:
        print(f"Файл '{file_name}' не знайдено.")
    except json.JSONDecodeError:
        print(f"Файл '{file_name}' не є коректним JSON.")


# Функція для пошуку даних за одним із полів
def search_data(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)

        field = input("Введіть поле для пошуку (name/items/weight): ")
        value = input("Введіть значення для пошуку: ")

        if field in ["items", "weight"]:
            value = float(value) if '.' in value else int(value)

        results = [record for record in data if record[field] == value]

        print("Результати пошуку:")
        print(json.dumps(results, indent=4))
    except FileNotFoundError:
        print(f"Файл '{file_name}' не знайдено.")
    except KeyError:
        print("Невірне поле для пошуку.")
    except json.JSONDecodeError:
        print(f"Файл '{file_name}' не є коректним JSON.")


# Функція для вирішення завдання
def solve_task(file_name, output_file):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)

        # Пасажири з більше ніж двома речами
        more_than_two_items = [p['name'] for p in data if p['items'] > 2]

        # Розподіл за вагою багажу
        weight_categories = {"less_than_5kg": 0, "from_5_to_25kg": 0, "more_than_25kg": 0}
        for p in data:
            if p['weight'] < 5:
                weight_categories["less_than_5kg"] += 1
            elif 5 <= p['weight'] <= 25:
                weight_categories["from_5_to_25kg"] += 1
            else:
                weight_categories["more_than_25kg"] += 1

        results = {
            "more_than_two_items": more_than_two_items,
            "weight_categories": weight_categories,
        }

        with open(output_file, 'w') as file:
            json.dump(results, file, indent=4)

        print(f"Результати завдання збережено у файл '{output_file}'.")
    except FileNotFoundError:
        print(f"Файл '{file_name}' не знайдено.")
    except json.JSONDecodeError:
        print(f"Файл '{file_name}' не є коректним JSON.")


# Основна програма
def main():
    file_name = "passengers.json"
    output_file = "task_results.json"

    while True:
        print("\nМеню:")
        print("1. Створити JSON файл із початковими даними")
        print("2. Вивести вміст JSON файлу")
        print("3. Додати запис у JSON файл")
        print("4. Видалити запис із JSON файлу")
        print("5. Шукати дані у JSON файлі")
        print("6. Розв'язати завдання та зберегти результати")
        print("7. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            create_json_file(file_name)
        elif choice == "2":
            read_json_file(file_name)
        elif choice == "3":
            add_record(file_name)
        elif choice == "4":
            delete_record(file_name)
        elif choice == "5":
            search_data(file_name)
        elif choice == "6":
            solve_task(file_name, output_file)
        elif choice == "7":
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
