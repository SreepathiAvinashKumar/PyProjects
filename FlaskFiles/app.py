from flask import Flask, request, render_template

app = Flask(__name__)

SPORTS = ["BasketBall", "VolleyBall", "FootBall", "Kabaddi", "Koko"]

@app.route("/")
def index():
    return render_template("form.html",sports=SPORTS)


@app.route("/form", methods=["POST"])
def form():
    # name = request.args.get("name") for the GET
    # name = request.form.get("name")
    if not request.form.get("name") or request.form.get("sport") not in  SPORTS:
        return render_template("failure.html")

    return render_template("success.html")
    # return render_template("index.html", name=name)


    # if __name__ == '__main__':
    #     app.run()
