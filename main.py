from flask import Flask, request, render_template, session
from grid import Grid
from beer import Beer

app = Flask(__name__)
app.secret_key="PUTTHISSOMEWHERESAFELATER"

"""
Main page to play game
"""
@app.route("/", methods = ['POST', 'GET']) # type: ignore
def main():
    #create new grid
    if 'grid' not in session:
        grid = Grid()
        session['grid'] = grid.serialize()
    else:
        grid = Grid(session = session['grid'])
    #check answer and potentially update grid
    if request.method == "POST":

        beer = request.form.get('beer_name')
        row_idx = int(request.form.get('row'))
        col_idx = int(request.form.get('col'))

        print(f"Guess for {grid.rows[row_idx]} x {grid.cols[col_idx]}: {beer}")

        return render_template('grid.html', cols=grid.cols, rows=grid.rows)

    return render_template('grid.html', cols = grid.cols, rows = grid.rows)


if __name__ == "__main__":
    app.run(debug=True)