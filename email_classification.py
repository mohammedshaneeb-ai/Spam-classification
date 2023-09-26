import streamlit as st
import joblib  
from sentence_transformers import SentenceTransformer
from utils import preprocess_text


# loading custom trained classification model
model = joblib.load('email_classification.pkl')
# initializing embedding model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Title of app
st.title("Spam Classification App")

# Add text input for user
user_input = st.text_input("Enter a message:")

# Add a button to trigger classification
if st.button("Classify"):
    # Preprocess the user input 
    preprocessed_input = preprocess_text(user_input)

    # Embedd the text
    embedded_text = embedding_model.encode(preprocessed_input)

    # Using custom trained model for classification
    prediction = model.predict([embedded_text])[0]

    # Display the result
    if prediction == 1:
        st.error("This message is spam.")
    else:
        st.success("This message is not spam.")
