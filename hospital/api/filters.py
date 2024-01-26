import django_filters as filters
from api.models import Doctor, Patient


class DoctorFilterSet(filters.FilterSet):
    last_name = filters.CharFilter(field_name='last_name',)

    class Meta:
        model = Doctor
        fields = {
            'last_name' : ['exact', 'icontains'],
            'first_name' : ['exact',],
            'specialization' : ['exact',]
        }


# class PatientFilterSet(filters.FilterSet):
#     last_name = filters.CharFilter(field_name='last_name',)
#
#     class Meta:
#         model = Patient
#         fields = {
#             'last_name' : ['exact', 'icontains'],
#             'first_name' : ['exact',]
#         }