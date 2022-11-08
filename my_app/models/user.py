from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    detail = models.CharField(max_length=300)

    def __str__(self):
        return self.name + ' ' + self.email
