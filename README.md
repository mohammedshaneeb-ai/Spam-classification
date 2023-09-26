# Email Spam Classification using Machine Learning

This project is an email spam classification system that uses logistic regression with Sentence Transformers for embedding to determine whether an input message is spam or not. Users can interact with the model through a Streamlit web application.


## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)

## Introduction

Email spam classification is a common problem in the field of natural language processing and machine learning. This project demonstrates a simple yet effective solution for classifying emails as spam or ham (non-spam).

The key components of this project are:

- **Machine Learning Model:** A logistic regression model trained on message embeddings generated using Sentence Transformers.

- **Streamlit Application:** An interactive web application that allows users to input a message and receive a classification result.

## Prerequisites

Before setting up the project, make sure you have the following prerequisites installed on your system:

- Python (>=3.7)
- pip (Python package manager)

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/email-spam-classification.git
   cd email-spam-classification
   ```
2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate

   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Download the Spacy model:
   ```bash
   python -m spacy download en_core_web_sm
   ```


## Usage

1. Start the Streamlit application:
  ```bash
  streamlit run app.py
  ```

2. Open your web browser and go to the URL provided by Streamlit (usually http://localhost:8501).

3. In the web application, enter a message you want to classify as spam or ham.

4. Click the "Classify" button to receive the classification result.




