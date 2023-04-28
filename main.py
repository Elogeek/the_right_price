# Import ce d'on j'ai besoin
from random import randint

# Choisir un nombre aléatoire entre 1 et 1000
just_price = randint(1, 1000)

# statut du jeu (activé/désactivé)
game_status = True

# tant que le jeu est en cours d'éxécution
while game_status:

    # demander à l'utilisateur d'entrer un prix dans la console
    user_price = int(input("Entrer un prix entre 1 et 1000 : "))

    # si le prix est le meme que le juste prix
    if user_price == just_price:
        print("Trouvé !")
        # fin du jeu
        game_status = False

    # si le prix de l'utilisateur est supérieur au prix à trouver
    elif user_price > just_price:
        print("C'est moins ! ")

    # si le prix de l'utilisateur est inférieur au prix à trouver
    elif user_price < just_price:
        print("C'est plus ! ")

# fin du jeu après la boucle
print("Fin du jeu !")
