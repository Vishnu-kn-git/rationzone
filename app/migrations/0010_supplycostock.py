# Generated by Django 4.2.16 on 2024-11-26 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplycostock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.CharField(blank=True, max_length=20, null=True)),
                ('quantity', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]