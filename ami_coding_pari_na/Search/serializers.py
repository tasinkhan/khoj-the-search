from rest_framework import serializers
from Search.models import Search

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields=['user_id','input_values','timestamp']