from django.urls import path
from .views import home, signup,dashboard
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('', home),
    path('signup/', signup),
    path('login/', TokenObtainPairView.as_view()), 
      path('dashboard/', dashboard),  
]
