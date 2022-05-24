from flask import Flask, request, render_template
import pandas as pd
# import joblib

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
     return render_template("index.html")

@app.route('/predict_1', methods=['GET','POST'])
def predict():
     # json_ = request.json
     # query_df = pd.DataFrame(json_)
     # query = pd.get_dummies(query_df)
    
     # model = joblib.load('model.pkl')
     # prediction = model.predict(query)
     # return jsonify({'prediction': list(prediction)})

     if request.method == 'POST':
          my_json = request.json
          number1 = my_json.get("number1")
          number2 = my_json.get("number2")
          prediction = int(number1) + int(number2)
          return {"prediction": prediction}

     return render_template('predict_1.html')

@app.route('/prediction_1', methods=['GET','POST'])
def prediction_1():

     return render_template('prediction_1.html')

@app.route('/prediction_2', methods=['GET','POST'])
def prediction_2():

     return render_template('prediction_2.html')

if __name__ == '__main__':
     app.run(debug=True)