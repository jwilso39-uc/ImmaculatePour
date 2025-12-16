from flask import Flask, request, render_template, session

app = Flask(__name__)
app.secret_key = """obviously in a real situation this would be somewhere else 
but worried about testers not being able to replicate if I do that
"""

@app.route("/") # type: ignore
def main():
    """
    Main page to play game
    """
    return render_template('grid.html')

if __name__ == "__main__":
    main()