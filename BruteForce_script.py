#import pour le timer, l'outil pour générer toutes les combinaisons
import hashlib
from os import close
import time
import itertools

#lancement du timer 
timerBegin = time.time()
#Toutes les variables dont avoir besoin, dont une liste de caractère pour toutes les possibilités
shadow = open("shadow","r")
Users = shadow.readlines()
chars = "`1234567890-=qwertyuiop[]asdfghjkl;'zxcvbnm,./!@#$%^&*()_+¡²³¤€¼½¾‘’¥×"
with open("resultBrutForce", "a") as r:
    r.write("voici le résultat en utilisa nt une méthode par force brute" + "\n")
close
#parcours les deux fichier pour trouver une similitude
for user in Users:
    username = user.split(":")[0]
    password = user.split(":")[1]
    #on applique les règles spécifiques au fichier
    if '$' in user:
        password = user.split(":")[1].split("$")[2]
        #on détermine qu'elle est la longueur minimum pour un script
        for number in range(8,12):
            #avec l'itertool on crée des produits qui vont tester tous les itérations possibles en dépend d'une longeuer
            for words in itertools.product(chars,repeat=number):
                word = ''.join(words)
                truepassword = word
                word = hashlib.md5(word.encode()).hexdigest()
                if word == password:
                    with open("result", "a") as r:
                        r.write("l'user se nomme : " + username + "\n" + "son mot de passe crypté est :  " + password + "\n")
                        r.write(" voici le mot de passe : " + truepassword + "\n")
                    close
                print("le temps de calcul a été de : " , (time.time() - timerBegin) , "s"  )
                print("l'user se nomme : " + username + "\n" + "son mot de passe crypté est :  " + password)
                print("voici le mot de passe : " + truepassword + "\n")
                break
    else: 
        print("le mot de passe ne peux pas etre lu pour l'utulisateur : " + username + "\n")  
print("vous pouvez trouver les mots de passe qui ont réussi a etre décrypter dans le fichier result!")