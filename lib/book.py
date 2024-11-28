class Book:
    def __init__(self, title, page_count, year_published=None, price=None):
        self.title = title
        self.page_count = page_count
        self.year_published = year_published
        self.price = price
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and value:
            self._title = value
        else:
            raise ValueError("Title must be a non-empty string.")

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")  

    @property
    def year_published(self):
        return self._year_published

    @year_published.setter
    def year_published(self, value):
        if value is None or isinstance(value, int):
            self._year_published = value
        else:
            raise ValueError("Year published must be an integer.")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value is None or isinstance(value, (int, float)):
            self._price = value
        else:
            raise ValueError("Price must be a number.")
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
