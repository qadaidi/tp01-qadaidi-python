"""
Programme de calcul du prix d'un billet de transport journalier selon plusieurs rabais possibles.
    Prix normal d'un billet : 10chf
    Rabais étudiant : 2chf
    Rabais demi-tarif : 5chf
    Rabais groupe : 2 chf par billet acheté à partir de 4.
    Carte mensuelle : Billet gratuit

Indications :
    - Il est possible de bénéficier d'un rabais demi-tarif et étudiant
    - Le rabais groupe n’est cumulable avec aucun autre rabais
    - Il est possible d'avoir une carte mensuelle permettant d’avoir ce billet gratuitement

Contrainte : 
- Si la personne possède la carte mensuelle, il ne faut pas lui demander
d'autres informations.

"""

### Déclaration et initialisation des variables

prix: int = 10
rabais_etudiant: int = 2
rabais_demitarif: int = 5


### Séquence d'opération

while True:
    cmensuelle :str = input("Possèdez-vous la carte mensuelle ? (oui ou non) : ")
        
    if cmensuelle == "oui":
        prix = 0
        print("Le prix à payer est de", prix,"CHF.-")
  
        exit()
        
    else:
                cdemitarif :str = input("Possèdez-vous la carte demi-tarif ? (oui ou non) : ")
                if cdemitarif == "oui":
                    prix_dt = prix - rabais_demitarif
                    print("Le prix à payer est de", prix_dt,"CHF.-")

                    exit()
        
                else:
        
                        cetudiant :str = input("Possèdez-vous la carte étudiante ? (oui ou non) :") 
                        if cetudiant == "oui":
                            prix_e = prix - rabais_etudiant
                            print("Le prix à payer est de", prix_e,"CHF.-")
                            
                            exit()
        
                        else:
                
                                cmb = int(input("Combien de billets voulez-vous ?"))
                                if cmb >= 4:
                                    prix_cmb = 8 * cmb
                                    print("Le prix à payer est de", prix_cmb,"CHF.-")
                                    exit()
                    
                                else:
                    
                                        prix_cmb = prix * cmb
                                        print("Le prix à payer est de", prix_cmb,"CHF.-")
                                        exit()
                                
        



    
