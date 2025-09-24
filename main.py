def can_vote(age, citizenship, is_disqualified):
    if age < 18 or citizenship != "россия" or is_disqualified != "нет":
        return False
    else:
        return True


try:
    age = int(input("Введите ваш возраст: "))
    citizenship = input("Введите страну, в которой у вас гражданство: ").lower()
    disqualified = input("Вы признанны недееспособным или содержащийся в местах лишения свободы(да, нет): ").lower()

    print("Вы можете голосовать") if can_vote(age, citizenship, disqualified) else print("Вы не можете голосовать")
except:
    print("Веденные данные - некорректны")