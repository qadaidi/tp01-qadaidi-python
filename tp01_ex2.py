"""
Programme simulant un distributeur de snacks
 Données : - Un montant entré par l'utilisateur
           - Un numéro d'article entré par l'utilisateur
 Indications :
           Le distributeur comporte :
           - Fanta orange à 2.90
           - Coca cola à 2.90
           - Coca cola light à 2.70
           - Henniez à 2.30
           - Ice Tea à 2.20
           - Limonade à 1.90
           
 Résultats : - Un message d’annulation de la transaction
                 (« Produit inconnu / Monnaie insuffisante »)
             - Un message indiquant la monnaie rendue si existante
             - Un message indiquant le produit vendu et souhaitant "santé"

"""

### Déclaration et initialisation des variables

print("Bienvenue ! Voici notre sélection de produit :")
print("----------------------------------------------")
print("1. Fanta Orange")
print("2. Coca cola")
print("3. Coca cola light")
print("4. Henniez")
print("5. Ice tea")
print("6. Limonade")

fanta : float = 2.90
coca : float = 2.90
cocalight : float = 2.70
henniez : float = 2.30
icetea : float = 2.20
limonade : float = 1.90

monnaie :float = float(input("Veuillez introduire votre monnaie : "))
produit :str = input("Veuillez sélectionner un produit : ")

### Séquence d'opération

if produit == "1" and monnaie > fanta:
    fanta_rendre = monnaie - fanta
    print("Voici votre monnaie : ", fanta_rendre)
    print("Fanta servi! Santé!")
    
elif produit == "2" and monnaie > coca:
    coca_rendre = monnaie - coca
    print("Voici votre monnaie : ", coca_rendre)
    print("Coca servi! Santé!")
    
elif produit == "3" and monnaie > cocalight:
    cocalight_rendre = monnaie - cocalight
    print("Voici votre monnaie : ", cocalight_rendre)
    print("Coca-light servi! Santé!")
    
elif produit == "4" and monnaie > henniez:
    henniez_rendre = monnaie - henniez
    print("Voici votre monnaie : ", henniez_rendre)
    print("Henniez servi! Santé! De l'eau, c'est mieux!")
    
elif produit == "5" and monnaie > icetea:
    icetea_rendre = monnaie - icetea
    print("Voici votre monnaie : ", icetea_rendre)
    print("Thé froid servi! Santé!")
       
elif produit == "6" and monnaie > limonade:
    limonade_rendre = monnaie - limonade
    print("Voici votre monnaie : ", limonade_rendre)
    print("Limonade servi! Santé!")
    
else :
        
        print ("Produit inconnu ou monnaie insuffisante")
    
    
    


