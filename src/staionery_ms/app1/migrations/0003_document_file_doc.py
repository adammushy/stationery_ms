# Generated by Django 4.0.4 on 2023-01-12 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_user_phone_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='file_doc',
            field=models.FileField(blank=True, null=True, upload_to='pdfs/'),
        ),
    ]
