from rest_framework import serializers


def validate_positive_integer(value):
    if value <= 0:
        raise serializers.ValidationError("Value must be a positive integer.")
    return value
#  def validate positive value
