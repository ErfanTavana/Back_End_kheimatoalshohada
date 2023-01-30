from django.db import models
from django.contrib.auth.models import User

class CodeLogin(models.Model):
    username = models.CharField(max_length=11)
    verification_code = models.CharField(max_length=6)
    expiration_date = models.TimeField(blank=True)
    def __str__(self):
        return f"{self.username} - {self.verification_code}"