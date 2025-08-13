from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS # CORS for handling Cross-Origin Resource Sharing
import pickle 

# Create a Flask application instance
app = Flask(__name__)

# Enable CORS for all routes, allowing requests from any origin
CORS(app,resources={r"/*":{"origins":"*"}})


placement = pickle.load(open('placement.pkl', 'rb'))

# Define a route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        query_df = pd.DataFrame([data])
        prediction = placement.predict(query_df)
        return jsonify({'Package': list(prediction)})
    except Exception as e:
        return jsonify({'error': str(e)})



if __name__ == '__main__':
    app.run(debug=True, port=5000)