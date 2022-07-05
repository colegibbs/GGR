from rest_framework import generics
from .models import Listing
from .serializers import ListingSerializer

class ListingList(generics.ListCreateAPIView):
  queryset = Listing.objects.all()
  serializer_class = ListingSerializer

class ListingDeatil(generics.RetrieveUpdateDestroyAPIView):
  queryset = Listing.objects.all()
  serializer_class = ListingSerializer