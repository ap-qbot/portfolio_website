from django.urls import path
from .views import PortfolioView, ProjectDetailView

urlpatterns = [
    path('', PortfolioView.as_view(), name='home'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
]