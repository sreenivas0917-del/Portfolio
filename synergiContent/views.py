from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from .models import ContactUs
from .models import QuickEnquiry
from .models import CVSubmission
from .models import ResumeSubmission
from .models import ConfidentialReport



# Home page view
def index(request):
    return render(request, 'index.html')  
    # 👆 looks for index.html inside myapp/templates/myapp/

def services(request):
    return render(request, 'services.html')      


def about(request):
    return render(request, 'about.html')   


def contactPage(request):
    return render(request, 'contact.html')   


def faq(request):
    return render(request, 'faq.html')   

def blog(request):
    return render(request, 'blog.html')   


def career(request):
    return render(request, 'career.html')   



def termsAndconditions(request):
    return render(request, 'terms&conditions.html')   

def privacyPolicy(request):
    return render(request, 'privacyPolicy.html')   

def LoanRecoveryServices(request):
    return render(request, 'LoanRecoveryServices.html')   


def CustomerCareAndSupport(request):
    return render(request, 'CustomerCareAndSupport.html')   


def EmailAndChatSupport(request):
    return render(request, 'EmailAndChatSupport.html')  



def TelicallingAndLeadGeneration(request):
    return render(request, 'TelicallingAndLeadGeneration.html')   

def DataManagementAndAnalytics(request):
    return render(request, 'DataManagementAndAnalytics.html')   


def AddPage(request):
    return render(request, 'AddPage.html')   


def compliances(request):
    return render(request, 'compliances.html')   


def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect("index")  # Redirect back to the contact page

    return render(request, "index.html")




def contact_us_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save to database
        ContactUs.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        messages.success(request, "Thank you! Our team will get back to you shortly.")
        return redirect('contact_us')  # redirect to home page after successful submission

    return render(request, 'contact.html')




def quick_enquiry_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        enquiry_type = request.POST.get('type')
        message = request.POST.get('message')

        QuickEnquiry.objects.create(
            name=name,
            email=email,
            phone=phone,
            type=enquiry_type,
            message=message
        )

        messages.success(request, "Your enquiry has been submitted successfully! We'll get back to you soon.")
        return redirect('quick_enquiry')  # redirect to same page after submission

    return render(request, 'quick_enquiry.html')




def submit_resume_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        position = request.POST.get('position')
        message = request.POST.get('message')
        resume_file = request.FILES.get('resume')

        # Save to database
        ResumeSubmission.objects.create(
            name=name,
            email=email,
            phone=phone,
            position=position,
            message=message,
            resume=resume_file
        )

        messages.success(request, "Your resume has been submitted successfully! We’ll review and get back to you if shortlisted.")
        return redirect('submit_resume')  # redirect to same page

    return render(request, 'career.html')




def submit_cv_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        position = request.POST.get('position')
        resume = request.FILES.get('resume')

        CVSubmission.objects.create(
            name=name,
            email=email,
            position=position,
            resume=resume
        )

        messages.success(request, "Your CV has been submitted successfully! Thank you for your interest.")
        return redirect('submit_cv')  # Redirect back to same page or careers page

    return render(request, 'careers.html')






def submit_report_view(request):
    if request.method == 'POST':
        reporter_name = request.POST.get('reporter_name')
        reporter_email = request.POST.get('reporter_email')
        reporter_phone = request.POST.get('reporter_phone')
        category = request.POST.get('category')
        details = request.POST.get('details')
        evidence = request.FILES.get('evidence')

        ConfidentialReport.objects.create(
            reporter_name=reporter_name,
            reporter_email=reporter_email,
            reporter_phone=reporter_phone,
            category=category,
            details=details,
            evidence=evidence
        )

        messages.success(request, "Your confidential report has been submitted successfully. Thank you for reporting.")
        return redirect('submit_report')  # Replace with your current page or modal reload

    return render(request, 'report_form.html')



# def contact_us_view(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')

#         # Save to database
#         ContactUs.objects.create(
#             name=name,
#             email=email,
#             subject=subject,
#             message=message
#         )

#         messages.success(request, "Thank you! Our team will get back to you shortly.")
#         return redirect('contact')  # redirect to same page after successful submission

#     return render(request, 'contact.html')

