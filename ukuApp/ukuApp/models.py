from django.db import models

class Agreement(models.Model):
    title_text = models.CharField(max_length=100)
    desc_date = models.TextField(max_length=1024)

class Activity(models.Model):
    agreement = models.Field(Agreement)
    title_text = models.CharField(max_length=100)