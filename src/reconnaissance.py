from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles



#fonction reconnaissance modifiée pour retourner l'indice ET la proportion de similitude
def reconnaissance_chiffre_(image, liste_modeles, S):
    image_binarisee = image.binarisation(S)
    image_localisee = image_binarisee.localisation()
    
    tab_similitude = [] #liste des similitudes entre notre image et tous les modèles
    for x in liste_modeles : #x est une image modèle
        image_resized = image_localisee.resize(x.H,x.W) #on redimensionne notre image à la taille de l'image modèle pour pouvoir les comparer
        similitude = image_resized.similitude(x)
        tab_similitude.append(similitude)
    
    ind_max_similitude = 0  
    max_similitude = 0
    for i in range (len(tab_similitude)): #on recherche le modèle qui a le plus de similitude avec notre image
        if tab_similitude[i]>max_similitude:
            max_similitude = tab_similitude[i]
            ind_max_similitude = i
    return ind_max_similitude, max_similitude






#fonction reconnaissance copiée pour valider les tests Github
def reconnaissance_chiffre(image, liste_modeles, S):
    image_binarisee = image.binarisation(S)
    image_localisee = image_binarisee.localisation()
    
    tab_similitude = [] #liste des similitudes entre notre image et tous les modèles
    for x in liste_modeles : #x est une image modèle
        image_resized = image_localisee.resize(x.H,x.W) #on redimensionne notre image à la taille de l'image modèle pour pouvoir les comparer
        similitude = image_resized.similitude(x)
        tab_similitude.append(similitude)
    
    ind_max_similitude = 0  
    max_similitude = 0
    for i in range (len(tab_similitude)): #on recherche le modèle qui a le plus de similitude avec notre image
        if tab_similitude[i]>max_similitude:
            max_similitude = tab_similitude[i]
            ind_max_similitude = i
    return ind_max_similitude
