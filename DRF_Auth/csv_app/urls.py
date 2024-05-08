from django.urls import path
from .views import CSVUploadViewProf, CSVUploadViewEtudiant
from . import views

urlpatterns = [
    path('upload-etudiant/', CSVUploadViewEtudiant.as_view(), name='upload-csv'),
    path('upload-prof/', CSVUploadViewProf.as_view(), name='upload-csv'),


    path('etudiant/',views.EtudiantView.as_view()),
    path('etudiant/<int:pk>/',views.SingleEtudiantView.as_view()),
    path('prof/',views.ProfView.as_view()),
    path('prof/<int:pk>/',views.SingleProfView.as_view()),
    
]
