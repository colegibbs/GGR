from rest_framework import serializers
from .models import Listing

class ListingSerializer(serializers.ModelSerializer):
  class meta:
    fields = ("owner", "price", "year_built", "sq_footage", "stories", "beds", "baths", "address", "description", "created_at", "updated_at")
    model = Listing
