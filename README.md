# Sentiment Analysis Microservice Deployment (Amazon Product Review)
 
1. General Description of the Service
The deployed microservice provides sentiment analysis for Amazon product reviews using a pre-trained SVM model with TF-IDF vectorization. This service determines whether a given text expresses a
positive or negative sentiment.
  - Backend: FastAPI hosted on Render
  - Frontend: Streamlit app for user interaction
________________________________________
2. Service URL

 - FastAPI Backend: https://amazon-product-review-eai6010-mod5.onrender.com
 - Streamlit Frontend: https://amazonreviewsentimentanalysis.streamlit.app/
________________________________________
3. API Endpoints & Usage
3.1. Home Endpoint (Health Check)
- URL: https://amazon-product-review-eai6010-mod5.onrender.com/
- Method: GET

Response Example: 
- {"message": "FastAPI is running! Use /predict-text to analyze sentiment."}
- Purpose: Confirms that the API is live and running.
________________________________________
3.2. Sentiment Analysis Endpoint
- URL: https://amazon-product-review-eai6010-mod5.onrender.com/predict-text
- Method: POST
- Input Format: JSON 
- {"text": "This product is amazing!"}
- Expected Output: JSON response with sentiment classification 
- {"review": "This product is amazing!", "sentiment": "positive”}
- Error Handling: 
  - If the input is empty: 
  - {"error": "Text field is empty"}
  - If API fails: 
  - {"error": "Could not analyze sentiment. Try again!"}
________________________________________
4. Frontend (Streamlit Web App)
For a user-friendly interface, the Streamlit frontend allows users to enter text and get instant sentiment analysis results.
- URL: https://amazonreviewsentimentanalysis.streamlit.app/

- How to Use: 
1.	Open the web app.
2.	Enter a product review in the text box.
3.	Click "Analyze Sentiment".
4.	View the result (Positive 😊 or Negative 😞).

5. Example Use Cases
Input (Review Text)	API Output (Sentiment)
"The battery lasts long and the design is great!"	"positive" 😊
"Terrible quality! Broke within a week."	"negative" 😞
"Fast shipping and excellent customer service!"	"positive" 😊
"Not worth the price. Very disappointed."	"negative" 😞
________________________________________
6. Deployment Details
Component	Technology Used
Backend	FastAPI (hosted on Render)
Model	SVM with TF-IDF
Frontend	Streamlit (hosted on Streamlit Cloud)
API Testing	Postman, cURL
Deployment Platform	Render (backend), Streamlit Cloud (frontend)
________________________________________
7. Instructor Testing Instructions
  
1.	Test API via Browser (Health Check)
Open: https://amazon-product-review-eai6010-mod5.onrender.com/
2.	Enter a review in the provided input box.
3.	Click the Analyze button to receive the sentiment classification result.
 
 
8. Test API via Postman or cURL
- Method: POST
- URL: https://amazon-product-review-eai6010-mod5.onrender.com/predict-text
- Body (JSON):
- {"text": "This product is fantastic!"}
- Expected Response:
- {"review": "This product is fantastic!", "sentiment": "positive"}

9.	Test Web Interface (Easiest Way)
Open: https://amazonreviewsentimentanalysis.streamlit.app/
- Enter any review text.
- Click Analyze Sentiment.
- View the result.
![image](https://github.com/user-attachments/assets/8348031e-de78-49f3-bbb1-a5e943c25338)
![image](https://github.com/user-attachments/assets/437e4247-0424-47f8-9998-831007f0dcf2)


