# Generated by Django 4.0.4 on 2023-01-12 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_document_file_doc'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('printed', 'printed'), ('taken', 'taken')], default='pending', max_length=20),
        ),
    ]
