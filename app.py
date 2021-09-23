from flask import Flask, render_template, request


app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# @app.route("/predict", methods=["POST"])
# def predict():
#     Name = request.form["Name"]
#     City = request.form["City"]
#     State = request.form["State"]
#     category = request.form["category"]
#     Student_Population = request.form["Student_Population"]
#     Total_Annual_Cost = request.form["Total_Annual_Cost"]
    
#     predicated_price = country_rank_prediction(model,Name, City, State, category, Student_Population, Total_Annual_Cost)
#     predicated_price = predicated_price.astype("int")

#     return render_template("index.html", prediction_text="Country Rank of:- {}".format(predicated_price))


if __name__ == "__main__":
    app.run()    
    