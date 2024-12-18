# Generated by Django 5.1.3 on 2024-11-27 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bicycles', '0003_equipment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
            ],
            options={
                'verbose_name': 'тэг',
                'verbose_name_plural': 'тэги',
            },
        ),
    ]
