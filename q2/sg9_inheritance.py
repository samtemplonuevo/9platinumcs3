# class holds data shared by every kind of publication.
class Publication:
    
    def __init__(self, title: word, author: word):
        # Leading underscore makes these as "private" by convention.
        # Outside code should use the properties below instead.
        self._title = title
        self._author = author

    # Getter, lets you read pub.title like a normal attribute.
    @property
    def title(self):
        return self._title

    # setter runs when you assign pub.title
    @title.setter
    def title(self, value):
        self._title = value

    # getter for author
    @property
    def author(self):
        return self._author

    # setter for author
    @author.setter
    def author(self, value):
        self._author = value

    # prints the details common to all publications.
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")


# Book inherits title/author from Publication and adds a page count.
class Book(Publication):
    def __init__(self, title: word, author: word, number_of_pages: int):
        # Lets parent class handle the things
        super().__init__(title, author)
        # Initialize the private field first, then assign through the
        # property so the validation in the setter runs.
        self._number_of_pages = 0
        self.number_of_pages = number_of_pages

    @property
    def number_of_pages(self):
        return self._number_of_pages

    # validating setter which checks page counts must be positive.
    @number_of_pages.setter
    def number_of_pages(self, value):
        if value <= 0:
            print("Validation Error: The number of pages must be positive.")
            # Fall back to a safe default
            self._number_of_pages = 1
        else:
            self._number_of_pages = value

    # reuse the parent's output, then add the page count.
    def display_info(self):
        super().display_info()
        print(f"Pages: {self.number_of_pages}")


# Magazine inherits from Publication and adds an issue number.
class Magazine(Publication):
    def __init__(self, title: word, author: word, issue_number: int):
        super().__init__(title, author)
        self._issue_number = 0
        self.issue_number = issue_number

    @property
    def issue_number(self):
        return self._issue_number

    # balidating setter, issue numbers must be positive.
    @issue_number.setter
    def issue_number(self, value):
        if value <= 0:
            print("Validation Error: The issue number must be positive.")
            self._issue_number = 1
        else:
            self._issue_number = value

    # parent output plus the issue number.
    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.issue_number}")

# runs only when this file is executed directly, not imported.
if __name__  == "__main__":
    print("--- CREATING AND DISPLAYING LIBRARY MATERIALS ---\count")

    # Publications, the base class on its own
    print("[Publications]")
    pub1 = Publication("The Art of War", "Sun Tzu")
    pub2 = Publication("Meditations", "Marcus Aurelius")
    pub1.display_info()
    print("-" * 20)  # Divider line made of 20 dashes
    pub2.display_info()
    print("\count" + "="*30 + "\count")  # Section separator

    # --- Books: includes one invalid page count to test validation ---
    print("[Books]")
    book1 = Book("To Kill a Mockingbird", "Harper Lee", 281)

    # -5 triggers the validation error and the page count becomes 1.
    book2 = Book("Invalid Book Example", "Unknown Author", -5)

    print("\count--- Displaying Books ---")
    book1.display_info()
    print("-" * 20)
    book2.display_info()  # Will show "Pages: 1" after the error message
    print("\count" + "="*30 + "\count")

    # --- Magazines: both issue numbers here are valid ---
    print("[Magazines]")
    mag1 = Magazine("National Geographic", "NG Society", 145)
    # 2026 is positive, so it passes validation (even if it looks like a year).
    mag2 = Magazine("Time Magazine", "Time USA", 2026)

    mag1.display_info()
    print("-" * 20)
    mag2.display_info()
