# Generated by Django 3.2.9 on 2021-11-17 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human_resource', '0002_auto_20211117_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='gross_salary',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='id_number',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='personal_email',
            field=models.EmailField(max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='work_email',
            field=models.EmailField(max_length=50, null=True, unique=True),
        ),
    ]
