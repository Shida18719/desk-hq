# Generated by Django 3.2.18 on 2023-03-10 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('desk', '0004_auto_20230310_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='location',
            field=models.ForeignKey(default='DESK HQ Brooklyn House', on_delete=django.db.models.deletion.CASCADE, to='desk.location'),
        ),
    ]