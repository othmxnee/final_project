from rest_framework import serializers
from .models import Person,Etudiant,Prof

class EtudiantModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = '__all__'

class ProfModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prof
        fields = '__all__'