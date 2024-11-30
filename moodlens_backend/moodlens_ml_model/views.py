from django.shortcuts import render
from django.http import JsonResponse
import joblib
import os
from django.conf import settings
import sklearn
import re
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ReviewDataModel


model_path=os.path.join(settings.BASE_DIR, 'ml_models/sentiment_analysis_model.pkl')
tfidf_path=os.path.join(settings.BASE_DIR, 'ml_models/tfidf_vectorizer.pkl')

model = joblib.load(model_path)
vectorizer = joblib.load(tfidf_path)

def cleaning_user_text(text):
    text = re.sub(r'<br\s*/?>', ' ', text)
    text = re.sub(r'•|▪|➤|➔|-|\*', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower() 
    text = re.sub(r'\s+', ' ', text).strip()
    return text

@csrf_exempt
def MakePrediction(req):
    if req.method == "POST":

        body = json.loads(req.body)
        user_review = body.get('review')

        cleaned_text = cleaning_user_text(user_review)
        
        vectorized_text = vectorizer.transform([cleaned_text])
        sentiment = model.predict(vectorized_text)

        message="None"

        if sentiment == 1:
            message="Positive"
        else:
            message="Negative"

        sentiment = str(sentiment[0])

        data_saving=ReviewDataModel(User_Review=user_review, Cleaned_Review=cleaned_text, Sentiment=message, Model_Prediction=sentiment)
        data_saving.save()

        return JsonResponse({'sentiment': message})