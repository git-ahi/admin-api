# Generated by Django 3.2.9 on 2021-11-15 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='national_id',
            field=models.IntegerField(null=True, verbose_name='National Id or passport'),
        ),
    ]
