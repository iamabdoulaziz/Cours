
def ask_name():
    name_answer = ""
    while name_answer == "":
        name_answer = input("Quel est ton nom ? : ")
    return name_answer


def ask_age(person_name):
    fun_age = 0
    while fun_age == 0:
        age_str = input(person_name + " Quel est ton âge ? : ")
        try:
            fun_age = int(age_str)
        except ValueError:
            print("Erreur : L'âge est inccorecte, tu dois mettre un nombre !")
    return fun_age


name = ask_name()
age = ask_age(name)

def print_function(person_name, person_age):
    print(f"Tu t'appelles : {person_name}")
    print(f"Ton âge est : {person_age} ans")
    print("L'an prochain tu auras " + str(person_age + 1) + " ans.")
    if person_age == 17:
        print("Tu es presque majeur !")
    elif person_age == 18:
        print("Tout juste majeur : Félicitations !")
    elif person_age > 18:
        print("Tu es majeur")
    else:
        print("Tu es mineur !")


print_function(name, age)
