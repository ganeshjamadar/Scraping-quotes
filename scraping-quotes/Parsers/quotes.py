from Locators.quotes_locators import QuotesLocators

class QuotesParser:
    """
    Given one of the specific quote divs, Find out the data about
    the quote (quote content, author, tags).
    """

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Quote {self.content}, by {self.author}>'

    @property
    def content(self):
        locator = QuotesLocators.CONTENT
        return self.parent.select_one(locator).string

    @property
    def author(self):
        locator = QuotesLocators.AUTHOR
        return self.parent.select_one(locator).string
    
    @property
    def tags(self):
        locator = QuotesLocators.TAGS
        return [e.string for e in self.parent.select(locator)]
