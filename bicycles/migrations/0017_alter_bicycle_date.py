# Generated by Django 5.1.3 on 2024-12-10 13:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bicycles', '0016_alter_bicycle_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bicycle',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата публикации'),
        ),
    ]