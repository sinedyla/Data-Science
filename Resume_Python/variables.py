# ********************** TYPES NUMÉRIQUES ********************** #

# Entiers
a = 5 # exemple d'entier (1)
print(a) # ...
print(type(a)) # <class 'int'>
print('') # Remarque : en Python, tout est un objet


# Nombres à virgule flottante
x = 33.5 # exemple de nombre à virgule flottante (2)
print(x) # ...
print(type(x)) # <class 'float'>
print('') # ...

# Types complexes
c = 4 + 5j # exemple de nombre complexe (3)
print(c) # ...
print(type(c)) # <class 'complex'>
print('') # ...

# Valeurs binaires/hexadécimales
b = 0b01010 # exemple d'entier binaire (4)
h = 0xf # exemple d'entier hexadécimal (5)
print(b) # ...
print(h) # ...
print(type(b)) # <class 'int'>
print(type(h)) # <class 'int'>
print('') # ...

# Types booléens
g = True # exemple de type booléen (6)
print(g) # ...
print(type(g)) # <class 'bool'>
print(9 > 8) # condition vraie
print(9 < 8) # condition fausse
print('') # ...


#  Opérateurs mathématiques

print(int('42')) # exemple de conversion (1)
print(float('42')) # exemple de conversion (2)
print(bin(42)) # exemple de conversion (3)
print(hex(42)) # exemple de conversion (4)
print(oct(42)) # exemple de conversion (5)

print("Addition :\t", 3 + 4) # exemple d'addition
print("Soustraction :\t", 4 - 3) # exemple de soustraction
print("Multiplication :\t", 6 * 5) # exemple de multiplication
print("Division :\t", 12 / 5) # exemple de division
print("Division entière :\t", 18 // 4) # exemple de division entière (sans reste)
print("Modulo :\t", 8 % 5) # exemple de reste de la division
print("Puissance :\t", 5 ** 3) # exemple de puissance

print(8 + 2 * 10) # exemple de priorité des opérations (1. sans parenthèses)
print(8 + (2 * 10)) # exemple de priorité des opérations (2. avec parenthèses)

a, b = 10, 5

a += b # opérateur d'affectation (1)
print(a) # ...
a *= b # opérateur d'affectation (2)
print(a) # ...

print(a == 75 and b == 5) # opérateur logique (1)
print(a == 10 and b == 5) # opérateur logique (2)
print(a == 10 and b == 5) # opérateur logique (3)
print(not(a == 10 and b == 5)) # opérateur logique (4)

print(a == 75 or b == 5) # opérateur logique (5)


# CHAÎNES DE CARACTÈRES

print("Hello Word!")                            # exemple (1)  
print('Hello Word!')                            # exemple (2)  

print("I don't think")                          # gestion de l'apostrophe (1)  
print('He said :" Look at the sky!"...')       # gestion de l'apostrophe (2)  
print('I don\'t think')                         # gestion de l'apostrophe (3)  
print(r'/home/Captain/example')                 # gestion de l'apostrophe (4)  

print('Hi' + str(5))                            # conversion en chaîne  

firstName = 'Captain'                           # utilisation d'une variable (1)  
print(firstName)                                # ...  
print(firstName + 'Mich')                       # ...  
print(firstName * 5)                            # multiplication d'une chaîne (répétition)  

string = """This  
is a multiple  
line string declaration  
"""                                             # utilisation d'une variable (2)  
print(string)                                   # ...  


# TRAVAILLER AVEC LES CHAÎNES

user = 'Tuna is the best'

print(user[0])                          # accès à une lettre précise d'une chaîne  
print(user[1])                          # ...  
print(user[2])                          # ...  
print(user[3])                          # ...  
print('')

print(user[-1])                         # accès depuis la fin  
print(user[-2])                         # ...  
print(user[-3])                         # ...  
print(user[-4])                         # ...  
print('')

print(user[1:3])                        # découpage (slice) d'une chaîne [de l'indice 1 à 3 non inclus]  
print(user[:3])                         # découpage du début à l'indice 3 (non inclus)  
print(user[1:])                         # découpage de l'indice 1 jusqu'à la fin  
print(user[:])                          # toute la chaîne  
print(user[-3:-1])                      # découpage en indices négatifs  
print(user[0:4:3])                      # découpage avec un pas défini (ici 3)  
print(user[::-1])                       # inverser la chaîne  
print('')

print(len(user))                        # longueur de la chaîne  
print(len('Tuna'))                      # (Remarque : l'espace compte comme un caractère)  
print(user.count('e'))                 # compter le nombre d'occurrences d'une sous-chaîne  

print(user.find('un'))                  # trouver la position d'une sous-chaîne ;  
                                        # renvoie l'indice si trouvé  
print(user.find('u', 0, len(user)))    # chercher avec des limites  
print(user.replace('una', 'omb'))      # remplacer 'una' par 'omb' dans la chaîne  

print(user)                            # la chaîne originale n'est pas modifiée  

print(user.upper())                    # conversion en majuscules  
print(user.lower())                    # conversion en minuscules  
print(user.title())                    # conversion en majuscule au début de chaque mot  

print(user.isalpha())                  # retourne True si tous les caractères sont alphabétiques  
                                     # et qu'il y a au moins un caractère, sinon False  

line = '  aaa,bbb,cccccc,dd  \n'       # exemple  

print(line.split(','))                 # découpage selon un délimiteur en liste de sous-chaînes  
print(line.strip())                    # suppression des espaces en début et fin  
print(line.rstrip())                   # suppression des espaces à droite  
print(line.lstrip().split())           # combinaison de deux opérations  

print('%s, eggs, and %s' % ('spam', 'SPAM!'))           # formatage avec %  
print('{}, eggs, and {}'.format('spam', 'SPAM!'))       # formatage avec la méthode format  


# RECHERCHE DE MOTIFS (PATTERN MATCHING)


import re

str_example = 'Hello    Python world'                        # recherche d'une sous-chaîne qui commence par  
                                                             # "Hello" suivi de zéro ou plusieurs tabulations ou espaces  
match = re.match('Hello[\t]*(.*)world', str_example)         # "Hello" suivi de zéro ou plusieurs tabulations  
print(match.group(1))                                        # puis capture tout caractère arbitraire (groupe 1)  

pattern = '/usr/home/testuser'                               # autre exemple avec extraction de trois groupes  
match = re.match('[/:](.*)[/:](.*)[/:](.*)', pattern)        # séparés par des slashs ou deux-points  
print(match.groups())                                        # affichage des groupes capturés  

match = re.split('[/:]', pattern)                            # ici split retourne le même résultat  
print(match)                                                 # que l'exemple précédent  

# Liste

vide = []                                      # liste vide
print(vide)                                    # ...
joueurs = [70,5,9]                              # syntaxe d'une liste
print(joueurs)                                  # print entire list

differents = [10,20, "Newton", 30.5, True]       # definie differents types d'éléments
print(differents)  