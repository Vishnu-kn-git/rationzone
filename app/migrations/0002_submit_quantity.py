# Generated by Django 4.2.16 on 2024-10-16 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submit',
            name='quantity',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
