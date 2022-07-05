from django.db import models
from django.contrib.auth import get_user_model

class Listing(models.Model):
  owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  price = models.IntegerField()
  year_built = models.IntegerField()
  sq_footage = models.IntegerField()
  stories = models.IntegerField()
  beds = models.IntegerField()
  baths = models.IntegerField()
  address = models.CharField(max_length=64)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name