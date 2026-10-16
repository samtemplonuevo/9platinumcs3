# OOP Relationships.py
# My OOP Seed System - Part III: Connecting your Objects
# Existing class: Movie | New related class: Playlist
# Association: Playlist contains Movie (1 : 0..*)

class Movie:
    """Represents a feature film within a streaming catalog or digital media library."""
    
    def __init__(self, title, director, duration_minutes, release_year, rating=0):
        # Public attributes
        self.title = title
        self.director = director
        self.duration_minutes = duration_minutes
        self.release_year = release_year
        
        # Private attributes
        self.__rating = 0
        self.__is_watched = False
        self.__is_playing = False
        
        if rating != 0:
            self.set_rating(rating)

    def play(self):
        self.__is_playing = True
        print(f"▶ Now playing: {self.title}")

    def pause(self):
        if self.__is_playing:
            self.__is_playing = False
            print(f"⏸ Paused: {self.title}")
        else:
            print(f"'{self.title}' is not playing, so there is nothing to pause.")

    def mark_as_watched(self):
        self.__is_watched = True
        self.__is_playing = False
        print(f"✔ '{self.title}' marked as watched.")

    def set_rating(self, stars):
        if isinstance(stars, int) and 1 <= stars <= 5:
            self.__rating = stars
            print(f"★ Rating for '{self.title}' set to {stars}/5.")
        else:
            print(f"❌ Invalid rating '{stars}' for '{self.title}'. Use a whole number from 1 to 5.")

    def get_rating(self):
        return self.__rating

    def get_status(self):
        if self.__is_playing:
            return "Playing"
        if self.__is_watched:
            return "Watched"
        return "Not watched"


class Playlist:
    """A collection of movies that one person has put together to watch."""
    
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.__movies = []      # List of actual Movie objects (not titles)

    def add_movie(self, movie):
        """Adds a Movie object to the playlist (no duplicates)."""
        if not isinstance(movie, Movie):
            print("❌ Only Movie objects can be added to a playlist.")
        elif movie in self.__movies:
            print(f"'{movie.title}' is already in '{self.name}'.")
        else:
            self.__movies.append(movie)
            print(f"➕ Added '{movie.title}' to '{self.name}'.")

    def get_movies(self):
        """Returns the list of Movie objects stored in the playlist."""
        return self.__movies

    def get_total_duration(self):
        """Adds up the duration of every movie, using each Movie object's own data."""
        return sum(movie.duration_minutes for movie in self.__movies)

    def count_watched(self):
        """Counts how many movies in the playlist have been watched."""
        return sum(1 for movie in self.__movies if movie.get_status() == "Watched")

    def display_playlist(self):
        print(f" Playlist: {self.name} (by {self.owner})")
        print(f" 🎬 Movies : {len(self.__movies)} | Total: {self.get_total_duration()} min")
        print(f" │ Watched: {self.count_watched()}")
        for movie in self.__movies:
            rating = f"{movie.get_rating()}/5" if movie.get_rating() else "Not rated"
            print(f" └─ (movie.title} ({movie.release_year}) | {movie.duration_minutes} min")
            print(f"    │ [rating] | (movie.get_status())")


# --- Test run ---
if __name__ == "__main__":
    print("=" * 56)
    print("--- BEFORE RELATIONSHIP ---")
    playlist = Playlist("Weekend Watchlist", "Alex")
    movie1 = Movie("Inception", "Christopher Nolan", 148, 2010)
    movie2 = Movie("Spirited Away", "Hayao Miyazaki", 125, 2001)
    movie3 = Movie("Parasite", "Bong Joon-ho", 132, 2019)
    print("Objects created: 1 Playlist and 3 Movies.")
    print(f"Movies in playlist: {len(playlist.get_movies())}")

    print("\n--- BUILDING RELATIONSHIP ---")
    playlist.add_movie(movie1)
    playlist.add_movie(movie2)
    playlist.add_movie(movie3)
    playlist.add_movie(movie2)  # duplicate -> ignored

    print("\n--- AFTER RELATIONSHIP ---")
    playlist.display_playlist()

    print("\nAccessing data through the relationship:")
    for item in playlist.get_movies():
        print(f" {type(item).__name__}: {item.title} directed by {item.director}")
    print(f"First movie in playlist is {playlist.get_movies()[0] is movie1}")

    print("\nChanging movie directly (not through the playlist)...")
    movie1.set_rating(5)
    movie1.mark_as_watched()
    print("\nPlaylist NOW shows the update:")
    playlist.display_playlist()
    print("=" * 56)
