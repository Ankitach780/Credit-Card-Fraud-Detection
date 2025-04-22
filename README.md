# Credit Card Fraud Detection

This project leverages machine learning algorithms to detect fraudulent credit card transactions using historical transaction data. The model is deployed using Streamlit to provide a simple user interface (UI) for predicting fraud in real-time.

## Project Overview

In this project, we use a **Random Forest Classifier** to classify transactions as either fraudulent or legitimate. The model is trained on historical credit card transaction data and is then deployed as a web app using Streamlit.

### Key Features:
- **Random Forest Classifier** for fraud detection.
- **Streamlit** UI to allow users to input transaction details and get fraud predictions in real-time.
- **SMOTE (Synthetic Minority Over-sampling Technique)** is used to handle class imbalance in the dataset.

## Installation

To run this project on your local machine, follow these steps:

### 1. Clone the repository

```bash
git clone https://github.com/Ankitach780/Credit-Card-Fraud-Detection.git
cd Credit-Card-Fraud-Detection
```
### 2. Install dependencies
Make sure you have Python 3.7+ installed. Then, install the required dependencies using pip:
```bash
pip install -r requirements.txt
```
### 3. Download or Train the Model
If you have a pre-trained model, you can skip training the model and simply use it. Otherwise, follow these steps to train the model:
- Preprocess the dataset.
- Train the Random Forest Classifier model.
- Save the model using joblib.
```bash
import joblib
from sklearn.ensemble import RandomForestClassifier

# After training, save the model
joblib.dump(model, 'random_forest_fraud.pkl')
```
### 4. Run the Streamlit App
Once you've set up everything, you can start the Streamlit app with:
```bash
streamlit run app.py
```
This will open the app in your browser at http://localhost:8501, where you can input transaction details and get real-time predictions on fraud detection.

## Model Explanation
The model used in this app is a Random Forest Classifier, trained on a dataset of credit card transactions. It predicts fraud based on the following features:
- Merchant
- Category
- Transaction Amount
- User's Age
- User's Gender
- City
- State
- Latitude/Longitude of merchant
- City Population
- Job and other merchant-related data

### 1. Prediction Results
The app provides the following outcomes:
- Fraud Detected: If the model predicts the transaction is fraudulent.
- Transaction is Not Fraud: If the model predicts the transaction is legitimate.

### 2. Model Evaluation
Performance Metrics:
- Accuracy: The Random Forest model achieves an accuracy of approximately 99.68% on the test data.
- Confusion Matrix: The confusion matrix is used to evaluate the performance on imbalanced data, where we focus on the model's ability to correctly identify fraudulent transactions (class 1.0).

## Contributing
If you would like to contribute to this project, feel free to open issues or submit pull requests. Contributions such as improving the model's performance, adding additional features to the app, or fixing bugs are always welcome.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
- Scikit-learn: For providing various machine learning algorithms including Random Forest Classifier.
- Streamlit: For creating the easy-to-use app framework.
- SMOTE: For addressing the class imbalance problem during training.

