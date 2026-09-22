from business import iss_position,astronauts_position

continuer = True

while continuer:
    print()
    print("Menu ISS")
    print(50 * "=")
    print("1 - Afficher la position de l'ISS")
    print("2 - Afficher les occupants de l'ISS")
    print("0 - Quitter")
    print()

    choix = input("Votre choix: ")

    if choix == "1":
        print(iss_position())

    elif choix == "2":
        print(astronauts_position())

    elif choix == "0":
        print("Au revoir !")
        continuer = False

    else:
        print("Choix invalide. Veuillez choisir une option entre 0 et 3.")
