from cgi import test
from flask import Flask, request, render_template, jsonify
import pandas as pd
import pickle
import statsmodels.api as sm

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
          two_pointer = float(my_dict.get("2pointer"))
          three_pointer = float(my_dict.get("3pointer"))
          freethrow = float(my_dict.get("freethrow"))
          assists = float(my_dict.get("assists"))
          rebounds = float(my_dict.get("rebounds"))
          attendance = float(my_dict.get("attendance"))

          

          columns = ['2pointer_PCT_AVG', '3pointer_PCT_AVG', 'FreeThrow_PCT_AVG', 'Assists_AVG', 'Rebounds_AVG', 'Attendance']
          test_data = pd.DataFrame([[two_pointer,three_pointer,freethrow,assists,rebounds,attendance]], columns=columns)
          test_data = sm.add_constant(test_data, has_constant='add')
          print(test_data)
          # return test_data.to_json()
          model = pickle.load(open('Models_Folder_Updated/Models/Games_OLS.sav','rb'))
          prediction_df = model.predict(test_data)
          prediction = int(prediction_df[0])
          print(prediction)
          # return {'prediction' : prediction}

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