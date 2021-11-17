from django.contrib import admin

from .models import Employee, EmploymentType, Department, BankDetails, LeaveType, Leave, JobListing, Application, ScheduledInterview, OfferLetter



admin.site.register(Employee)
admin.site.register(EmploymentType)
admin.site.register(Department)