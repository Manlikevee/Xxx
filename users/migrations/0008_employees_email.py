# Generated by Django 4.2.5 on 2024-04-23 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_visitorslog_reason_visitorslog_visitation_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='email',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
