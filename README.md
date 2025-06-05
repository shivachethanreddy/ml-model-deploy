# 🧠 Machine Learning Model Deployment Project

## ✅ Component Overview

| Component     | Status  | Description                            |
|---------------|---------|----------------------------------------|
| **ML Model**  | ✅ Done | Extracted from Jupyter Notebook        |
| **API**       | ✅ Done | Flask-based prediction service         |
| **Deployment**| ✅ Done | Hosted on [Render](https://render.com) |
| **CI/CD**     | ✅ Done | Automated via GitHub Actions           |
| **Scheduling**| ✅ Done | Hourly retraining via GitHub Schedule  |

---

## 🚀 Visit the Deployed Site

👉 **[Click here to access the API](https://ml-model-deploy-zujx.onrender.com)**

---

## 📡 API Usage

### 🔹 POST `/predict`

#### ✅ Request Body (JSON):

{
"features": [1, 2, 3, ..., 20]
}


#### ✅ Response:

{
"prediction": 4.2
}



---

## 📦 Project Structure

ml_model_deploy/
'''

1) app.py # Flask application
2) model.pkl # Trained ML model file
3) requirements.txt # Python dependencies
4) .github/workflows/ # GitHub Actions CI/CD scripts
5) README.md # Project documentation


'''
---

## 🛠️ Built With

- Python
- Flask
- scikit-learn
- NumPy
- Render
- GitHub Actions

---

> 💡 This project demonstrates a complete ML workflow: training, API serving, deployment, CI/CD automation, and scheduled retraining.












