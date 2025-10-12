from django.core.mail import send_mail, BadHeaderError
from smtplib import SMTPException
from django.conf import settings

def send_status_update_email(application):
    subject = f"Application Status Updated"
    message = (
        f"Dear {application.user.username},\n\n"
        f"Your application for {application.get_application_type_display()} "
        f"has been updated to {application.get_status_display()}.\n\n"
        f"Best regards,\nKebele Office"
    )

    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [application.user.email],
            fail_silently=False
        )
    except (SMTPException, BadHeaderError) as e:
        print(f"⚠️ Failed to send email: {e}")
