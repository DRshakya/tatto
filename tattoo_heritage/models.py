from django.db import models
import uuid

# Create your models here.

class Artist(models.Model):
    a_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    a_name = models.CharField(max_length=120)
    a_img = models.ImageField(upload_to='artists', blank=True)
    a_contact = models.CharField(max_length=100, blank=True)
    a_email = models.EmailField(blank=True)
    a_des = models.CharField(max_length=1000, default="This is tattoo artist.")
    a_fb = models.URLField(blank=True)
    a_insta =models.URLField(blank=True)

    def __str__(self):
        return self.a_name

class artist_work(models.Model):
    w_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    a_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    w_img = models.ImageField(upload_to='work', blank=False)

    def __str__(self):
        return self.a_id.a_name

class gallery1(models.Model):
    g1_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    g1_img = models.ImageField(upload_to='gallery1', blank=True)

    def __str__(self):
        return str(self.g1_img)





