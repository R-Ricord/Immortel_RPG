nom_joueur = "Kaya"
pv_joueur = 1200
pv_max_joueur = 1500
endurance_joueur = 300
endurance_max_joueur = 500

garde_active = False

concentration_disponible = True

cle_langue_ancienne = False

nom_ennemi = "Créature des Ruines"
pv_ennemi = 800
pv_max_ennemi = 800

nom_chimere = "Chimère"
pv_chimere = 3500
pv_max_chimere = 3500

def attaquer(pv_ennemi, degats, nom_ennemi, pv_max_ennemi):
    print(f"{nom_joueur} attaque {nom_ennemi} !")
    print(f"{nom_joueur} inflige {degats} points de dégâts à {nom_ennemi}.")
    pv_ennemi -= degats
    if pv_ennemi < 0:
        pv_ennemi = 0
    print(f"{nom_ennemi} : {pv_ennemi} / {pv_max_ennemi} PV")
    return pv_ennemi

def attaquer_ennemi(pv_joueur, degats, nom_ennemi, nom_joueur, pv_max_joueur):
    print()
    print(f"{nom_ennemi} attaque {nom_joueur} !")
    print(f"{nom_ennemi} inflige {degats} points de dégâts à {nom_joueur}.")
    pv_joueur -= degats
    if pv_joueur < 0:
        pv_joueur = 0
    print(f"{nom_joueur} : {pv_joueur} / {pv_max_joueur} PV")
    return pv_joueur

print("=" * 50)
print("           IMMORTEL : LE RPG")
print("=" * 50)

print()
print("        PROLOGUE — L'ÉVEIL DE KAYA")
print()

print("Le silence règne sur les terres d'Etheria.")
print("Kaya est inconsciente au milieu des ruines.")

print()
print("-" * 50)
print(f"Personnage : {nom_joueur}")
print("-" * 50)
print()

input("Appuie sur Entrée pour commencer l'aventure...")

print()

input("Appuie sur Entrée pour que Kaya ouvre les yeux...")

print()
print("Kaya se redresse lentement.")
print()

while True:
    print()
    print("Que veux-tu faire ?")
    print()
    print("1 - Observer les environs")
    print("2 - Avancer dans les ruines")
    print("3 - Vérifier l'état de Kaya")
    if concentration_disponible:
        print("4 - Se Concentrer (gain : 50 END)")

    choix = input("Ton choix : ")
    print()
    if choix == "1":
        print()
        print("Kaya observe les environs.")
        print("Le vent soulève la poussière des ruines.")
        print("Aucun ennemi n'est visible.")

    elif choix == "2":
        print()
        print("Kaya avance prudemment entre les pierres.")
        print("Une étrange présence se fait ressentir...")
        break

    elif choix == "3":
        print()
        print("=== ÉTAT DE KAYA ===")
        print(f"PV : {pv_joueur} / {pv_max_joueur}")
        print(f"Endurance : {endurance_joueur} / {endurance_max_joueur}")

    elif choix == "4" and concentration_disponible:
        print()
        print("Kaya se concentre.")
        print("Elle récupère 50 points d'endurance.")
        endurance_joueur += 50
        if endurance_joueur > endurance_max_joueur:
            endurance_joueur = endurance_max_joueur
        concentration_disponible = False
        print(f"Endurance actuelle : {endurance_joueur} / {endurance_max_joueur}")

    else:
        print()
        print("Choix invalide.")

print()
print("=" * 50)
print("           LES RUINES D'ETHERIA")
print("=" * 50)
print()

print("Kaya s'enfonce dans les ruines.")
print("Plus elle avance, plus le silence devient pesant.")
print()
print("Soudain, un bruit résonne derrière elle...")
print()

input("Appuie sur Entrée pour te retourner...")

print()
print("Une créature surgit des décombres !")
print("Ses yeux brillent d'une lueur malveillante.")
print()
print("Elle se prépare à attaquer Kaya !  ")

concentration_disponible = True

