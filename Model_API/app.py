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
 
     if request.method == 'POST':
          my_dict = request.form.to_dict()
          number1 = my_dict.get("number1")
          number2 = my_dict.get("number2")
          prediction = number1 + number2
          

     return render_template('predict_1.html', prediction=prediction)

if __name__ == '__main__':
     app.run(debug=True)