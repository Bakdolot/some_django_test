from rest_framework import serializers

from .utils import brackets_validator


class SomeSerializer(serializers.Serializer):
    math_string = serializers.CharField()

    def is_valid_string(self) -> bool:
        return brackets_validator(self.data["math_string"])


class MainResponseSerializer(serializers.Serializer):
    is_valid = serializers.BooleanField()
