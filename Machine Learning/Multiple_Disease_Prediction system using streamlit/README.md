I apologize for the misunderstanding. Here's the full content as a Markdown file:

```markdown
# Multiple Disease Prediction System Web App

This repository contains a web application that predicts multiple diseases using machine learning models. The web app is built using Streamlit and allows users to input relevant medical parameters for different diseases and receive predictions.

## Project Structure

- `collab_notebook/`: Contains the Jupyter Notebook(s) used for data preprocessing, model training, and evaluation.

- `Models/`: Contains the trained machine learning models serialized using pickle.

- `system.py`: The main Python file for the Streamlit web application.

- `requirements.txt`: List of required Python packages and their versions.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Streamlit (`pip install streamlit`)
- Required libraries (automatically installed via `requirements.txt`):
  - scikit-learn==1.3.0
  - numpy
  - tensorflow
  - Pillow
  - pickle-mixin
  - streamlit-option-menu

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/multiple-disease-prediction.git
   cd multiple-disease-prediction
   ```

2. Install the required packages from the requirements.txt file:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Navigate to the project directory:
   ```bash
   cd multiple-disease-prediction
   ```

2. Run the Streamlit web app:
   ```bash
   streamlit run system.py
   ```

Access the web app in your browser by opening the displayed URL (usually http://localhost:8501).

Choose a disease from the sidebar menu, input the relevant medical parameters, and click the corresponding button to get the disease prediction.

## Datasets

The Multiple Disease Prediction System uses the following datasets:

- [Diabetes Dataset](https://www.kaggle.com/datasets/akshaydattatraykhare/diabetes-dataset)
- [Heart Disease Dataset](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)
- [Kidney Disease Dataset](https://www.kaggle.com/datasets/akshayksingh/kidney-disease-dataset)
- [Breast Cancer Dataset](https://www.kaggle.com/datasets/yasserh/breast-cancer-dataset)
- [Liver Disease Dataset](https://www.kaggle.com/datasets/uciml/indian-liver-patient-records)
- [Parkinson's Disease Dataset](https://www.kaggle.com/datasets/vikasukani/parkinsons-disease-data-set)
- [COVID-19 Radiography Database](https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database) (with COVID label)

Please download the datasets and provide the appropriate file paths in the Streamlit app for testing.

## Disease Prediction Results

| S.No | Disease Prediction      | Algorithm                  | Accuracy |
| ---- | ----------------------- | -------------------------- | -------- |
| 1    | Heart Disease           | Random Forest Classifier   | 98%      |
| 2    | Breast Cancer           | Random Forest Classifier   | 96%      |
| 3    | Kidney Disease          | Random Forest Classifier   | 100%     |
| 4    | Liver Disease           | Logistic Regression        | 77%      |
| 5    | Parkinson's Disease     | SVM                        | 88%      |
| 6    | Diabetes Disease        | Logistic Regression        | 76%      |
| 7    | COVID-19 Detection      | Xception Model             | 76%      |

### COVID-19 Detection Using X-ray Images

We've added a new feature to the system for COVID-19 detection using X-ray images. The model is based on the Xception architecture and achieves an accuracy of 76%. This addition allows users to upload X-ray images for COVID-19 prediction.

To get a COVID-19 prediction, select "COVID-19" from the sidebar menu, upload an X-ray image, and click the corresponding button. The model will provide you with the COVID-19 prediction.

Note: For this feature, please ensure you have a dataset of X-ray images for COVID-19 detection.
