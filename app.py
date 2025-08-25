from dao.movie_dao import MovieDAO

def main():
    dao = MovieDAO()

    # 1. Création
    movie_id = dao.create_movie({"title": "Inception", "year": 2010})
    print("Film inséré avec ID:", movie_id)

    # 2. Récupération
    movie = dao.get_movie(movie_id)
    print("Récupéré:", movie)

    # 3. Liste
    movies = dao.list_movies()
    print("Tous les films:", movies)

    # 4. Mise à jour
    updated = dao.update_movie(movie_id, {"year": 2012})
    print("Mis à jour ?", updated)

    # 5. Suppression
    deleted = dao.delete_movie(movie_id)
    print("Supprimé ?", deleted)

if __name__ == "__main__":
    main()
