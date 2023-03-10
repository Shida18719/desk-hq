# Generated by Django 3.2.18 on 2023-03-10 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('desk', '0005_alter_booking_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='location_address',
        ),
        migrations.AlterField(
            model_name='booking',
            name='location',
            field=models.ForeignKey(default='DESK HQ Brooklyn House (3 STONE AVENUE LONDON SU5 2AZ)', on_delete=django.db.models.deletion.CASCADE, to='desk.location'),
        ),
        migrations.AlterField(
            model_name='location',
            name='location_name',
            field=models.CharField(choices=[('DESK HQ Brooklyn House (3 STONE AVENUE LONDON SU5 2AZ)', 'DESK HQ Brooklyn House (3 STONE AVENUE LONDON SU5 2AZ)'), ('DESK HQ Dockyard Place (55 PARADE STREET LONDON E20 3YB)', 'DESK HQ Dockyard Place (55 PARADE STREET LONDON E20 3YB)')], default='DESK HQ Brooklyn House (3 STONE AVENUE LONDON SU5 2AZ)', max_length=200),
        ),
    ]
