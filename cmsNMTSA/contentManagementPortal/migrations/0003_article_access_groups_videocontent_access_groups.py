# Generated by Django 5.1.2 on 2024-10-12 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentManagementPortal', '0002_accessgroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='access_groups',
            field=models.ManyToManyField(to='contentManagementPortal.accessgroup'),
        ),
        migrations.AddField(
            model_name='videocontent',
            name='access_groups',
            field=models.ManyToManyField(to='contentManagementPortal.accessgroup'),
        ),
    ]