print()
print("=== COMBAT ===")
print()
print(f"{nom_ennemi} :")
print(f"{pv_ennemi} / {pv_max_ennemi} PV")

while pv_ennemi > 0 and pv_joueur > 0:

    action_effectuee = False

    print()
    print("=== TOUR DE KAYA ===")
    print()
    print("1 - Attaque simple")
    print("2 - Compétences")
    if concentration_disponible:
        print("3 - Se Concentrer (gain : 50 END)")

    choix_combat = input("Ton choix : ")

    if choix_combat == "1":
        pv_ennemi = attaquer(pv_ennemi, 200, nom_ennemi, pv_max_ennemi)
        action_effectuee = True

    elif choix_combat == "2":
        print()
        print("=== COMPÉTENCES DE KAYA ===")
        print("1 - Frappe Lourde (coût : 100 END)")
        print("2 - Garde Défensive (coût : 50 END / gain : 100 END)")
        print("3 - Retour")
        print()

        choix_competence = input("Ton Choix : ")

        if choix_competence == "1":
            if endurance_joueur >= 100:
                print()
                print("Kaya utilise Frappe Lourde !")
                print(f"{nom_joueur} inflige 350 points de dégâts à {nom_ennemi}.")
                pv_ennemi -= 350
                if pv_ennemi < 0:
                    pv_ennemi = 0
                endurance_joueur -= 100
                print()
                print(f"{nom_ennemi} : {pv_ennemi} / {pv_max_ennemi} PV")
                print()
                print(f"Endurance actuelle : {endurance_joueur} / {endurance_max_joueur}")
                action_effectuee = True
            else:
                print()
                print("Pas assez d'endurance pour utiliser Frappe Lourde.")

        elif choix_competence == "2":
            if endurance_joueur >= 50:
                print()
                print("Kaya utilise Garde Défensive !")
                print("Elle récupère 50 points d'endurance.")
                garde_active = True
                endurance_joueur -= 50
                endurance_joueur += 100
                if endurance_joueur > endurance_max_joueur:
                    endurance_joueur = endurance_max_joueur
                print(f"Endurance actuelle : {endurance_joueur} / {endurance_max_joueur}")
                action_effectuee = True
            else:
                print()
                print("Pas assez d'endurance pour utiliser Garde Défensive.")

        elif choix_competence == "3":
            print()

        else:
            print()
            print("Choix invalide.")

    elif choix_combat == "3" and concentration_disponible:
        print()
        print("Kaya se concentre.")
        print("Elle récupère 50 points d'endurance.")
        endurance_joueur += 50
        if endurance_joueur > endurance_max_joueur:
            endurance_joueur = endurance_max_joueur
        concentration_disponible = False
        print(f"Endurance actuelle : {endurance_joueur} / {endurance_max_joueur}")
        action_effectuee = False

    else:
        print()
        print("Choix invalide.")

    if pv_ennemi <= 0:
        print()
        print(f"{nom_ennemi} a été vaincu !")

    if action_effectuee and pv_ennemi > 0:
        print()
        print("=== TOUR DE L'ENNEMI ===")
        degats_ennemi = 150
        if garde_active:
            print()
            print("La garde de Kaya réduit les dégâts subis de moitié!")
            degats_ennemi = degats_ennemi // 2
            garde_active = False
        pv_joueur = attaquer_ennemi(pv_joueur, degats_ennemi, nom_ennemi, nom_joueur, pv_max_joueur)

    if pv_joueur <= 0:
        print()
        print(f"{nom_joueur} a été vaincu !")

if pv_joueur <= 0:
    print()
    print("Kaya s'effondre au sol, vaincue par la créature.")
    print("Les ruines d'Etheria restent silencieuses et impitoyables.")
    print("GAME OVER.")
    exit()

print()
print("Kaya reprend son souffle.")
print("Le silence règne à nouveau sur les ruines d'Etheria.")
print("Un nuage de poussière se dissipe au loin dans les ruines, révélant une stèle ensevelie dans les décombres.")
print("Kaya s'approche de la stèle, intriguée par sa couleur, un turquoise éclatant.")
print()

