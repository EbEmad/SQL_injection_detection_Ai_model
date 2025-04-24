from fastapi import FastAPI, Request, Header
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional
import joblib
import time
import mysql.connector

app = FastAPI()

# Load model and vectorizer
model = joblib.load('./sql_injection_model.pkl')
vectorizer = joblib.load('./tfidf_vectorizer.pkl')
# DB config
db_config = {
    'host': 'localhost',
    'user': 'test_user',
    'password': 'test_password',
    'database': 'test_db'
}

# Request body structure
class PredictionRequest(BaseModel):
    sentences: List[str]

# Function to log request metadata
def log_request_to_db(source_ip, request_type, endpoint, response_time, user_agent,
                      content_length, status_code, referrer, query_parameters, headers,
                      error_message, api_version, client_id, request_id):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        print("Database connected successfully!")
        query = """
        INSERT INTO requests (
            source_ip, request_type, endpoint, response_time, user_agent, content_length,
            status_code, referrer, query_parameters, headers, error_message, api_version,
            client_id, request_id
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            source_ip, request_type, endpoint, response_time, user_agent, content_length,
            status_code, referrer, query_parameters, headers, error_message, api_version,
            client_id, request_id
        ))
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Error logging request: {e}")

# Prediction endpoint
@app.post("/predict")
async def predict(
    request: Request,
    body: PredictionRequest,
    user_agent: Optional[str] = Header(None),
    content_length: Optional[int] = Header(None),
    x_client_id: Optional[str] = Header(None),
    x_request_id: Optional[str] = Header(None),
    referer: Optional[str] = Header(None)
):
    start_time = time.time()
    try:
        sentences = body.sentences
        transformed = vectorizer.transform(sentences)
        predictions = model.predict(transformed)
        probabilities = model.predict_proba(transformed)
        avg_confidence = probabilities.max(axis=1).mean()

        response_time = time.time() - start_time

        await request.body()  # Needed to read the request to avoid "already consumed" error

        log_request_to_db(
            source_ip=request.client.host,
            request_type=request.method,
            endpoint=request.url.path,
            response_time=response_time,
            user_agent=user_agent,
            content_length=content_length,
            status_code=200,
            referrer=referer,
            query_parameters=str(request.query_params),
            headers=str(request.headers),
            error_message=None,
            api_version="v1",
            client_id=x_client_id,
            request_id=x_request_id
        )

        return {
            "predictions": predictions.tolist(),
            "average_confidence": avg_confidence
        }

    except Exception as e:
        response_time = time.time() - start_time
        log_request_to_db(
            source_ip=request.client.host,
            request_type=request.method,
            endpoint=request.url.path,
            response_time=response_time,
            user_agent=user_agent,
            content_length=content_length,
            status_code=500,
            referrer=referer,
            query_parameters=str(request.query_params),
            headers=str(request.headers),
            error_message=str(e),
            api_version="v1",
            client_id=x_client_id,
            request_id=x_request_id
        )
        return JSONResponse(status_code=500, content={"error": str(e)})
