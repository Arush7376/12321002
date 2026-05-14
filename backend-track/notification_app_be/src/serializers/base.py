from rest_framework import serializers


class EmptySerializer(serializers.Serializer):
    """Use for endpoints that do not require request body input."""

    pass
