# Generated by Django 3.2.9 on 2021-11-25 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0003_alter_company_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='country',
            field=models.CharField(max_length=100),
        ),
    ]