# Generated by Django 3.2.9 on 2021-11-25 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('superadmin', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('linkedin_url', models.URLField()),
                ('phone_number', models.CharField(max_length=120)),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('education_obtained', models.CharField(blank=True, max_length=100, null=True)),
                ('graduation_year', models.CharField(blank=True, max_length=100, null=True)),
                ('desired_salary', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('experience', models.CharField(blank=True, max_length=500, null=True)),
                ('location', models.CharField(max_length=100)),
                ('date_available', models.DateField(auto_now=True)),
                ('cover_letter', models.TextField(blank=True, null=True)),
                ('status', models.CharField(default='pending', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('soft_delete', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduledInterview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interview_date', models.DateField()),
                ('interview_time_from', models.TimeField()),
                ('interview_time_to', models.TimeField()),
                ('content', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('soft_delete', models.BooleanField(default=False, null=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='human_resource.application')),
            ],
        ),
        migrations.CreateModel(
            name='OfferLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=200)),
                ('supervisor', models.CharField(max_length=200)),
                ('offer_start_date', models.DateField(auto_now=True)),
                ('offer_letter_content', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('soft_delete', models.BooleanField(default=False, null=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='human_resource.application')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='human_resource.department')),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positon', models.CharField(blank=True, max_length=100, null=True)),
                ('leave_date_from', models.DateField(blank=True, null=True)),
                ('leave_date_to', models.DateField(blank=True, null=True)),
                ('status', models.CharField(default='pending', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('soft_delete', models.BooleanField(default=False, null=True)),
                ('approved_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='human_resource.department')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_leave', to=settings.AUTH_USER_MODEL)),
                ('employment_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='human_resource.employmenttype')),
                ('leave_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='human_resource.leavetype')),
            ],
        ),
        migrations.CreateModel(
            name='JobListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('job_description', models.TextField()),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(max_length=100)),
                ('job_type', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=100)),
                ('salary', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('deadline', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('soft_delete', models.BooleanField(default=False, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='human_resource.department')),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employment_date', models.DateField(auto_now_add=True)),
                ('position', models.CharField(max_length=30)),
                ('status', models.BooleanField(default=True)),
                ('soft_delete', models.BooleanField(default=False, null=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employees', to='superadmin.company')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='human_resource.department')),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employmentinformation', to=settings.AUTH_USER_MODEL)),
                ('employment_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='human_resource.employmenttype')),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='job_listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='human_resource.joblisting'),
        ),
    ]
