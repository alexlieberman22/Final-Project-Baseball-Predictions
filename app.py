from flask import Flask, request, render_template, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
     return render_template("index.html")

# @app.route('/predict_1', methods=['GET','POST'])
# def predict():
#      # json = request.json
#      # querydf = pd.DataFrame(json)

#      # model = joblib.load('model.pkl')
#      # prediction = model.predict(query)
#      # return jsonify({'prediction': list(prediction)})

#      if request.method == 'POST':
#           my_json = request.json
#           number1 = my_json.get("number1")
#           number2 = my_json.get("number2")
#           prediction = int(number1) + int(number2)
#           return {"prediction": prediction}

#      return render_template('predict_1.html')

@app.route('/prediction_teams', methods=['GET','POST'])
def prediction_1():

     # json = request.json
     # querydf = pd.DataFrame(json)

     # model = joblib.load('Models/Games_OLS.sav')
     # prediction = model.predict(querydf)
     # return jsonify({'prediction_wins': prediction})

     if request.method == 'POST':
          my_dict = request.form.to_dict()
          # two_pointer = my_dict.get("2pointer")
          # three_pointer = my_dict.get("3pointer")
          # freethrow = my_dict.get("freethrow")
          # assists = my_dict.get("assists")
          # rebounds = my_dict.get("rebounds")
          # attendance = my_dict.get("attendance")


          querydf = pd.DataFrame(my_dict)
          # print(querydf)
          # model = joblib.load('Models/Games_OLS.sav')
          # prediction = model.predict(querydf)
          # print(prediction)
          
          return querydf
          return render_template('prediction_teams.html', prediction_wins=prediction)
          # prediction = int(number1) + int(number2)
          # return render_template('predict_1.html', prediction=prediction)


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