
def ask_age():
    fun_age = 0
    while fun_age == 0:
        age_str = input("Quel est ton âge ? : ")
        try:
            fun_age = int(age_str)
        except ValueError:
            print("Erreur : L'âge est inccorecte, tu dois mettre un nombre !")
    return fun_age


def ask_name():
    name_answer = ""
    while name_answer == "":
        name_answer = input("Quel est ton nom ? : ")
    return name_answer


name = ask_name()
age = ask_age()
print(f"Ton nom est {name} et tu as {age} ans. L'an prochain tu auras " + str(age + 1) + " ans")
