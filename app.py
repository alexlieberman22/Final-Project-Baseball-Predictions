from flask import Flask, request, render_template, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
     return render_template("index.html")

@app.route('/predict1', methods=['GET','POST'])
def predict():
     # json = request.json
     # querydf = pd.DataFrame(json)

     # model = joblib.load('model.pkl')
     # prediction = model.predict(query)
     # return jsonify({'prediction': list(prediction)})

     
    # Code for select dropdown
     # if request.method == 'POST':
     #      my_json = request.json
     #      number1 = my_json.get("number1")
     #      number2 = my_json.get("number2")
     #      prediction = int(number1) + int(number2)
     #      return {"prediction": prediction}

     # Code for input form
     if request.method == 'POST':
          my_dict = request.form.to_dict()
          number1 = my_dict.get("number1")
          number2 = my_dict.get("number2")
          prediction = int(number1) + int(number2)
          return render_template('predict_1.html', prediction=prediction)
        
     return render_template('predict_1.html')

@app.route('/prediction_teams', methods=['GET','POST'])
def prediction_1():

     json = request.json
     querydf = pd.DataFrame(json)

     model = joblib.load('Models/Games_OLS.sav')
     prediction = model.predict(querydf)
     return jsonify({'prediction_wins': prediction})




     return render_template('prediction_teams.html')

@app.route('/prediction_players', methods=['GET','POST'])
def prediction_2():

     # json = request.json
     # querydf = pd.DataFrame(json)

     # model = joblib.load('model.pkl')
     # prediction = model.predict(query)
     # return jsonify({'prediction': prediction})



     return render_template('prediction_players.html')

if __name__ == '__main__':
     app.run(debug=True)