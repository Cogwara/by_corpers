from django.contrib.auth.models import User
from django.db import models


class Registration(models.Model):
    corper = models.ForeignKey(User)
    state_code = models.CharField(max_length=12)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.state_code
