from flask import Flask, request, render_template
import pandas as pd
# import joblib

app = Flask(__name__)

@app.route('/predict_1', methods=['POST'])
def predict():
     # json_ = request.json
     # query_df = pd.DataFrame(json_)
     # query = pd.get_dummies(query_df)
    
     # model = joblib.load('model.pkl')
     # prediction = model.predict(query)
     # return jsonify({'prediction': list(prediction)})
 
     number_1 = request.json.get("number1")
     number_2 = request.json.get("number2")
     output = number_1 + number_2

     return render_template('predict_1.html', output=output)

if __name__ == '__main__':
     app.run(debug=True)