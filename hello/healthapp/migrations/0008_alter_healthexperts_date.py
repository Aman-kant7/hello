# Generated by Django 4.0.3 on 2022-03-11 08:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('healthapp', '0007_alter_patient_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthexperts',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]