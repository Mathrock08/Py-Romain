# Création de la définition gérant la conversion
def Conversion():

    # Définit le nombre à convertir
    NombreArabe = int(input("Choisissez un nombre (écrit sous forme arabe)"))

    # Tableau où sont rentrer les différents nombres clés sous forme arabe et romaine
    tab = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
        [ 100, 'C'], [ 90, 'XC'], [ 50, 'L'], [ 40, 'XL'],
        [  10, 'X'], [  9, 'IX'], [  5, 'V'], [  4, 'IV'],
        [   1, 'I']]

    # Création des variables
    NombreRomain = ""
    Cpt = 0

    # Boucle qui permet de convertir
    while NombreArabe > 0:
        while tab[Cpt][0] > NombreArabe:
            Cpt = Cpt + 1

        NombreRomain = NombreRomain + tab[Cpt][1]
        NombreArabe = NombreArabe - tab[Cpt][0]

    # On affiche le résultat final en nombre romain
    print(NombreRomain)

# On appelle la définition
Conversion()