from django.db import models


class UPhoto(models.Model):
    comment = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.comment
