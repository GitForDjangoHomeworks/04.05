# Generated by Django 4.1.5 on 2023-06-13 10:59

from django.db import migrations, models
import django.db.models.deletion
import precise_bbcode.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Название категории')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='category', verbose_name='Картина')),
                ('document', models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d/', verbose_name='Документы')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='products/%d%m%Y', verbose_name='Картина')),
                ('description', models.CharField(max_length=200, verbose_name='Описание')),
                ('order', models.PositiveSmallIntegerField(db_index=True, default=0)),
            ],
            options={
                'verbose_name': 'Картина Продукта',
                'verbose_name_plural': 'Картины продукта',
            },
        ),
        migrations.CreateModel(
            name='SingleProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('initial_price', models.BigIntegerField(verbose_name='Цена')),
                ('discount', models.PositiveIntegerField(blank=True, verbose_name='Процент скидки')),
                ('end_price', models.PositiveBigIntegerField(editable=False, verbose_name='Цена с учетом скидки')),
                ('number_products', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Количество товаров')),
                ('in_store', models.BooleanField(default=True, verbose_name='Доступен')),
                ('order', models.SmallIntegerField(db_index=True, default=0)),
                ('_content_rendered', models.TextField(blank=True, editable=False, null=True)),
                ('content', precise_bbcode.fields.BBCodeTextField(blank=True, no_rendered_field=True, null=True, verbose_name='Содержание')),
                ('document', models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d/', verbose_name='Документы')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.category', verbose_name='Категория товара')),
                ('images', models.ManyToManyField(blank=True, to='products.productimage', verbose_name='Картины')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['order', 'name'],
            },
        ),
    ]
