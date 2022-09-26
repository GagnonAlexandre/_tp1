#Alexandre Gagnon 401 13sept2022

def count_word() :
    #je demande a l'utilisateur decrire une phrase
    test_string = input("Ecrivez une phrase")
    #je demande au programe de recrire la phrase
    print("la phrase original : " + test_string)
    #je demande au programe de conter le nombre de mots
    res = len(test_string.split())
    #je demande au programe de dire le nombre de mots
    print("le nombre de mots est :" + str(res))
    #j'appelle la fonction
count_word()