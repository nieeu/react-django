from django.urls import path
from .views import RoomView

# from .views import main

# urlpatterns = [
#     path('home', main),
#     path('',main) # we can have multiple end points
#     # now we can see hello with ".../api/home" or ".../api"
# ]

urlpatterns = [
    path('home', RoomView.as_view())
]