input("Appuie sur Entrée pour que Kaya examine la stèle...")

print("Kaya découvre une inscription en or, gravée en langue ancienne sur la stèle.")
print("« Ces symboles sont les mêmes que ceux inscrits sur l'Obélisque de la Lumière. »")

cle_langue_ancienne = True

print("La stèle semble entrer en résonance avec Kaya, elle se met à briller.")
print("Une énergie turquoise parcourt le corps de Kaya.")
print("Ses blessures se referment et sa fatigue se dissipe.")
print()

pv_joueur = pv_max_joueur
endurance_joueur = endurance_max_joueur
concentration_disponible = True

input ("Appuie sur Entrée pour vérifier l'état de Kaya...")

print()
print(f"PV : {pv_joueur} / {pv_max_joueur}")
print(f"Endurance : {endurance_joueur} / {endurance_max_joueur}")
print()
print("« Je me sens beaucoup mieux ! »")
print()

print("La lueur que la stèle émet est de plus en plus intense.")
print()

input("Appuie sur Entrée pour observer la stèle...")

print()
print("Un énorme rugissement retentit dans les ruines, laissant Kaya terrifiée.")
print("Le sol se met à trembler, comme si quelque chose de colossal s'approchait, de plus en plus pressant.")
print("Soudain, plus un bruit, plus un tremblement, plus de lumière, juste un souffle chaud dans le dos de Kaya.")
print()

input("Appuie sur Entrée pour que Kaya se retourne...")

print()
print("Une immense créature se dresse devant Kaya, ses yeux rouges sang semblants transpercer son âme.")
print("Cette créature à tête de lion, au corps d'ours et aux ailes de dragon, a un serpent en guise de queue, et ses griffes acérées sont chacune plus grande que Kaya.")
print("La chimère déploie ses ailes, pousse un rugissement faisant trembler les environs et commence à lever l'une de ses pattes, prête à s'abattre sur Kaya.")
print("Kaya arme son épée, prête à se lancer dans le combat, malgré la peur faisant trembler chacun de ses membres.")
print()

input("Appuie sur Entrée pour engager le combat...")

print()
print("=== COMBAT ===")
print()
print(f"{nom_chimere} :")
print(f"{pv_chimere} / {pv_max_chimere} PV")

while pv_chimere > 0 and pv_joueur > 100:

    action_effectuee = False

    print()
    print("=== TOUR DE KAYA ===")
    print()
    print("1 - Attaque simple")
    print("2 - Compétences")
    if concentration_disponible:
        print("3 - Se Concentrer (gain : 50 END)")
    print()
    
    choix_combat = input("Ton choix : ")

    if choix_combat == "1":
        pv_chimere = attaquer(pv_chimere, 200, nom_chimere, pv_max_chimere)
        action_effectuee = True

    elif choix_combat == "2":
        print()
        print("=== COMPÉTENCES DE KAYA ===")
        print("1 - Frappe Lourde (coût : 100 END)")
        print("2 - Garde Défensive (coût : 50 END / gain : 100 END)")
        print("3 - Retour")
        print()
    
        choix_competence = input("Ton Choix : ")
    
        if choix_competence == "1":
            if endurance_joueur >= 100:
                print()
                print("Kaya utilise Frappe Lourde !")
                print(f"{nom_joueur} inflige 350 points de dégâts à {nom_chimere}.")
                print()
                pv_chimere -= 350
                if pv_chimere < 0:
                    pv_chimere = 0
                endurance_joueur -= 100
                print(f"{nom_chimere} : {pv_chimere} / {pv_max_chimere} PV")
                print()
                print(f"Endurance actuelle : {endurance_joueur} / {endurance_max_joueur}")
                action_effectuee = True
            else:
                print()
                print("Pas assez d'endurance pour utiliser Frappe Lourde.")
    
        elif choix_competence == "2":
            if endurance_joueur >= 50:
                print()
                print("Kaya utilise Garde Défensive !")
                print("Elle récupère 50 points d'endurance.")
                garde_active = True
                endurance_joueur -= 50
                endurance_joueur += 100
                if endurance_joueur > endurance_max_joueur:
                    endurance_joueur = endurance_max_joueur
                print(f"Endurance actuelle : {endurance_joueur} / {endurance_max_joueur}")
                action_effectuee = True
            else:
                print()
                print("Pas assez d'endurance pour utiliser Garde Défensive.")
    
        elif choix_competence == "3":
            print()
    
        else:
            print()
            print("Choix invalide.")
    
    elif choix_combat == "3" and concentration_disponible:
        print()
        print("Kaya se concentre.")
        print("Elle récupère 50 points d'endurance.")
        endurance_joueur += 50
        if endurance_joueur > endurance_max_joueur:
            endurance_joueur = endurance_max_joueur
        concentration_disponible = False
        print(f"Endurance actuelle : {endurance_joueur} / {endurance_max_joueur}")
        action_effectuee = False
    
    else:
        print()
        print("Choix invalide.")

    if action_effectuee and pv_chimere > 0:
        print()
        print("=== TOUR DE L'ENNEMI ===")
        print()
        degats_chimere = 400
        if garde_active:
            print("La garde de Kaya réduit les dégâts subis de moitié!")
            degats_chimere = degats_chimere // 2
            garde_active = False
        pv_joueur = attaquer_ennemi(pv_joueur, degats_chimere, nom_chimere, nom_joueur, pv_max_joueur)

