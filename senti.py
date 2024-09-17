import streamlit as st
import joblib

try:
    # Load the saved model and vectorizer
    model = joblib.load('sentiment_model.pkl')
    vectorizer = joblib.load('tfidf_vectorizer.pkl')
except Exception as e:
    st.error(f"Error loading model or vectorizer: {e}")
    st.stop()

# Streamlit title
st.title("Sentiment Analysis")

# Input box for custom review
review = st.text_area("Enter your movie review:")

if st.button("Predict Sentiment"):
    try:
        # Transform the review using the saved TF-IDF vectorizer
        review_tfidf = vectorizer.transform([review])
        
        # Make prediction using the trained model
        prediction = model.predict(review_tfidf)
        
        # Convert prediction to a readable label
        prediction_label = 'positive' if prediction == 1 else 'negative'
        
        # Display the result
        st.write(f"The sentiment of the review is: **{prediction_label}**")
    except Exception as e:
        st.error(f"Error making prediction: {e}")
