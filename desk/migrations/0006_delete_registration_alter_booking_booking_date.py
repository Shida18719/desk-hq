# Generated by Django 4.1.7 on 2023-04-06 14:18

import datetime
import desk.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desk', '0005_rename_enquires_enquiry_alter_booking_booking_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Registration',
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 7, 14, 18, 37, 712810), validators=[desk.models.validate_date]),
        ),
    ]