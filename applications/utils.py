# utils.py
from django.core.mail import send_mail
from django.conf import settings

def send_status_update_email(application):
    subject = f"Application Status Updated"
    message = (
        f"Dear {application.user.username},\n\n"
        f"Your application for {application.get_application_type_display()} "
        f"has been updated to {application.get_status_display()}.\n\n"
        f"Best regards,\nKebele Office"
    )

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [application.user.email],
        fail_silently=False
    )
