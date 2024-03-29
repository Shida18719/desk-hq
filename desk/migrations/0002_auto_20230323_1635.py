# Generated by Django 3.2.18 on 2023-03-23 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('desk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='location',
            field=models.ForeignKey(blank=True, default='DESK HQ Brooklyn House (3 STONE AVENUE LONDON SE5 2AZ)', null=True, on_delete=django.db.models.deletion.CASCADE, to='desk.location'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='space_booking',
            field=models.ForeignKey(blank=True, default='Day WorkStation', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='space_booking', to='desk.service'),
        ),
    ]
