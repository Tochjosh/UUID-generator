from django.urls import path
from UUID_gen_app.views import DataAPIView

urlpatterns = [
    path('', DataAPIView.as_view(), name='index')
]
