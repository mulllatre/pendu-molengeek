import random

list_mot = ["hello", "dev", "python", "molengeek", "bruxelles", "europe"]

def mN(list_mot):
    mot = random.choice(list_mot)
    LT = []
    faute = 6

    while True:
        affichage = ''
        for lettre in mot:
            if lettre in LT:
                affichage += lettre
            else:
                affichage += '-'
        print(affichage)

        if faute == 0:
             print("Tu as depasser ta limite de faute, ressaye !!")
             break
        
        in_user = input("\nVeuillez entrer une lettre : ")
        
        if len(in_user) != 1:
             print("\nTu fais quoi, rentre une lettre!")
             continue
        
        if in_user in mot:
            print("\nExacte ! : ", in_user)
            LT.append(in_user)
            print("il te reste", faute, "essaye\n")
        elif in_user != mot[0]:
            print("\nMauvais choix ! : ", in_user)
            faute -= 1
            print("il te reste", faute, "essaye\n")

        if all(lettre in LT for lettre in mot):
            print("\nBravo tu as bien jouer le mot est :", mot)
            print("\nVoici ton nombre de faute : ",f"{faute}/6")
            break  


launch = input("Bienvenue sur le jeux du pendu, Voulez vous jouer ? (Oui/Non) : ")
print(' ')

while True:
        if launch.lower() == 'oui':
                mN(list_mot)
                break
        elif launch.lower() == 'non':
                print("Merci de votre reponse, a bientot avec Molengeek")
                break
        else:
                print("\nVeuillez donner votre reponse s'il vous plait !!!\n")
                launch = input("Bienvenue sur le jeux du pendu, Voulez vous jouer ? (Oui/Non) : ")
                print(' ')
       
