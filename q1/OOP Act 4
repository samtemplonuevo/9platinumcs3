# advancedRelationships.py
# My OOP Seed System - Part IV: Designing Advanced Class Relationships

import gc
import weakref

# ========================================================
# PART (composition): created and owned by one Movie
# ========================================================
class PlaybackProgress:
    """Tracks how many minutes of ONE movie have been watched."""

    def __init__(self, total_minutes):
        self.total_minutes = total_minutes
        self.minutes_watched = 0

    def advance(self, minutes):
        self.minutes_watched = min(self.total_minutes, self.minutes_watched + minutes)

    def get_percent(self):
        return round(self.minutes_watched / self.total_minutes * 100)

    def is_complete(self):
        return self.minutes_watched >= self.total_minutes


# ========================================================
# PARENT class
# ========================================================
class Movie:
    """Represents a feature film within a streaming catalog or digital media library."""

    def __init__(self, title, director, duration_minutes, release_year, rating=0):
        # Public attributes
        self.title = title
        self.director = director
        self.duration_minutes = duration_minutes
        self.release_year = release_year

        # Private attributes
        self._rating = 0
        self._is_watched = False
        self._is_playing = False

        # COMPOSITION: The Movie itself creates its PlaybackProgress.
        self._progress = PlaybackProgress(duration_minutes)

        if rating != 0:
            self.set_rating(rating)

    def play(self):
        if not self._is_playing:
            self._is_playing = True
            print(f"▶ Now playing: {self.title}")

    def pause(self):
        if self._is_playing:
            self._is_playing = False
            print(f"⏸ Paused: {self.title}")
        else:
            print(f"'{self.title}' is not playing, so there is nothing to pause.")

    def mark_as_watched(self):
        self._is_watched = True
        self._is_playing = False
        print(f"✔ '{self.title}' marked as watched.")

    def set_rating(self, stars):
        if isinstance(stars, int) and 1 <= stars <= 5:
            self._rating = stars
            print(f"★ Rating for '{self.title}' set to {stars}/5.")
        else:
            print(f"✖ Invalid rating '{stars}' for '{self.title}'. Use a whole number from 1 to 5.")

    def get_rating(self):
        return self._rating

    def get_status(self):
        if self._is_playing:
            return "Playing"
        elif self._is_watched:
            return "Watched"
        return "Not watched"

    def watch_for(self, minutes):
        """Plays the movie and advances its progress. Finishes the movie if the end is reached."""
        self.play()
        self._progress.advance(minutes)
        print(f"— Watched {minutes} min of '{self.title}' ({self.get_progress_percent()}% done)")
        if self._progress.is_complete():
            self.mark_as_watched()

    def get_progress_percent(self):
        return self._progress.get_percent()

    def get_progress(self):
        """Returns the PlaybackProgress part (used to show that each movie owns its own)."""
        return self._progress

    def describe(self):
        return f"{self.title} ({self.release_year}), directed by {self.director}, ({self.duration_minutes} min)"


# ========================================================
# CHILD class: AnimatedMovie IS-A Movie
# ========================================================
class AnimatedMovie(Movie):
    """Represents an animated feature film, inheriting from Movie."""

    def __init__(self, title, director, duration_minutes, release_year, studio, rating=0):
        super().__init__(title, director, duration_minutes, release_year, rating)
        self.studio = studio

    def get_animation_info(self):
        return f"Studio Ghibli Animation: {self.studio}"

    def describe(self):
        base_desc = super().describe()
        return f"{base_desc} | Animated by {self.studio}"


# ========================================================
# AGGREGATION class: Playlist HAS-A Movie (movies exist outside the playlist)
# ========================================================
class Playlist:
    """Represents a curated collection of movies."""

    def __init__(self, name, creator):
        self.name = name
        self.creator = creator
        self._movies = [] # AGGREGATION: stores references to existing Movie objects

    def add_movie(self, movie):
        if movie not in self._movies:
            self._movies.append(movie)
            print(f"+ Added '{movie.title}' to playlist '{self.name}'.")

    def display_playlist(self):
        print(f"\n🎵 Playlist: {self.name} (Created by {self.creator})")
        if not self._movies:
            print("  (Playlist is empty)")
        for movie in self._movies:
            print(f"  - {movie.describe()} [{movie.get_status()}]")


# ========================================================
# Test run
# ========================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1 - INHERITANCE (AnimatedMovie IS-A Movie)")
    print("=" * 60)
    inception = Movie("Inception", "Christopher Nolan", 148, 2010)
    spirited = AnimatedMovie("Spirited Away", "Hayao Miyazaki", 125, 2001,
                             "Studio Ghibli", hand-drawn=True, rating=4)
    print("Inherited from Movie, used by the child:")
    print(f" spirited.title          = {spirited.title}")
    print(f" spirited.duration_minutes = {spirited.duration_minutes}")
    print(f" spirited.get_rating()   = {spirited.get_rating()}")
    print(f" spirited.get_status()   = {spirited.get_status()}")
    print("Added by the child:")
    print(f" spirited.get_animation_info() = {spirited.get_animation_info()}")
    print(f" isinstance(spirited, Movie)   = {isinstance(spirited, Movie)}")
    print("describe() on each object:")
    print(f" {inception.describe()}")
    print(f" {spirited.describe()}")

    print()
    print("=" * 60)
    print("TEST 2 - COMPOSITION (Movie owns PlaybackProgress)")
    print("=" * 60)
    inception.watch_for(74)
    inception.pause()

    print(f"Inception progress : {inception.get_progress_percent()}%")
    print(f"  ({inception.get_progress().minutes_watched}/{inception.get_progress().total_minutes} min)")
    inception.watch_for(74)
    print(f"  ({inception.get_progress().minutes_watched}/{inception.get_progress().total_minutes} min)")
    print(f"Same progress object? {inception.get_progress() is spirited.get_progress()}")

    print()
    print("Lifecycle check: delete a temporary movie")
    temp = Movie("Temp Movie", "Nobody", 90, 2020)
    part_ref = weakref.ref(temp.get_progress())
    print(f"Progress exists before delete? {part_ref() is not None}")
    del temp
    gc.collect()
    print(f"Progress exists after delete? {part_ref() is not None}")

    print()
    print("=" * 60)
    print("TEST 3 - AGGREGATION (Playlist holds existing movies)")
    print("=" * 60)
    playlist = Playlist("Weekend Watchlist", "Alex")
    playlist.add_movie(inception)
    playlist.add_movie(spirited)
    playlist.display_playlist()

    del playlist
    gc.collect()
    print("Playlist deleted. Do the movies still exist?")
    print(f"Inception.title: {inception.title} (Inception.get_progress_percent()%)")
    print(f"Spirited.title: {spirited.title} (Spirited.get_status()) / {spirited.get_progress_percent()}%")

