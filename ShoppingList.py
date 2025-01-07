print('\n Liste des Options de la liste\n1- Ajouter un produit\n2- Supprimer un produit\n3- Afficher le panier \n')
Shop=True
Storage=['bannane','pomme','poire','raisin','kiwi','mangue','pastèque','Pepsi','Double7','Red bull','Pressea','mais','mil','blé','riz','avoine','sorgho','Viande rouge','Chaire_blanche','Poissons','fruit de mer']

shoppingList=[]
while Shop==True:
   choix=int(input('Veuillez choisir  parmis les opitons ci-dessus :'))

   if choix==1:
       if len(shoppingList) < 20:
        produit=input('Entrer le nom du produit à ajouter :')
        if produit in Storage:
            shoppingList.append(produit)
            print('Le produit a été ajouté avec succès !')
        else : 
           print('Le produit est en rupture d stock')    
       else :
          print('Vous avez atteint le maximum de produits!')
       
   elif choix==2:
       produit=input('Entrer le nom du produit à supprimer : \n')
       if produit in shoppingList:
          shoppingList.remove(produit)
          print("le produit a été  bien supprimé du  panier !")
       else:
          print("le produit demandé n'est pas dans le panier !")

   elif choix==3:
     print('La liste des produit du panier :')
     for i in shoppingList :
        print (i)         

  
   print('Voulez-vous poursuivre vos courses ? \n Repondre par Y ou N ')
   reponse=input('Entrer votre reponse ')
   if reponse=='N':
      print('Au revoir , à la prochaine')
      Shop=False
  