if pv_joueur <= 100:
    print()
    print("Kaya n'a plus la force de continuer...")
    print("Elle regarde, impuissante, un genou à terre, la Chimère lever sa patte.")
    print("« C'est donc la fin, c'est aujourd'hui que ma vie s'achève... »")
    print("« Non. Pas sans combattre ! »")
    print()

    input("Appuie sur Entrée pour ramasser l'épée de Kaya...")

    print()
    print("Kaya arme son épée, prête à se battre jusqu'à la mort.")
    print()

    input("Appuie sur Entrée pour porter une ultime attaque...")

    print()
    print("En un mouvement, fulgurant, la bête désarme Kaya et envoie voler son épée au loin.")
    print("« Saleté de monstre ! »")
    print("La Chimère lève à nouveau sa patte.")
    print("Kaya ferme les yeux, comprenant que la lutte est vaine.")
    print()

    input("Appuie sur Entrée pour accepter la mort...")

    print()
    print("La Chimère abat sa patte sur Kaya afin de l'achever.")
    print("Kaya ne ressent aucune douleur, comme si l'attaque de la bête ne l'avait jamais atteinte.")
    print("La Chimère pousse un cri strident !")
    print()

    input("Appuie sur Entrée pour ouvrir les yeux...")

    print()
    print("Un homme capuché, vêtu d'un long manteau noir se tient entre Kaya et la Chimère.")
    print("La patte censée mettre fin à la vie de Kaya gît juste à côté d'elle.")
    print("« Qu'est-ce que...?! »")
    print()

    input("Appuie sur Entrée pour observer la scène...")

    print()
    print("L'homme disparaît une fraction de seconde et réapparaît aussitôt juste derrière la Chimère.")
    print("La bête se fige, mais aucune blessure apparente ne se manifeste.")
    print("Soudain, la Chimère se sépare en deux, puis s'effondre au sol, sans vie. Laissant s'élever un épais nuage de poussière.")
    print()

    pv_chimere = 0
    print()
    print(f"{nom_chimere} a été vaincue !")

    print()
    print("Sans que le nuage n'ait le temps de se dissiper, l'homme se tient à nouveau devant Kaya, une main tendue vers elle et un large sourire aux lèvres.")
    print("« Enchanté ! Je m'appelle Raiden. »")
    print()

    input("Appuie sur Entrée pour accepter la main tendue et se relever...")

    print()
    print("« De...De même ! Je suis Kaya. »")