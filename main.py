def can_vote(age, citizenship, is_disqualified):
    if age < 18:
        return False
    elif citizenship != "россия":
        return False
    elif is_disqualified == True:
        return False
    else:
        return True


try:
    age = int(input("Введите ваш возраст: "))
    citizenship = input("Введите страну, в которой у вас гражданство: ").lower()
    disqualified_input = int(input("Дисквалифицированы ли вы с выборов (0 - нет, 1 - да): "))
    assert disqualified_input == 0 or disqualified_input == 1

    is_disqualified = bool(disqualified_input)
except:
    print("Веденные данные - некорректны")
else:
    print("Вы можете голосовать") if can_vote(age, citizenship, is_disqualified) else print("Вы не можете голосовать")
