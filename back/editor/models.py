from django.db import models

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    url = models.TextField()

class InfoCard(models.Model):
    id = models.AutoField(primary_key=True)
    top = models.TextField()
    middle_number = models.IntegerField()
    middle_text = models.TextField(blank=True, null=True)
    bottom = models.TextField()