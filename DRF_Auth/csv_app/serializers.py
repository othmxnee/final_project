from rest_framework import serializers
from .models import Person,Etudiant,Prof

class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
class EtudiantModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = '__all__'

class ProfModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prof
        fields = '__all__'