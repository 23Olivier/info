from itertools import product
variables = []

def print_karnaugh(variables, values):
    # Affiche la table de Karnaugh à partir des variables et de leurs valeurs
    entrez = input('entrez votre variable')
    entrez.append(variables)
    num_variables = len(variables)
    num_rows = 2 ** num_variables
    karnaugh_map = [[' ' for _ in range(2**(num_variables-1))]
    
for nums_rows in range(2**(num_variables-1))]:
    # Remplit la table de Karnaugh avec les valeurs fournies
   for i, value in enumerate(values):
        row = i // (2**(num_variables-1))
        col = i % (2**(num_variables-1))
        karnaugh_map[row][col] = str(int(value))

    # Affiche la table de Karnaugh
    print("Table de Karnaugh :")
    print(" "*(num_variables//2 + 1), end='')
        for i in range(2**(num_variables-1)):
          print(variables[num_variables-1] + str(i), end=' ')
         print()
            for i, row in enumerate(karnaugh_map):
             print(variables[0] + str(i), end=' '*((num_variables//2)*2 + 1))
            print(' | '.join(row))

# Demande à l'utilisateur de saisir les noms des variables
num_variables = int(input("Entrez le nombre de variables : "))
variables = [input(f"Entrez le nom de la variable {i+1} : ") for i in range(num_variables)]

# Demande à l'utilisateur de saisir les valeurs pour chaque cellule de la table de Karnaugh
values = [input(f"Entrez la valeur de la cellule {i+1} (True/False) : ") for i in range(2**(num_variables))]

# Affiche la table de Karnaugh
print_karnaugh(variables, values)