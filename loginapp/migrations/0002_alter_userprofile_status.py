# Generated by Django 4.2.16 on 2024-10-22 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'Active'), ('DEACTIVE', 'Deactive')], max_length=20),
        ),
    ]