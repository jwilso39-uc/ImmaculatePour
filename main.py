from flask import Flask, request, render_template, session, jsonify
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
        data = request.get_json()

        beer_str = data.get('beer_name')
        if beer_str is not None:
            beer = Beer(soup = Beer.find_beer(beer_str))

        if beer is not None:
            row_idx = int(data.get('row'))
            col_idx = int(data.get('col'))

            is_correct = False
            if grid.check_square(col_idx, row_idx, beer):
                print(f"Guess for {grid.rows[row_idx]} x {grid.cols[col_idx]}: {beer} is CORRECT!")
                grid.grid[row_idx][col_idx] = beer
                is_correct = True
            else:
                print(f"Guess for {grid.rows[row_idx]} x {grid.cols[col_idx]}: {beer} is INCORRECT!")

            return jsonify({
                "is_correct": is_correct,
                "row": row_idx,
                "col": col_idx,
                "beer": beer.serialize()
            })

    return render_template('grid.html', cols = grid.cols, rows = grid.rows)


if __name__ == "__main__":
    app.run(debug=True)