# **MoodLens - Sentiment Analysis Web App**

MoodLens is a **sentiment analysis web application** that utilizes **machine learning** (Logistic Regression) and a **React + Django full-stack architecture** to analyze textual data and classify it as **positive** or **negative**. This project showcases an end-to-end pipeline for data preprocessing, analysis, model integration, and a responsive UI for user interaction.

---

## **Features**
- 🧠 **Machine Learning Model**: Logistic Regression trained on a sentiment analysis dataset.
- 📊 **Data Analysis**: Preprocessing and exploratory data analysis (EDA) using Python and Pandas.
- 🎨 **Responsive Frontend**: Built with **ReactJS**, designed to be user-friendly and mobile-compatible.
- 🔗 **Backend API**: Powered by **Django**, serving predictions via RESTful APIs.
- 💾 **Full Stack Integration**: Seamless communication between React frontend and Django backend.
- 🌟 **Real-Time Sentiment Feedback**: Displays an attractive message to users after analyzing the sentiment.


---

## **Demo**

### **Screenshots**

<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=1XbbSLxsJ6hA4G-pKQWnlyOyeVUvCbDFV" alt="img" width="310" style="margin: 5px;">
  <img src="https://drive.google.com/uc?export=view&id=1I71HaILhacJkHe5h94Gb8FiBRYJ4W4Ys" alt="img" width="310" style="margin: 5px;">
  <img src="https://drive.google.com/uc?export=view&id=1YnCL5PD9EAG-BKJKJf9IFwPtd6fq-N4_" alt="img" width="310" style="margin: 5px;">
</p>
<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=1_DDcF4zgAyOfwoWalKAlK3ygm8W8J3xU" alt="img" width="310" style="margin: 5px;">
  <img src="https://drive.google.com/uc?export=view&id=1V-KypE5ROhvWcBf8GtaiExN5k8pp1cC4" alt="img" width="310" style="margin: 5px;">
  <img src="https://drive.google.com/uc?export=view&id=1gYk7no_ab9LWbCbrGTqbZk27ecSnPbbj" alt="img" width="310" style="margin: 5px;">
</p>
<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=1Trn0CKPIsh95ta8bvCaqq1avBuNw0azg" alt="img" width="166" style="margin: 5px;">
  <img src="https://drive.google.com/uc?export=view&id=1i3hC6yeCoPnwsxqvqHuPp06YaMX_yXjf" alt="img" width="310" style="margin: 5px;">
  <img src="https://drive.google.com/uc?export=view&id=1E8SOGRLeVZqdMI7XxJxHQHiAn6LEmRRU" alt="img" width="310" style="margin: 5px;">
</p>
<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=1jZeTp9fzyDZr_Ek65nxX340aX0jiNkQz" alt="img" width="166" style="margin: 5px;">
  <img src="https://drive.google.com/uc?export=view&id=12xf7DbVPnd9BsE3DuCKfg6toYjRBy0SC" alt="img" width="310" style="margin: 5px;">
</p>

### **Video**
**Project Video**

Click the image below to watch the project video

[![Watch the video](https://drive.google.com/uc?export=view&id=1XbbSLxsJ6hA4G-pKQWnlyOyeVUvCbDFV)](https://drive.google.com/file/d/1DGy-vg98Jt1OojSrKRdBtE9IU6VZws-D/view?usp=drive_link)



---

## **Tech Stack**
### **Frontend**
- **ReactJS**: Component-based UI library for building a dynamic and responsive user interface.
- **HTML/CSS**: Standard web technologies for structuring and styling the application.
- **JavaScript (ES6)**: Enhances interactivity and functionality of the frontend.

### **Backend**
- **Django**: A Python web framework for building and managing backend APIs.
- **REST Framework (DRF)**: Used for handling API endpoints.
- **Python**: Primary language for data analysis and machine learning.

### **Machine Learning**
- **Logistic Regression**: Supervised learning model for sentiment classification.
- **Pandas**: Data manipulation and preprocessing.
- **scikit-learn**: Building and training the machine learning model.

---

## **How It Works**
1. **Input**: Users enter a review or text on the MoodLens website.
2. **Frontend**: The text is sent to the backend via a POST request.
3. **Backend**:
   - Preprocesses the input text.
   - Feeds the text into the trained Logistic Regression model.
   - Returns the predicted sentiment as either **Positive** or **Negative**.
4. **Output**: The sentiment result is displayed to the user with an attractive, dynamic message on the frontend.

---

## **Project Setup**

### **Prerequisites**
- **Python**: >= 3.8
- **Node.js**: >= 14.x
- **Django**: >= 4.0
- **React**: >= 18.x

### **Backend Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/MoodLens.git
   cd MoodLens
   
2. **Set up the back-end**
   - Navigate to the backend folder.
   - Install dependencies and run the server
   ```bash
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver

3. **Set up the front-end**
   - Navigate to the frontend folder.
   - Install dependencies and run the development server
   ```bash
   npm install
   npm start

4. **Access the application at**
   ```bash
   http://localhost:3000/


---

## **Dataset**

### **The sentiment analysis model is trained using a dataset from Kaggle. The dataset consists of:**
- **Reviews**: Textual data that includes <br> tags, bullet points, etc., which were cleaned during preprocessing.
- **Sentiments**: Labels indicating whether the sentiment is Positive or Negative.

### **Data Preprocessing Steps**
- Removed HTML tags (e.g., <br>) and unnecessary characters.
- Tokenized text into words.
- Converted text to lowercase and removed stopwords.
- Vectorized text using TF-IDF for feature extraction.


---

## **Exploratory Data Analysis**

### **Key insights from the dataset:**
- Visualized word distributions using WordCloud.
- Examined sentiment polarity with bar charts and pie charts.
- Ensured balance in positive and negative sentiments.


---

## **Usage**

- Open the MoodLens web application in your browser.
- Enter a review or text in the input box and click "Analyze."
- View the sentiment result with a corresponding dynamic and engaging message.


## **Contact**

- [LinkedIn](https://www.linkedin.com/in/sambhaji-shinde-1679ab309/)
- [Instagram](https://www.instagram.com/sambhaji_26/)