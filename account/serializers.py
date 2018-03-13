from rest_framework import serializers
from account.models import Account

class AccountSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    atype = serializers.CharField(max_length=24)

    def create(self, validated_data):
        return Account.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.atype = validated_data.get('name', instance.name)
        instance.save()
        return instance
