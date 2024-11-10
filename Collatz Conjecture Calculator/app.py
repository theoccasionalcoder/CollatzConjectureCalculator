from flask import Flask, render_template, request

app = Flask(__name__)

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    sequence = []
    
    if request.method == "POST":
        try:
            number = int(request.form["number"])
            if number <= 0:
                message = "Please enter a positive integer."
            else:
                sequence = collatz_sequence(number)
        except ValueError:
            message = "Please enter a valid integer."
    
    return render_template("index.html", message=message, sequence=sequence)

if __name__ == "__main__":
    app.run(debug=True)
