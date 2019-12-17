# Generated by Django 2.2.8 on 2019-12-17 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125, unique=True, verbose_name='Name')),
                ('description', models.CharField(max_length=500, verbose_name='Description')),
                ('category', models.CharField(choices=[(1, 'Convenience Goods'), (2, 'Shopping Goods'), (3, 'Specialty Goods')], max_length=125, verbose_name='Category')),
                ('pictures', models.ImageField(upload_to='project_name / media / products / images /', verbose_name='Pictures')),
                ('amount', models.IntegerField(default=0, verbose_name='Amount')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Price')),
                ('production_date', models.DateField(auto_now_add=True, verbose_name='Production Date')),
                ('isnew', models.BooleanField(default=False, verbose_name='Is New')),
                ('cerificate', models.FileField(null=True, upload_to='project_name / media / products / files /', verbose_name='Certificate')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=1, null=True, verbose_name='Rating')),
                ('detailed_view_link', models.CharField(max_length=300, null=True, verbose_name='URL')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'company_products',
                'ordering': ['name'],
            },
        ),
    ]
