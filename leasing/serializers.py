from leasing.models import *
from rest_framework import serializers

class ChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        if data == '' and self.allow_blank:
            return ''
        for key, val in self._choices.items():
            if val.lower() == data:
                return key
        self.fail('invalid_choice', input=data)


class VehicleDetailsSerializer(serializers.ModelSerializer):
    vehicle_type = ChoiceField(choices=VehicleType.choices)

    class Meta:
        model = VehicleDetails
        fields = "__all__"