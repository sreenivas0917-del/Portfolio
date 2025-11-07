from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contactPage/', views.contactPage, name='contactPage'),
    path('faq/', views.faq, name='faq'),
    path('blog/', views.blog, name='blog'),
    path('career/', views.career, name='career'),
    path('terms&conditions/', views.termsAndconditions, name='terms&conditions'),
    path('privacyPolicy/', views.privacyPolicy, name='privacyPolicy'),
    path('LoanRecoveryServices/', views.LoanRecoveryServices, name='LoanRecoveryServices'),
    path('CustomerCareAndSupport/', views.CustomerCareAndSupport, name='CustomerCareAndSupport'),
    path('EmailAndChatSupport/', views.EmailAndChatSupport, name='EmailAndChatSupport'),
    path('TelicallingAndLeadGeneration/', views.TelicallingAndLeadGeneration, name='TelicallingAndLeadGeneration'),
    path('DataManagementAndAnalytics/', views.DataManagementAndAnalytics, name='DataManagementAndAnalytics'),
    path('AddPage/', views.AddPage, name='AddPage'),
       path('compliances/', views.compliances, name='compliances'),
       path('contact/', views.contact_view, name='contact'),
        path('contact-us/', views.contact_us_view, name='contact_us'),
          path('quick-enquiry/', views.quick_enquiry_view, name='quick_enquiry'),
          path('career/apply/', views.submit_resume_view, name='submit_resume'),
           path('career/submit_cv/', views.submit_cv_view, name='submit_cv'),
           path('report/submit/', views.submit_report_view, name='submit_report'),
]
