def menu():
    msg_list = [
        "Выберите пункт меню:",
        "1. Принять нового сотрудника",
        "2. Изменить данные сотрудника",
        "3. Поиск сотрудника",
        "4. Уволить сотрудника",
        "5. Показать всех сотрудников",
        "6. Экспортировать сотрудников в txt файл",
        "7. Импортировать сотрудников из csv файл",
        "0. Выход"
    ]
    
    [print(f"{v}") for v in msg_list]
    