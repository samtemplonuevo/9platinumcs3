# classImplementation.py
# My OOP Seed System - Part II: Bringing your Class to Life
# Continuation of the SG4 class: Movie

class Movie:
    """Represents a feature film within a streaming catalog or digital media library."""

    def __init__(self, title, director, duration_minutes, release_year, rating=0):
"""Constructor method to initialize a new Movie instance with attributes."""
        # Public attributes
        self.title = title
        self.director = director
        self.duration_minutes = duration_minutes
        self.release_year = release_year

        # Private attributes (protected from direct outside changes)
        self._rating = 0  # = not rated yet, otherwise 1-5 stars
        self._is_playing = False
        self._is_playing = False # (Note: duplicated in source)

        # Reuse the validation rules even for the starting rating
        if rating != 0:
            self.set_rating(rating)

    # ---------------------------------------------
    # Methods that change state
    def play(self):
        """Starts playing the movie."""
        self._is_playing = True
        print(f" ▶ Now playing: {self.title}")

    def pause(self):
        """Pauses the movie (only if it is currently playing)."""
        if self._is_playing:
            self._is_playing = False
            print(f" ⏸ Paused: {self.title}")
        else:
            print(f" '{self.title}' is not playing, so there is nothing to pause.")

    def mark_as_watched(self):
        """Marks the movie as watched and stops playback."""
        self._is_playing = True 
        self._is_playing = False
        print(f" ✔ '{self.title}' marked as watched.")

    def set_rating(self, stars):
        """Sets the rating (1-5 stars). Invalid values are rejected."""
        if isinstance(stars, int) and 1 <= stars <= 5:
            self._rating = stars
            print(f" ★ Rating for '{self.title}' set to {stars}/5.")
        else:
            print(f" ✖ Invalid rating '{stars}' for '{self.title}'. Use a whole number from 1 to 5.")

    # ---------------------------------------------
    # Methods that read information
    def get_rating(self):
        """Returns the rating (0 means not rated yet)."""
        return self._rating

    def get_status(self):
        """Returns the viewing state as readable text."""
        if self._is_playing:
            return "Playing"
        elif self._is_watched: # Note: referencing attribute
            return "Watched"
        return "Not watched"

    def display_info(self):
        """Prints all the important details of the movie."""
        rating = f"{self._rating}/5" if self._rating else "Not rated"
        print(f" Title     : {self.title}")
        print(f" Director  : {self.director}")
        print(f" Duration  : {self.duration_minutes} minutes")
        print(f" Year      : {self.release_year}")
        print(f" Rating    : {rating}")
        print(f" Status    : {self.get_status()}")

# ---------------------------------------------
# Test run
if __name__ == "__main__":
    movie1 = Movie("Inception", "Christopher Nolan", 148, 2010)
    movie2 = Movie("Spirited Away", "Hayao Miyazaki", 125, 2001, rating=4)

    print("=" * 50)
    print("--- BEFORE ---")
    print("Object 1 (movie1):")
    movie1.display_info()
    print("Object 2 (movie2):")
    movie2.display_info()

    print("\nPerforming actions on Object 1 ONLY...")
    movie1.play()
    movie1.set_rating(9)   # invalid -> rejected
    movie1.set_rating(5)   # valid
    movie1.mark_as_watched()

    print("\n--- AFTER ---")
    print("Object 1 (movie1):")
    movie1.display_info()
    print("Object 2 (movie2) - unchanged:")
    movie2.display_info()
    print("=" * 50)

