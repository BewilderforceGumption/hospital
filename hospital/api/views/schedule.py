# from api.mixin import HospitalGenericViewSet
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import mixins, filters
# from api.serializers.patient import PatientListSerializer, PatientDetailedSerializer, PatientCreateOrUpdateSerializer
# # from api.filters import PatientFilterSet
#
#
# class PatientView(
#     HospitalGenericViewSet,
#     mixins.ListModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.CreateModelMixin,
#     mixins.DestroyModelMixin
# ):
#     lookup_field = 'id'
#
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_fields = ['gender']
#     search_fields = ['first_name', 'last_name']
#     # filterset_class = PatientFilterSet
#
#     def get_action_permissions(self):
#         if self.action in ('list', 'retrieve'):
#             self.action_permissions = ['view_patient', ]
#         elif self.action == 'create':
#             self.action_permissions = ['add_patient', ]
#         elif self.action == 'update':
#             self.action_permissions = ['change_patient', ]
#         elif self.action == 'destroy':
#             self.action_permissions = ['delete_patient', ]
#
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return PatientListSerializer
#         if self.action == 'retrieve':
#             return PatientDetailedSerializer
#         if self.action == 'create':
#             return PatientCreateOrUpdateSerializer
#         if self.action == 'update':
#             return PatientCreateOrUpdateSerializer
#
#     def get_queryset(self):
#         return Patient.objects.all()