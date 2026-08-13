nom_joueur = "Kaya"
pv_joueur = 1200
pv_max_joueur = 1500
endurance_joueur = 300
endurance_max_joueur = 500

garde_active = False

concentration_disponible = True

nom_ennemi = "Créature des Ruines"
pv_ennemi = 800
pv_max_ennemi = 800

def attaquer(pv_ennemi, degats):
    print(f"{nom_joueur} attaque {nom_ennemi} !")
    print(f"{nom_joueur} inflige {degats} points de dégâts à {nom_ennemi}.")
    pv_ennemi -= degats
    if pv_ennemi < 0:
        pv_ennemi = 0
    print(f"{nom_ennemi} : {pv_ennemi} / {pv_max_ennemi} PV")
    return pv_ennemi

def attaquer_ennemi(pv_joueur, degats):
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

input("Appuie sur Entrée pour commencer l'aventure...")

input("Appuie sur Entrée pour que Kaya ouvre les yeux...")

print()
print("Kaya se redresse lentement.")
print()

while True:
    print()
    print("Que veux-tu faire ?")
    print("1 - Observer les environs")
    print("2 - Avancer dans les ruines")
    print("3 - Vérifier l'état de Kaya")
    if concentration_disponible:
        print("4 - Se Concentrer")

    choix = input("Ton choix : ")
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
print("Soudain, un bruit résonne derrière elle...")

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
        print("3 - Se Concentrer")

    choix_combat = input("Ton choix : ")
    if choix_combat == "1":
        pv_ennemi = attaquer(pv_ennemi, 200)
        action_effectuee = True

    elif choix_combat == "2":
        print()
        print("=== COMPÉTENCES DE KAYA ===")
        print("1 - Frappe Lourde")
        print("2 - Garde Défensive")
        print("3 - Retour")

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
                print(f"{nom_ennemi} : {pv_ennemi} / {pv_max_ennemi} PV")
                print(f"Endurance actuelle : {endurance_joueur} / {endurance_max_joueur}")
                action_effectuee = True
            else:
                print()
                print("Pas assez d'endurance pour utiliser Frappe Lourde.")

        elif choix_competence == "2":
            if endurance_joueur >= 50:
                print()
                print("Kaya utilise Garde Défensive !")
                garde_active = True
                endurance_joueur -= 50
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
        action_effectuee = True

    else:
        print()
        print("Choix invalide.")

    if pv_ennemi <= 0:
        print()
        print(f"{nom_ennemi} a été vaincu !")
    if pv_joueur <= 0:
        print()
        print(f"{nom_joueur} a été vaincu !")

    if action_effectuee and pv_ennemi > 0:
        print()
        print("=== TOUR DE L'ENNEMI ===")
        degats_ennemi = 150
        if garde_active:
            print("La garde de Kaya réduit les dégâts subis de moitié!")
            degats_ennemi = degats_ennemi // 2
            garde_active = False
        pv_joueur = attaquer_ennemi(pv_joueur, degats_ennemi)
        