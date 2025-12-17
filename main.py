from flask import Flask, request, render_template, session
from grid import Grid
from beer import Beer
app = Flask(__name__)

"""
Main page to play game
"""
@app.route("/") # type: ignore
def main():
    grid = Grid()
    return render_template('grid.html', cols = grid.cols, rows = grid.rows)

if __name__ == "__main__":
    app.run(debug=True)