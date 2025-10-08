from django.db import models

from django.conf import settings

class Application(models.Model):
    # Choices
    APPLICATION_TYPES = [
        ("NEW_ID", "New ID"),
        ("ID_RENEWAL", "ID Renewal"),
        ("BIRTH_CERTIFICATE", "Birth Certificate"),
    ]

    STATUS_CHOICES = [
        ("PENDING", "Pending Review"),
        ("READY", "Ready for Pickup"),
        ("REJECTED", "Rejected"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,  # one active application per resident
        on_delete=models.CASCADE,
        related_name="application"
    )
    application_type = models.CharField(max_length=20, choices=APPLICATION_TYPES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")

    # Common fields
    full_name = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    resident_address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    # Emergency contact (for NEW_ID)
    emergency_contact_name = models.CharField(max_length=255, blank=True, null=True)
    emergency_contact_phone = models.CharField(max_length=20, blank=True, null=True)

    # Specific to NEW_ID
    blood_group = models.CharField(max_length=5, blank=True, null=True)

    # Specific to ID Renewal
    existing_id_number = models.CharField(max_length=50, blank=True, null=True)
    reason_for_renewal = models.CharField(max_length=255, blank=True, null=True)

    # Specific to Birth Certificate
    child_full_name = models.CharField(max_length=255, blank=True, null=True)
    place_of_birth = models.CharField(max_length=100, blank=True, null=True)
    father_full_name = models.CharField(max_length=255, blank=True, null=True)
    mother_full_name = models.CharField(max_length=255, blank=True, null=True)
    birth_certificate_photo = models.FileField(
    upload_to="applications/birth_photos/",
    blank=True,
    null=True
)

    # Attachments (you can use FileField/ImageField)
    photo = models.FileField(upload_to="applications/photos/", blank=True, null=True)
    residence_proof = models.FileField(upload_to="applications/proofs/", blank=True, null=True)
    old_id_card = models.FileField(upload_to="applications/old_ids/", blank=True, null=True)
    hospital_proof = models.FileField(upload_to="applications/hospital_proofs/", blank=True, null=True)
    parent_id = models.FileField(upload_to="applications/parent_ids/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.application_type} ({self.status})"
