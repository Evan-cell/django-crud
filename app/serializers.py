from rest_framework import serializers

from .models import Todos


class todosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = '__all__'