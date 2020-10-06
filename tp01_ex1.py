"""
Programme permettant de convertir une quantité en plusieurs unités d'énergie.

1J  =  0.738 ft-lb  =  0.239 cal  =  6.24*10^18 eV

Unités : joule, calorie, Ft-lb et eV
  Données : Une valeur et une unité
  Indications:
        Selon l'unité entrée par l'utilisateur, afficher la conversion
        dans les 3 autres unités.
  Résultats : Affichage des conversions
"""

### Déclaration et initialisation des variables

joule: float= 1
ftlb: float= 0.738
cal: float= 0.239
ev: float= 6.24*10**18

qnt_energie :float = float(input("Quelle est la quantité d'énergie à convertir ? : "))
unite :str = str(input("Unité (J, ft-lb, cal ou eV) ? : "))

                                            
### Séquence d'opération

if unite == "J":
    
    ftlbs = qnt_energie * ftlb
    cals = qnt_energie * cal
    evs = qnt_energie * ev
    
    print("En ft-lb : ", ftlbs)
    print("En calories : ", cals)
    print("En eV : ", evs)
    
elif unite == "ft-lb":
    
    joules = qnt_energie / ftlb
    cals = qnt_energie * cal / ftlb
    evs = qnt_energie * ev / ftlb
    
    print("En joules : ", joules)
    print("En calories : ", cals)
    print("En éléctro-Volt : ", evs)
    
elif unite == "cal":
    
    joules = qnt_energie / cal
    cals = qnt_energie * ftlb / cal
    evs = qnt_energie * ev /cal
    
    print("En joules : ", joules)
    print("En calories : ", cals)
    print("En éléctro-Volt : ", evs)

elif unite == "eV":
    
    joules = qnt_energie * joule / ev
    cals = qnt_energie * cal / ev
    ftlbs = qnt_energie * ftlb / ev
    
    print("En joules : ", joules, "J")
    print("En calories : ", cals, "cal")
    print("En ft-lb : ", ftlbs, "ft-lb")
    

