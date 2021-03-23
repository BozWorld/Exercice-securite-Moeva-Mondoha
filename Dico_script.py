import hashlib
from os import close
import time

#lancement du timer 
timerBegin = time.time()

#ouverture des fichier pour le crackage
shadow = open("shadow","r")
dico = open("dico_mini_fr","r")

#variable
Users = shadow.readlines()
worldlist = dico.readlines()
inDico = True

with open("result", "a") as r:
    r.write("voici le résultat en utilisa nt une méthode par dictionnaire" + "\n")
close

for user in Users:
    username = user.split(":")[0]
    password = user.split(":")[1]
    #on applique les régles spécifique au fichier
    if '$' in user:
        password = user.split(":")[1].split("$")[2]
        for word in worldlist:
            inDico = False
            truepassword = word
            word.strip('\n')
            #avec cet méthode on encrypte le mot de notre liste pour le ressortir en version hashé
            word = hashlib.md5(word.strip('\n').encode()).hexdigest()
            if word == password:
                inDico = True
                with open("result", "a") as r:
                    r.write("l'user se nomme : " + username + "\n" + "son mot de passe crypté est :  " + password + "\n")
                    r.write(" voici le mot de passe : " + truepassword + "\n")
                close
                print("le temps de calcul a été de : " , (time.time() - timerBegin) , "s"  )
                print("l'user se nomme : " + username + "\n" + "son mot de passe crypté est :  " + password)
                print("voici le mot de passe : " + truepassword + "\n")
                break
        if inDico == False:
            print("le mot de passe de l'utilisateur : " + username + " n'es pas dans le dictionnaire" + "\n")
    else: 
        print("le mot de passe ne peux pas etre lu pour l'utulisateur : " + username + "\n")
print("vous pouvez trouver les mots de passe qui ont réussi a etre décrypter dans le fichier result!")