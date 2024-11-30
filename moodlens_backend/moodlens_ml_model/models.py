from django.db import models

class ReviewDataModel(models.Model):
    User_Review = models.TextField()
    Cleaned_Review = models.TextField()
    Sentiment = models.CharField(max_length=20)
    Model_Prediction = models.CharField(max_length=20)

    def __str__(self):
        # return self.review[:50]  
        return self.User_Review
