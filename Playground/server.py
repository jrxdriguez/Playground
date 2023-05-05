from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/play')
def home():
    return render_template('index.html', times=3, color='blue')

@app.route('/play/<int:x>')
def display_square(x):
    return render_template('index.html', times=x, color='blue')

@app.route('/play/<int:x>/<color>')
def display_square_colors(x, color):
    return render_template('index.html', times=x, color=color)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=5001)    # Run the app in debug mode.

