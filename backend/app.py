from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allow frontend connections

# Load trained model
MODEL_PATH = 'model/model.h5'

model = tf.keras.models.load_model(MODEL_PATH)

# Class names (match your dataset)
classes = [
    'Bacterial_spot',
    'Early_blight',
    'healthy',
    'Late_blight',
    'Leaf_Mold',
    'powdery_mildew',
    'Septoria_leaf_spot',
    'Spider_mites_Two-spotted_spider_mite',
    'Target_Spot',
    'Tomato_mosaic_virus',
    'Tomato_Yellow_Leaf_Curl_Virus'
]

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get uploaded file
        file = request.files['image']
        if not file:
            return jsonify({'error': 'No file uploaded'}), 400

        filepath = os.path.join('uploads', file.filename)

        file.save(filepath)

        # Preprocess the image
        img = image.load_img(filepath, target_size=(224, 224))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Make prediction
        preds = model.predict(img_array)
        predicted_class = classes[np.argmax(preds)]
        confidence = round(np.max(preds) * 100, 2)

        # Delete temp file
        os.remove(filepath)

        return jsonify({
    'predicted_class': str(predicted_class),
    'confidence': float(confidence)
})



    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

