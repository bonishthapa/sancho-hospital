# Generated by Django 4.0.4 on 2022-05-21 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_nurse'),
    ]

    operations = [
        migrations.AddField(
            model_name='nurse',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='nurse'),
        ),
    ]
