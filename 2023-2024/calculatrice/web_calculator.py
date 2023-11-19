from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])



def calculator():
    if request.method == "POST":
        x = int(request.form["x"])
        y = int(request.form["y"])
        op = request.form["op"]
        result = None

        if op == "+":
            result = x + y
        elif op == "-":
            result = x - y
        elif op == "*":
            result = x * y

        return render_template("calculator.html", result=result)

    return render_template("calculator.html")

if __name__ == "__main__":
    app.run(debug=True)

