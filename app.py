from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    binary = None

    if request.method == 'POST':
        try:
            decimal = int(request.form['decimal'])
            binary = bin(decimal)[2:]  # Menghapus prefix '0b' dari hasil bin()
        except ValueError:
            binary = "Invalid input"

    return render_template('index.html', binary=binary)

if __name__ == '__main__':
    app.run(debug=True)
