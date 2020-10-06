"""
Programme testant si une date, saisie par l'utilisateur, est valide ou non.
Données : Une date saisie par l'utilisateur
Indications:
        Pour pouvoir déterminer si une année est bissextile :       
            - Si une année n'est pas multiple de 4, on s'arrête là, elle n'est pas bissextile.
            - Si elle est multiple de 4, on regarde si elle est multiple de 100.
                - Si c'est le cas, on regarde si elle est multiple de 400.
            - Si c'est le cas, l'année est bissextile.
                                - Sinon, elle n'est pas bissextile.
- Sinon, elle est bissextile.

Résultats : Un message spécifiant si la date entrée est valide.

"""

### Déclaration et initialisation des variables

jour = int(input("Saisissez un jour : "))
mois = int(input("Saisissez un mois : "))
annee  = int(input("Saisissez une année : "))

### Séquence d'opération

if annee % 4 == 0 and annee % 100 != 0:
    
    print(annee, "est bissextile")
    
elif annee % 100 == 0:
    
    print(annee, "n'est pas bissextile")
    
elif annee % 400 == 0:
    
    print(annee, "est bissextile")
    
elif mois > 12 or mois < 0 or jour > 31 or jour < 0 or annee < 1500:
    
    print("Date invalide")
    
else:
    
    print(annee, "n'est pas bissextile")
    
    


        
