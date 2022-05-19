from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
     json_ = request.json
     query_df = pd.DataFrame(json_)
     query = pd.get_dummies(query_df)
    
     model = joblib.load('model.pkl')
     prediction = model.predict(query)
     return jsonify({'prediction': list(prediction)})


if __name__ == '__main__':
     app.run(debug=True)