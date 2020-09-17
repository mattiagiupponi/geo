from rest_framework import serializers

from coordinates.models import RequestHistory, Coordinate


class RequestHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RequestHistory
        fields = ['timestamp', 'request', 'x_axes', 'y_axes']


class ClosesPointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coordinate
        fields = ['']