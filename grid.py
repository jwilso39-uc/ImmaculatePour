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
        self.grid = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.cols = []
        exclude = set()
        for i in range(self.size):
            req = Requirement()
            self.cols.append(req)
            exclude = exclude + req.get_excluded_set()
        self.rows = []
        for i in range(self.size):
            #need each row to consider what columns it's intersecting with
            req = Requirement(exclude)
            self.rows.append(req)
    
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
