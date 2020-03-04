# Installation
```
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

# Développement

## Done
* Modèles : 
    * User
    * Publication
    * Tags
    * Tournoi
    * Vote
    * Tags

* API : 
    * GET/POST/PUT/PATCH/DELETE User
    * POST/DELETE Vote
    * DETAIL/POST Publication
    * Comparer 2 publications sur les votes des dernières 24h (comme dans un tournoi)
    * Récupérer les publications les plus populaires des 7 derniers jours (modulable)
    
## To do

* Tags liés aux publications (POST Tags / GET publications par tags)