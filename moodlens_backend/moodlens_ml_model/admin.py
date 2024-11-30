from django.contrib import admin
from .models import ReviewDataModel

# Register your models here.
class ReviewDataAdmin(admin.ModelAdmin):
    list_display=('User_Review', 'Cleaned_Review', 'Sentiment', 'Model_Prediction')

admin.site.register(ReviewDataModel,ReviewDataAdmin)
