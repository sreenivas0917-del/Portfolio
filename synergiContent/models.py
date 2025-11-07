from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    


class QuickEnquiry(models.Model):
    ENQUIRY_CHOICES = [
        ('Collections Partnership', 'Collections Partnership'),
        ('Technology Integration', 'Technology Integration'),
        ('Careers', 'Careers'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=100, choices=ENQUIRY_CHOICES, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Quick Enquiry"
        verbose_name_plural = "Quick Enquiries"

    def __str__(self):
        return f"{self.name} - {self.type or 'General'}"
    



class ResumeSubmission(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    position = models.CharField(max_length=255)
    resume = models.FileField(upload_to='resumes/')  # stores file under MEDIA_ROOT/resumes/
    message = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.position}"
    


class CVSubmission(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    position = models.CharField(max_length=255, blank=True, null=True)
    resume = models.FileField(upload_to='cv_uploads/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.position or 'N/A'})"



class ConfidentialReport(models.Model):
    CATEGORY_CHOICES = [
        ("Data Breach / Security Incident", "Data Breach / Security Incident"),
        ("Ethics / Misconduct", "Ethics / Misconduct"),
        ("Harassment / Discrimination", "Harassment / Discrimination"),
        ("Fraud / Financial Irregularity", "Fraud / Financial Irregularity"),
        ("Other", "Other"),
    ]

    reporter_name = models.CharField(max_length=255, blank=True, null=True)
    reporter_email = models.EmailField(blank=True, null=True)
    reporter_phone = models.CharField(max_length=20, blank=True, null=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    details = models.TextField()
    evidence = models.FileField(upload_to='confidential_reports/', blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.reporter_name or 'Anonymous'}"
