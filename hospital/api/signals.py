import datetime
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver
from .models import Visit, Notification, Doctor, Patient


@receiver(post_save, sender=Visit)
def notify_on_new_visit(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            sender=instance.patient.user,
            recipient=instance.schedule.doctor.user,
            message=f'Новый визит запланирован на {instance.schedule.timestamp_start}',
            notification_type=Notification.VISIT_CREATED
        )


@receiver(pre_save, sender=Visit)
def notify_on_canceled_visit(sender, instance, created, **kwargs):
    if instance.status == Visit.CANCELED:
        Notification.objects.create(
            sender=instance.patient.user,
            recipient=instance.schedule.doctor.user,
            message='Визит отменен',
            notification_type=Notification.VISIT_CANCELED
        )


@receiver(pre_delete, sender=Doctor)
def notify_on_doctor_delete(sender, instance, **kwargs):
    upcoming_visits_users_id = Visit.objects.filter(
        schedule__timestamp_start__gte=datetime.datetime.now(),
        schedule__doctor=instance
    ).values_list('patient__user_id', flat=True)
    for user_id in upcoming_visits_users_id:
        Notification.objects.create(
            sender=instance.user,
            recipient_id=user_id,
            message=f'Врач {instance.full_name} удален, все связанные визиты и расписания также удалены',
            notification_type=Notification.OTHER
        )


@receiver(pre_delete, sender=Patient)
def delete_related_visits(sender, instance, **kwargs):
    related_visits = Visit.objects.filter(patient=instance)
    for visit in related_visits:
        Notification.objects.create(
            sender=instance.user,
            recipient_id=visit.schedule.doctor.user,
            message=f'Пациент {instance.full_name} удален, связанный визит также удален',
            notification_type=Notification.OTHER
        )