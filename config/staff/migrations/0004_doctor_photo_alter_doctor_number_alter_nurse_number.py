# Generated by Django 4.0.4 on 2022-05-21 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_nurse_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='doctor'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='number',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='nurse',
            name='number',
            field=models.IntegerField(max_length=10),
        ),
    ]
