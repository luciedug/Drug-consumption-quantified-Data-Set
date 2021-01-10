# Drug-consumption-quantified-Data-Set

Source : https://archive.ics.uci.edu/ml/datasets/Drug+consumption+%28quantified%29

Le dataset est le résultat d'un sondage concernant le consommation de drogue. 1885 personnes ont participées et répondu à des questions concernant l'utilisation de 18 drogues différentes et la mesure de 12 autres indicateurs. Dans le dataset de départ, les indicateurs sont codés par des nombres.
Voici les différents éléments qui composent le dataset :

  - Informations générales sur la personne interrogée ('ID', 'Age', 'Gender', 'Education', 'Country', 
     'Ethnicity')    
  - Information neurologiques sur la personne correspondant au « Five Factor Model of personality », cinq domaines qui définisse une personnalité
 ( 'Nscore','Escore', 'Oscore', 'Ascore', 'Cscore', 'Impulsive','SS')   
  - Liste de drogues et information sur leur consommation ou non ('Alcohol', 'Amphet', 'Amyl', 'Benzos', 'Caff', 
     'Canabis', 'Choc', 'Coke', 'Crack', 'Ecstasy', 'Heroin', 'Ketamin', 'Legalh', 'LSD', 'Meth',
     'Mushrooms', 'Nicotine', 'Semer', 'VSA')
     
L'objectif de ce notebook est le suivant : Prévoir  si un individu consommera ou pas une drogue en fonction de ses caractéristiques psychologiques mais aussi de ses autres consommations grâce à différents modèles de Machine Learning.
     
Le projet se décompose en plusieurs parties :   
  1. Exploration du dataset : exploration des variables, recherche de corrélation
  2. Machine Learning : Test de différents modèles (SVC, Naive Bayes, K nearest neighbors, random forest) sur plusieurs variables pour prédire la consommation ou non d'une drogue.   
  3. API Flask : API qui permet de faire les prédictions
