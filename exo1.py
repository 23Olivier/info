from itertools import product

expression = bool(input("entrez l'expression logique (utilisant 'and','or','not') : " ))

noms_var = []

def syntaxe(noms_var):
    return eval(expression)
 
def nbr():
    n_imp = 0   
    while n_imp <=1 :
        n_entre = int(input( "entre les nombres de variable "))
        try:
            n_imp = int(n_entre)  
        except:
            print(" nombre sup à 2")

    return n_imp  

n_imp = nbr()   
# n = int(input("Entrez le nombre de variables : "))
interval = list(product([0, 1], repeat=n_imp))

for i in range(n_imp):
    nom = input(f"entrez le nom de la variable {i+1}: ")
    noms_var.append(nom)
tete = noms_var + ["fonction"]
print('table de verite à n varianle')

print('\t'.join(tete))


I = [0,1]
boolenne = str(expression)

name = str(nom)
for nom in interval:
      print("\t".join(str(val) for val in nom) , "\t".join(boolenne))

def premier_forme_canonique():
   forme_canonique_1ère = "[a * b * c] + [non(a) * non(c)]"
   return  forme_canonique_1ère 
print("\n\npremier_forme_canonique\t:\n==>",premier_forme_canonique())

def deuxieme_forme_canonique():
   forme_canonique_2éme = "[a + b + c] * [non(a) + non(b) + non(c)]"
   return  forme_canonique_2éme 
print("\n\ndeuxieme_forme_canonique:\n==>",deuxieme_forme_canonique())      
