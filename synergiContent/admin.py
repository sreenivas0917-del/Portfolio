from django.contrib import admin
from .models import Contact
from .models import ContactUs
from .models import QuickEnquiry
from .models import ResumeSubmission
from .models import CVSubmission
from .models import ConfidentialReport


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at',)


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at',)


@admin.register(QuickEnquiry)
class QuickEnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'type', 'created_at')
    search_fields = ('name', 'email', 'phone', 'type')
    list_filter = ('type', 'created_at')



@admin.register(ResumeSubmission)
class ResumeSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'position', 'submitted_at')
    search_fields = ('name', 'email', 'position')
    list_filter = ('submitted_at',)    


@admin.register(CVSubmission)
class CVSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'position', 'submitted_at')
    search_fields = ('name', 'email', 'position')
    list_filter = ('submitted_at',)




@admin.register(ConfidentialReport)
class ConfidentialReportAdmin(admin.ModelAdmin):
    list_display = ('category', 'reporter_name', 'reporter_email', 'submitted_at')
    list_filter = ('category', 'submitted_at')
    search_fields = ('reporter_name', 'reporter_email', 'category', 'details')
    readonly_fields = ('submitted_at',)