from flask import Flask, render_template, request, jsonify
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image
import io
import base64

app = Flask(__name__)

# Load model YOLO
model = YOLO(r"G:\Hk9\DoAnChuyenNganhTTNT\brain-tumor\runs\train\yolo_brain_tumor_continue26\weights\best.pt")  # thay bằng đường dẫn model của bạn

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        file = request.files["image"]
        img_bytes = file.read()
        img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
        img = np.array(img)

        results = model(img)
        annotated_img = results[0].plot()

        # Đếm số bounding box
        num_detected = len(results[0].boxes)

        _, buffer = cv2.imencode(".jpg", annotated_img)
        img_base64 = base64.b64encode(buffer).decode("utf-8")

        return jsonify({
            "predicted_image_base64": img_base64,
            "detected": num_detected
        })
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
