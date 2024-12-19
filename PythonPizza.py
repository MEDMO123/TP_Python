print('Bienvenue chez Python Pizza Livraisons')
#Recuperation des details de la commande : taille,surplus peperoni et fromage
size=input('Veuillez choisir la taille de votre pizza :\n P:Petit model\n M:Moyen\n G:Grand modele :\n')
peperoni_add=input('Souhaitez vous rajouter du peperoni sur votre Pizza  ? (Repondre par Y ou N ):\n')
fromage_add=input('Souhaitez vous rajouter du fromage sur votre Pizza ? (Repondre par Y ou N :\n')
#initialisation des couts
if size=='P' :
   Total=15
elif size=='M':
   Total=20
elif size=='G':
   Total=25
#Calcul peperoni
if peperoni_add=='Y':
   if size=='P':
      Total+=2
   else:
      Total+=3

#Calcul fromage
if fromage_add=='Y':
   Total+=1
   
print(f"Le cout totale de la commande est :{Total}$")
 