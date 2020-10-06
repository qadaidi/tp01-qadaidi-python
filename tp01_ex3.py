"""
Programme calculant le niveau de risque cardiovasculaire. 
  Données : - L'Age de l'utilisateur
            - Le sexe de l'utilisateur
            - Si l'utilisateur est un fumeur ou non
            - Si l'utilisateur pratique du sport
            - Si l’utilisateur possède une alimentation trop sucrée
  Indications :
            - Si l'utilisateur est fumeur, le niveau de risque augmente de 2
            - Si l'utilisateur fait du sport, le niveau de risque diminue de 1
            - Si l'utilisateur est un homme de plus de 50 ans,
              le niveau de risque augmente de 1
            - Si l'utilisateur est une femme de plus de 60ans,
              le niveau de risque augmente de 1
            - Si l’utilisateur consomme trop de sucre, le niveau de risque augmente de 2
            
  Résultats : Un message spécifiant le niveau de risque obtenu.
            - Si le niveau de risque est inférieur ou égal à 1, le niveau de risque est faible.
            - Si le niveau de risque est de 2 à 3, le niveau de risque est élevé
            - Sinon il est très élevé.

"""
### Déclaration et initialisation des variables

age = int(input("Quel est votre age ? : "))
sexe:str = input("Quel est votre sexe ? (f ou h) : ")
fumeur:str = input("Etes vous fumeur ? (oui ou non) : ")
sport:str = input("Etes vous sportif ? (oui ou non) : ")
alim:str = input("Mangez-vous beaucoup d'aliments sucrés ? (oui ou non) : ")

### Séquence d'opération et affichage
                     
if fumeur == "oui":
    valeur_fum = 2
                
else:
                    
    valeur_fum = 0
                                
if sport == "oui":
    valeur_sport = - 1

else:
    
    valeur_sport = 0
       
if alim == "oui":
    
    valeur_alim = 2
    
else:
    
    valeur_alim = 0
    
                 
if age > 50 and sexe == "h":
    valeur_age = 1
    valeur_finale = valeur_alim + valeur_sport + valeur_fum + valeur_age
        
    if valeur_finale <= 1:
            print("Votre niveau de risque est faible (", valeur_finale,")")
    if valeur_finale == 2 or valeur_finale == 3:
            print("Votre niveau de risque est élevé (", valeur_finale,")")
            
    else:
                
                print("Votre niveau de risque est très élevé (", valeur_finale,")")
                
elif age > 60 and sexe == "f":
    valeur = 1
    valeur_finale = valeur_alim + valeur_sport + valeur_fum + valeur_age
        
    if valeur_finale <= 1:
            print("Votre niveau de risque est faible (", valeur_finale,")")
    if valeur_finale == 2 or valeur_finale == 3:
            print("Votre niveau de risque est élevé (", valeur_finale,")")
            
    else:
                
                print("Votre niveau de risque est très élevé (", valeur_finale,")")
                
else:
    valeur_finale = valeur_alim + valeur_sport + valeur_fum
    
    if valeur_finale <= 1:
            print("Votre niveau de risque est faible (", valeur_finale,")")
    if valeur_finale == 2 or valeur_finale == 3:
            print("Votre niveau de risque est élevé (", valeur_finale,")")
            
    else:
                
                print("Votre niveau de risque est très élevé (", valeur_finale,")")

            
    


    
                


    


