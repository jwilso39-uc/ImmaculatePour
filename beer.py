"""
Docstring for beer

Functions for looking up beer on Untappd (using scraping tools) given search term
"""
class Beer:

    def __init__(self, html) -> None:
        pass

    """
    Finds beer given search term by first opening the right serach page, then picking the first
    option.

    Params: search - search term to look up

    Returns: First result of search term's Untappd page html
    """
    @classmethod
    def find_beer(cls, search):
        pass

    """
    Given beer HTML page, determine if it matches a requirements of the grid

    Params: beer - Beer object given by find_beer
            req - Requirement object to compare beer to.

    Returns: True if the Beer Object passes the requirment, False if not
    """
    def compare_beer(self, req):
        pass