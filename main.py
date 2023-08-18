import os
from typing import List

PHONEBOOK = "phonebook.txt"


def display_contacts(contacts: List[str], page: int, per_page: int):
    """
    Выводит на экран страницу записей из справочника.

    Args:
        contacts (List[str]): Список строк с контактами.
        page (int): Номер страницы для вывода.
        per_page (int): Количество записей на странице.

    Returns:
        None
    """
    start = (page - 1) * per_page
    end = start + per_page

    print("Список контактов:")
    for i, contact in enumerate(contacts[start:end], start=start + 1):
        print(f"{i}. {contact}")
    try:
        print(f"Страница {page}/{(len(contacts) + per_page - 1) // per_page}")
    except ZeroDivisionError:
        print("  Совпадения отсутствуют")



def add_contact() -> None:
    """
    Добавляет новую запись в справочник.

    Returns:
        None
    """
    last_name = input("Фамилия: ")
    first_name = input("Имя: ")
    middle_name = input("Отчество: ")
    organization = input("Название организации: ")
    work_phone = input("Рабочий телефон: ")
    personal_phone = input("Личный телефон (сотовый): ")
    contact = f"{last_name}, " \
              f"{first_name}, " \
              f"{middle_name}, " \
              f"{organization}, " \
              f"{work_phone}, " \
              f"{personal_phone}"
    with open(PHONEBOOK, "a") as file:
        file.write(contact + "\n")

    print("Контакт добавлен.")


def edit_contact() -> None:
    """
    Корректирует запись в справочнике.

    Returns:
        None
    """
    contacts = load_contacts()
    display_contacts(contacts, 1, len(contacts))

    index = int(input("Введите номер контакта для редактирования: ")) - 1
    if 0 <= index < len(contacts):
        new_info = input(
            "Введите новые данные для контакта (разделяя запятой): "
        )
        contacts[index] = new_info
        save_contacts(contacts)
        print("Контакт отредактирован.")
    else:
        print("Некорректный номер контакта.")


def search_contacts() -> None:
    """
    Поиск записи по параметру.

    Returns:
        None
    """
    query = input("Введите строку для поиска: ").lower()
    contacts = load_contacts()
    matching_contacts = [
        contact for contact in contacts if query in contact.lower()
    ]
    display_contacts(matching_contacts, 1, len(matching_contacts))


def load_contacts() -> List[str]:
    """
    Загружает контакты из файла.

    Returns:
        List[str]: Список строк, представляющих контакты.
    """
    if os.path.exists(PHONEBOOK):
        with open(PHONEBOOK, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []


def save_contacts(contacts: List[str]) -> None:
    """
    Сохраняет список контактов в файл.

    Args:
        contacts (List[str]): Список строк с контактами.
    """
    with open(PHONEBOOK, "w") as file:
        for contact in contacts:
            file.write(contact + "\n")


def main():
    """
    Основная функция для управления телефонным справочником через терминал.

    Returns:
        None
    """
    while True:
        print("\nТелефонный справочник")
        print("1. Вывод записей")
        print("2. Добавление записи")
        print("3. Редактирование записи")
        print("4. Поиск записей")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            contacts = load_contacts()
            per_page = 5
            page = 1
            while True:
                display_contacts(contacts, page, per_page)
                action = input(
                  "n - Следующая страница, "
                  "p - Предыдущая страница, "
                  "q - Вернуться в меню: "
                ).lower()
                if action == 'n':
                    page += 1
                elif action == 'p':
                    page = max(1, page - 1)
                elif action == 'q':
                    break
        elif choice == '2':
            add_contact()
        elif choice == '3':
            edit_contact()
        elif choice == '4':
            search_contacts()
        elif choice == '5':
            break


if __name__ == "__main__":
    main()
