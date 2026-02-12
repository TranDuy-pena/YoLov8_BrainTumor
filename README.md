### 🧠🔬 Brain Tumor Detection using YOLOv8
🚀 Ứng dụng AI trong chẩn đoán hình ảnh y khoa – Phát hiện u não từ ảnh MRI/X-ray bằng YOLO


## 🎯 Mục tiêu dự án là xây dựng một hệ thống Deep Learning có khả năng:

🧠 Phát hiện khối u não

📦 Khoanh vùng chính xác bằng Bounding Box

📊 Phân loại Tumor / No Tumor

⚡ Dự đoán nhanh theo thời gian thực

🌐 Sẵn sàng tích hợp Web / API

## Hệ thống sử dụng mô hình YOLOv8 dựa trên PyTorch.

🏥 Ứng Dụng Thực Tế

👨‍⚕️ Hỗ trợ bác sĩ chẩn đoán sơ bộ

🏥 Hệ thống hỗ trợ bệnh viện tuyến dưới

📚 Công cụ học tập cho sinh viên y khoa & AI

🔍 Sàng lọc hình ảnh tự động

# ⚠️ Dự án chỉ mang tính nghiên cứu – không thay thế chẩn đoán chuyên môn.

## 🧬 Kiến Trúc Tổng Quan Hệ Thống

📂 Dataset (MRI/X-ray Images)
        ↓
✏️ Annotation (LabelImg / Roboflow)
        ↓
🧠 Training YOLOv8
        ↓
🏆 best.pt Model
        ↓
🔎 Inference / Web App / API

| Thành phần          | Công nghệ           |
| ------------------- | ------------------- |
| 🔥 Deep Learning    | PyTorch             |
| 🎯 Detection Model  | YOLOv8              |
| 🖼 Image Processing | OpenCV              |
| 📊 Visualization    | Matplotlib          |
| 🏷 Annotation       | LabelImg / Roboflow |
| ☁ Dataset Source    | Kaggle              |

## 📊 Dataset

# 📁 Dataset bao gồm:

Ảnh MRI não

Ảnh X-ray (tuỳ phiên bản)

2 nhãn chính:

Tumor

No Tumor

📐 Định dạng nhãn theo chuẩn YOLO


## 📂 Cấu Trúc Thư Mục
brain-tumor-yolo/
│
├── dataset/
│   ├── images/train
│   ├── images/val
│   ├── labels/train
│   ├── labels/val
│
├── runs/
│   ├── detect/
│
├── app/
│   ├── api.py
│   ├── web.py
│
├── train.py
├── predict.py
├── requirements.txt
└── README.md

## ⚙️ Cài Đặt Môi Trường

# 📦 Cài đặt thư viện
pip install ultralytics opencv-python matplotlib numpy torch

# 🚀Cấu Hình Huấn Luyện Model
yolo detect train \
data=data.yaml \
model=yolov8n.pt \
epochs=100 \
imgsz=640 \
batch=16

# 🔎 Dự Đoán Ảnh
yolo detect predict \
model=best.pt \
source=test.jpg \
conf=0.5


## 📈 Đánh Giá Mô Hình
| Metric           | Giá trị tham khảo    |
| ---------------- | -------------------- |
| 🎯 mAP50         | 0.90 – 0.95          |
| 📊 Precision     | ~94%                 |
| 🔁 Recall        | ~92%                 |
| ⚡ Inference Time | < 30ms / image (GPU) |

## 🌐 Triển Khai Web

Có thể tích hợp với:

🐍 Flask

⚡ FastAPI

📊 Streamlit

⚛ React + REST API

# Chạy demo Streamlit:
streamlit run web.py

## 🔐 Các Cải Tiến Trong Tương Lai

 🧬 Phân loại đa lớp (Glioma, Meningioma, Pituitary...)

 🔍 Ứng dụng YOLOv8x cho độ chính xác cao hơn

 🧠 Thêm Grad-CAM để giải thích mô hình

 ☁ Deploy lên AWS / GCP

 📱 Tích hợp Mobile App

## ⚠️ Medical Disclaimer

🚨 Hệ thống này được phát triển phục vụ mục đích nghiên cứu, học tập và thử nghiệm công nghệ Trí tuệ Nhân tạo trong lĩnh vực xử lý ảnh y khoa.

Kết quả dự đoán từ mô hình YOLO chỉ mang tính chất hỗ trợ tham khảo, dựa trên dữ liệu huấn luyện và thuật toán học máy. Hệ thống không được thiết kế để thay thế chẩn đoán lâm sàng, không thể đảm bảo độ chính xác tuyệt đối trong mọi trường hợp và không nên được sử dụng như một công cụ chẩn đoán độc lập.

Các yếu tố như:

📉 Chất lượng ảnh MRI/X-ray

🧬 Độ đa dạng của dữ liệu huấn luyện

⚙️ Cấu hình mô hình

🧑‍⚕️ Bối cảnh bệnh lý cụ thể của bệnh nhân

đều có thể ảnh hưởng đến kết quả dự đoán.

🩺 Mọi quyết định y khoa phải được thực hiện bởi bác sĩ chuyên khoa thần kinh, bác sĩ chẩn đoán hình ảnh hoặc chuyên gia y tế có chuyên môn phù hợp.

Tác giả dự án không chịu trách nhiệm cho bất kỳ hậu quả nào phát sinh từ việc sử dụng hệ thống vào mục đích chẩn đoán, điều trị hoặc ra quyết định y tế thực tế.

## 👨‍💻 Tác Giả

👤 Name: Lê Trần Duy

🎓 University: NGUYEN TAT THANH University

📧 Email: letranduy24503@gmail.com


## ⭐ Nếu thấy dự án hữu ích

Hãy ⭐ repo để ủng hộ!
