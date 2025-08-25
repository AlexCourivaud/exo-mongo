Exercice test mongoDB - IASchool needemand 2025.

- Création du container :
  docker-compose up -d

- création du venv :
  python -m venv venv

- activation du venv (sous windows!):
  venv\Scripts\Activate

- lancement du container mongo :
  docker exec -it mongo_container mongosh -u root -p example

- test de l'app avec exemple Inception :
  python app.py
