name = input("Quel est ton nom ? : ")
next_age = 0
while next_age == 0:

    try:
        age = int(input("Quel est ton âge ? : "))
        next_age = age + 1
    except ValueError:
        print("Erreur : L'âge est inccorecte, tu dois mettre un nombre !")

print(f"Tu t'appelles {name}, ton âge est {age} ans et l'an prochain tu auras : {next_age} ans.")
