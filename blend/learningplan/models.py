from django.db import models

# Create your models here.
class LearningPlan(models.Model):
    title = models.CharField(max_length=128, default="NULL")