# Generated by Django 5.1.3 on 2024-12-01 16:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bicycles', '0008_sizes_bicycle_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название категории')),
            ],
            options={
                'verbose_name': 'категория товара',
                'verbose_name_plural': 'категории товара',
            },
        ),
        migrations.CreateModel(
            name='Have',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('have', models.CharField(max_length=50, verbose_name='определение')),
            ],
            options={
                'verbose_name': 'наличие',
                'verbose_name_plural': 'наличия',
            },
        ),
        migrations.CreateModel(
            name='MaterialRams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rams', models.CharField(max_length=100, verbose_name='материал')),
            ],
            options={
                'verbose_name': 'материал',
                'verbose_name_plural': 'материалы рам',
            },
        ),
        migrations.AddField(
            model_name='bicycle',
            name='category_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='bicycles_product', to='bicycles.categoryproduct'),
        ),
        migrations.AddField(
            model_name='bicycle',
            name='have',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bicycles.have'),
        ),
        migrations.CreateModel(
            name='Characters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100, verbose_name='цвет')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='год')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bicycles.country')),
                ('edition', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bicycles.from')),
                ('material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bicycles.materialrams')),
            ],
            options={
                'verbose_name': 'характеристика',
                'verbose_name_plural': 'характеристики',
            },
        ),
        migrations.AddField(
            model_name='bicycle',
            name='material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bicycles.materialrams'),
        ),
    ]