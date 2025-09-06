# SQL Injection Detection AI Model  

##  Introduction  
SQL Injection (SQLi) is a type of attack where malicious SQL statements are injected into an application’s database query, potentially allowing attackers to manipulate, extract, or delete data. There are several types of SQL injection attacks, including:  

- **Union-Based SQLi**: Exploits the `UNION` operator to retrieve data from different tables.  
- **Error-Based SQLi**: Forces the database to generate error messages revealing information about the structure.  
- **Boolean-Based SQLi**: Sends different queries and observes application responses to infer data.  
- **Time-Based SQLi**: Uses SQL queries with time delays (`SLEEP()`) to infer information based on response time.  
- **Blind SQLi**: Exploits databases without receiving direct feedback, requiring advanced inference techniques.  

---

##  Project Overview  
This project focuses on building an **AI-powered SQL Injection detection model** that classifies input queries as either **benign (clean) or malicious (SQLi)**. The model is deployed via a **Flask API**, running in a **Docker container**, alongside a **MySQL database** to log all requests.  

### **Key Features:**  
 **Machine Learning Model**: A `RandomForestClassifier` trained on an enhanced dataset.  
 **Feature Engineering**: Utilizes **TF-IDF Vectorization** to process textual input.  
 **Data Augmentation**: Incorporates additional SQL injection datasets for better generalization.  
 **Hyperparameter Tuning**: Optimized using **Grid Search** and **Random Search**.  
 **Model Deployment**: Fast server with a REST API for real-time predictions.  
 **Logging System**: Every request is stored in a MySQL database for analysis.  

---

##  Project Structure  
```
 **SQLi-Detection**  
├──  app.py # FastAPI API for SQLi detection
├──  docker-compose.yml # Docker setup for Fast & MySQL
├──  init.sql # SQL script for logging requests in MySQL
├──  sql_injection_model.pkl # Trained ML model
├──  tfidf_vectorizer.pkl # Pretrained TF-IDF vectorizer
├──  README.md # Project documentation
```
---

## Machine Learning Pipeline  

1. **Data Preprocessing**  
   - Loaded a dataset containing SQL injection samples and benign inputs.  
   - Removed duplicates, handled missing values, and shuffled data for randomness.  
   - Balanced dataset using **data augmentation techniques**.  

2. **Feature Extraction**  
   - **TF-IDF Vectorization** was used to convert text inputs into numerical representations.  
   - Performed **Grid Search** to fine-tune the vectorizer’s parameters.  

3. **Model Training & Tuning**  
   - Implemented a **RandomForestClassifier** with class weighting to handle imbalances.  
   - Conducted **Random Search & Grid Search** to optimize hyperparameters.  
   - Evaluated performance using **cross-validation and classification reports**.  

4. **Model Evaluation**  
   - Achieved an **accuracy of 99.67%** on the test dataset.  
   - Used a **confusion matrix** to visualize misclassified samples.  
   - Extracted **important features** to interpret model decisions.  

5. **Deployment & Logging**  
   - Wrapped the model in a **Fast API** for real-time predictions.  
   - Set up **MySQL logging** to store all incoming requests and responses.  
   - Packaged everything into a **Docker container** for easy deployment.  

---

##  Running the Project  

### **Step 1: Clone the Repository**  
```bash
git clone https://github.com/EbEmad/SQL_injection_detection_Ai_model.git
cd SQL_injection_detection_Ai_model

```
### **Step 2: Build & Run the Docker Containers**  
```bash
docker-compose up --build
```
🔹 This starts both the Fast API (localhost:5000) and the MySQL database (localhost:3306).

### **Step 3: Test the API**
```bash
curl -X POST "http://localhost:5000/predict" -H "Content-Type: application/json" -d '{
  "sentences": ["SELECT * FROM users WHERE username='admin' --"]
}'
```
🔹 The API will return a prediction:
```bash
{
  "predictions": [1],  
  "average_confidence": 0.98  
}
```
🔹 Where 1 = SQLi Detected and 0 = Clean Query.


 Technologies Used
```
🔹 Python (Fast, Sklearn, Pandas, Numpy) – Model development & API.
🔹 Machine Learning (Random Forest, TF-IDF) – Feature extraction & classification.
🔹 Docker – Containerized deployment.
🔹 MySQL – Logging requests & responses.
```
 Conclusion
This project provides a real-time SQL Injection detection system powered by machine learning. With high accuracy and fast performance, it can be easily integrated into web applications, firewalls, and security systems to prevent SQLi attacks.

🔹 Future Improvements:

Expand training data with real-world SQL injection payloads.
Explore Deep Learning (LSTMs, Transformers) for enhanced text analysis.
Implement real-time monitoring dashboards for API usage.

