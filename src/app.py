from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import uvicorn
from pathlib import Path

# Load the trained SVM model and TF-IDF vectorizer
model_path = Path(r"svm_model.pkl")
vectorizer_path = Path(r"tfidf_vectorizer.pkl")

with open(model_path, "rb") as model_file:
    model = pickle.load(model_file)

with open(vectorizer_path, "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Initialize FastAPI app
app = FastAPI()

# Define request model
class ReviewInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "FastAPI is running! Use /predict-text to analyze sentiment."}

@app.post("/predict-text")
def predict_text(data: ReviewInput):
    """API Endpoint to predict sentiment from a text input."""
    try:
        review_text = data.text.strip()

        # Ensure the text is not empty
        if not review_text:
            return {"error": "Text field is empty"}

        # Transform input using TF-IDF vectorizer
        review_tfidf = vectorizer.transform([review_text])

        # Make prediction
        prediction = model.predict(review_tfidf)[0]
        sentiment = "positive" if prediction == 1 else "negative"

        return {"review": review_text, "sentiment": sentiment}

    except Exception as e:
        return {"error": str(e)}

# Run FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
