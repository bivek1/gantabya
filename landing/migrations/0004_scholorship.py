# Generated by Django 5.0.2 on 2024-03-14 10:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_kyc_seen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scholorship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_scholorship', to='landing.course')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_scholorship', to='landing.customer')),
            ],
        ),
    ]
