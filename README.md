# Health Insurance Charge Prediction App

## Table of Contents
1. [Overview](#overview)
2. [Setup Instructions](#setup-instructions)
3. [Application Features](#application-features)
4. [Application Routes](#application-routes)
5. [Model Description](#model-description)
6. [Data Description](#data-description)
7. [Technologies Used](#technologies-used)
8. [License](#license)

## Overview

The Health Insurance Charge Prediction App is a web application developed using Flask and machine learning to predict health insurance charges based on user input. The app uses a trained Random Forest Regressor model to provide insights into expected medical costs based on several features such as age, sex, BMI, number of children, smoking status, and geographical region.

## Setup Instructions

1. Clone the repository or download the code files:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```

3. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
   ```

4. Install required packages:
   ```bash
   pip install pandas numpy scikit-learn flask
   ```

5. Place the `insurance.csv` file in the project directory.

6. Run the application:
   ```bash
   python insurance.py
   ```

7. Open your web browser and go to `http://127.0.0.1:9000/`.

## Application Features

- **Home Page**: Welcomes users with a brief message.
- **Charges Prediction**: Users can input personal details and get a prediction of health insurance charges.
- **Visualization**: Provides data visualization and insights.
- **About Page**: Displays statistical information about the dataset and model performance.

## Application Routes

- `/` (GET): Renders the home page with a greeting message.
- `/charge` (GET, POST): Renders a form for users to input data required for charge prediction.
- `/predict` (GET, POST): Processes the input data, makes a prediction using the trained model, and renders the results.
- `/visualization` (GET): Renders a page for data visualization insights.
- `/About` (GET): Provides statistical information about the dataset and model performance.

## Model Description

- **Model Used**: Random Forest Regressor
- **Purpose**: To predict health insurance charges based on multiple features from the input data.
- **Training**: The model is trained using a portion of the dataset split into training and test sets (80% training, 20% testing).

## Data Description

The application uses the `insurance.csv` dataset, which includes the following features:

- **age**: Age of the primary beneficiary.
- **sex**: Gender of the beneficiary (male, female).
- **bmi**: Body Mass Index.
- **children**: Number of dependents covered by health insurance.
- **smoker**: Smoking status (yes, no).
- **region**: Geographical area in the US (northeast, southeast, southwest, northwest).
- **charges**: Medical costs billed by health insurance (target variable).

## Technologies Used

- **Flask**: Web framework for building the application.
- **Pandas**: Data manipulation and analysis.
- **NumPy**: Numerical computations.
- **Scikit-Learn**: Machine learning library for model training and predictions.
- **HTML/CSS**: For front-end design and user interface.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
