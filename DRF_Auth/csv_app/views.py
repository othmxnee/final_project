# views.py
from django.http import JsonResponse
from rest_framework import generics

from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import csv, io
from .models import Etudiant,Prof
from .serializers import EtudiantModelSerializer,ProfModelSerializer

class CSVUploadViewProf(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        if 'file' not in request.data:
            return Response({"error": "No file was provided."}, status=status.HTTP_400_BAD_REQUEST)

        file = request.data['file']
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.reader(decoded_file)

        # Skip the header row
        next(reader, None)

        # Check if all emails end with @esi-sba.dz
        for row in reader:
            _, email, _ = row
            if not email.endswith('@esi-sba.dz'):
                return Response({"error": "All emails must end with @esi-sba.dz"}, status=status.HTTP_400_BAD_REQUEST)

        # Reset the reader because it was exhausted in the check above
        file.seek(0)
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.reader(decoded_file)
        next(reader, None)  # Skip the header row again

        # Process CSV data
        for row in reader:
            full_name, email, matricule = row
            
            Prof.objects.update_or_create(
                matricule=matricule,
                defaults={
                    'full_name': full_name,
                    'email': email,
                    'password':  matricule
                }
            )

        return Response({"success": "File uploaded successfully"}, status=status.HTTP_201_CREATED)

class CSVUploadViewEtudiant(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        if 'file' not in request.data:
            return Response({"error": "No file was provided."}, status=status.HTTP_400_BAD_REQUEST)

        file = request.data['file']
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.reader(decoded_file)

        # Skip the header row
        next(reader, None)

        # Check if all emails end with @esi-sba.dz
        for row in reader:
            _, email, _ = row
            if not email.endswith('@esi-sba.dz'):
                return Response({"error": "All emails must end with @esi-sba.dz"}, status=status.HTTP_400_BAD_REQUEST)

        # Reset the reader because it was exhausted in the check above
        file.seek(0)
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.reader(decoded_file)
        next(reader, None)  # Skip the header row again

        # Process CSV data
        for row in reader:
            full_name, email, matricule = row
            
            Etudiant.objects.update_or_create(
                matricule=matricule,
                defaults={
                    'full_name': full_name,
                    'email': email,
                    'password':  matricule
                }
            )

        return Response({"success": "File uploaded successfully"}, status=status.HTTP_201_CREATED)




    #etudiant
class EtudiantView(generics.ListCreateAPIView):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantModelSerializer


class SingleEtudiantView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EtudiantModelSerializer
    def get_queryset(self):
        return Etudiant.objects.filter(pk = self.kwargs['pk'])
    
#prof

class ProfView(generics.ListCreateAPIView):
    queryset = Prof.objects.all()
    serializer_class = ProfModelSerializer


class SingleProfView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfModelSerializer
    def get_queryset(self):
        return Prof.objects.filter(pk = self.kwargs['pk'])