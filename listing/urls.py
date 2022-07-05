from django.urls import path
from .views import ListingList, ListingDeatil

urlpatterns = [
  path("", ListingList.as_view(), name="listing_list"),
  path("<int:pk>/", ListingDeatil.as_view(), name="listing_detail")
]