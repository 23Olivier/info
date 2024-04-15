# symbole,Or,And,Not,logique,SOPform,POSform
from itertools import product
# but 1 de fatarian lo raha inclu ao ny not and sy or:apesaina ny  f° eval
  
    # 1 definissiavan lo  le  function iverifiena anle fonction ligique
expression = (input("entrez l'expression logique (utilisant 'and','or','not') : " ))

noms_var = []


# sotatanle utilisateur eto le fonction logique 
def convertion_en_operations(expression):
     expression = expression.subs("and", " & ").replace("or", " | ").replace("not", " not ")
     return expression 



# # Convertir les opérations logiques
expression = convertion_en_operations(expression)


# print(expression)
fonction_logique = expression
def syntaxe(noms_var):
    return eval(expression)
# input le variable izay tinle olona (isa ilay izy)

# eto le variable a,b,c,sns atsofika aminy f° append
# boucle for no napesaina (for ao ny initiation ,)
n = int(input("Entrez le nombre de variables : "))

for i in range(n):
    nom = input(f"entrez le nom de la variable {i+1}: ")
    noms_var.append(nom)
# titre anle table fotsiny 
tete = noms_var + ["fonction"]
print('table de verite à n varianle')

print('\t'.join(tete))

# table_verite

interval = list(product([0, 1], repeat=n))

# for nom in interval
 
for nom in interval:
      print("\t".join(str(val) for val in nom) + (int(fonction_logique)))








































