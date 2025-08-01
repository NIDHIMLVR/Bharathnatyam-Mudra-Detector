from flask import Flask, request, jsonify,render_template
from flask_cors import CORS
from tensorflow.keras.models import load_model
import numpy as np
import os

app = Flask(__name__)
CORS(app)  # 👈 Add this line to enable CORS


label_map = ['Ardhapathaka', 'Kartarimukha', 'Mayura', 'Pathaka', 'Tripathaka']
model = None

@app.route('/')
def home():
    global model
    if model is None:
        model = load_model('new_hand_landmark_classifier.h5')
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        keypoints = data.get("keypoints")
        if not keypoints or len(keypoints) != 63:
            return jsonify({"error": "Invalid keypoints"}), 400

        prediction = model.predict(np.array([keypoints]), verbose=0)
        class_id = int(np.argmax(prediction))
        confidence = float(np.max(prediction))

        return jsonify({
            "label": label_map[class_id],
            "confidence": confidence
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@app.route('/ping', methods=['GET'])
def ping():
    return "pong", 200
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use PORT env variable if present
    app.run(host='0.0.0.0', port=port)