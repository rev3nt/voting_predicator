def can_vote(age, citizenship, is_disqualified):
    if age < 18:
        return False
    elif citizenship != "Россия":
        return False
    elif is_disqualified == True:
        return False
    else:
        return True


age = 18
citizenship = "Россия"
is_disqualified = False

print("Вы можете голосовать") if can_vote(age, citizenship, is_disqualified) else  print("Вы не можете голосовать")