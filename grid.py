from beer import Beer
from requirement import Requirement
"""
Docstring for grid

Describes an instance of the game, with three columns and three rows.
"""

class Grid:
    """
    Represents one instance of the grid
    """
    def __init__(self) -> None:
        self.size = 3
        self.lives = self.size ** 2
        self.grid = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.cols = []
        exclude = set()
        dups = set()
        for i in range(self.size):
            req = Requirement(dups=dups)
            self.cols.append(req)
            exclude = exclude.union(req.get_excluded_set())
            dups.add((req.type, req.req))
        self.rows = []
        dups = set()
        for i in range(self.size):
            #need each row to consider what columns it's intersecting with
            req = Requirement(exclude=exclude, dups=dups)
            self.rows.append(req)
            dups.add((req.type, req.req))
    
    """
    Given an assumed empty coordinate on the grid and a beer, return whether that beer can fit into that square
    """
    def check_square(self, x: int, y: int, beer: Beer) -> bool:
        col = self.cols[x]
        row = self.rows[y]
        if (col.compare_beer(beer) and row.compare_beer(beer)):
            return True
        else:
            return False
        
    """
    Given a valid beer for a given coordinate, add that beer to the grid
    """
    def add_beer(self, x: int, y: int, beer: Beer) -> None:
        self.grid[y][x] = beer

    """
    Removes a guess from the grid and returns True if user is out of guesses
    """
    def remove_life(self) -> bool:
        self.lives -= 1
        if self.lives == 0:
            return True
        else:
            return False
