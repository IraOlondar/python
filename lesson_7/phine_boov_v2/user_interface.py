def menu():
    msg_list = [
        "Выберите пункт меню:",
        "1. Очистить/создать пустую базу данных",
        "2. Добавить новый контакт",
        "3. Изменить номер телефона",
        "4. Изменить фамилию",
        "5. Поиск по части имени, фамилии или номера",
        "6. Удалить контакт",
        "7. Показать все контакты",
        "8. Экспортировать контакты в txt файл",
        "9. Импортировать контакты из csv файл",
        "0. Выход"
    ]
    
    [print(f"{v}") for v in msg_list]
    
