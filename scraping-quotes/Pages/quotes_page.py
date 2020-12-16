from bs4 import BeautifulSoup

from Locators.quotes_page_locators import QuotesPageLocators
from Parsers.quotes import QuotesParser

class QuotesPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        locator = QuotesPageLocators.QUOTE
        quotes_tag = self.soup.select(locator)
        return [QuotesParser(e) for e in quotes_tag]