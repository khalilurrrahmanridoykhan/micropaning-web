from django.db import models

class Form(models.Model):
    name = models.CharField(max_length=255)

class Field(models.Model):
    TEXT = 'text'
    NUMBER = 'number'
    DATE = 'date'
    FIELD_TYPES = [
        (TEXT, 'Text'),
        (NUMBER, 'Number'),
        (DATE, 'Date'),
    ]

    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    field_type = models.CharField(max_length=10, choices=FIELD_TYPES)

class UserFormSubmission(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
