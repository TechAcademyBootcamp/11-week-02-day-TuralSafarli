# Generated by Django 2.2.8 on 2019-12-17 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20191217_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cerificate',
            field=models.FileField(blank=True, null=True, upload_to='project_name / media / products / files /', verbose_name='Certificate'),
        ),
        migrations.AlterField(
            model_name='product',
            name='detailed_view_link',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=1, null=True, verbose_name='Rating'),
        ),
    ]
