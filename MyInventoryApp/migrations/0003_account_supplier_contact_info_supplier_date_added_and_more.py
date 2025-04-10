# Generated by Django 5.1.7 on 2025-04-09 10:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyInventoryApp', '0002_supplier_city_supplier_country_supplier_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='supplier',
            name='contact_info',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplier',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='location',
            field=models.CharField(default='Unknown', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplier',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
