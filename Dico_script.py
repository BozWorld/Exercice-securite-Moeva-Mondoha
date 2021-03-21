import hashlib
import time
shadow = open("shadow","r")
dico = open("dico_mini_fr","r")

Users = shadow.readlines()
worldlist = dico.readlines()
for user in Users:
    username = user.split(":")[0]
    password = user.split(":")[1]
    if "!" in user: 
        print("le mot de passe ne peux pas etre lu pour l'utulisateur : " + username + "\n")
    if '$' in user:
        password = user.split(":")[1].split("$")[2]
        for word in worldlist:
            truepassword = word
            word.strip('\n')
            word = hashlib.md5(word.strip('\n').encode()).hexdigest()
            if word == password:
                with open("result", "a") as r:
                    r.write("l'user se nomme : " + username + "\n" + "son mot de passe crypté est :  " + password)
                    r.write(" voici le mot de passe : " + truepassword + "\n")
                print("l'user se nomme : " + username + "\n" + "son mot de passe crypté est :  " + password)
                print("voici le mot de passe : " + truepassword + "\n")
                print("vous pouvez trouver les mots de passe qui ont réussi a etre décrypter dans le fichier result!")
                break   