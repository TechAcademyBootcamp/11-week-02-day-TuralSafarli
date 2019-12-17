from django.db import models

SUBJECTS = ((1, 'Convenience Goods'), (2, 'Shopping Goods'), (3, 'Specialty Goods'))

# Create your models here.

class Product(models.Model):

    """ Bu class Product Table-ni yaradacaq """
    name=models.CharField('Name',max_length=125 , unique=True)
    description=models.CharField('Description',max_length=500)
    category=models.CharField('Category',max_length=125,choices=SUBJECTS,default=1)
    pictures=models.ImageField('Pictures',upload_to= 'project_name / media / products / images /' )
    amount=models.IntegerField('Amount',default=0)
    price=models.DecimalField('Price',max_digits=5,decimal_places=2)
    production_date=models.DateField('Production Date',auto_now_add=True)
    isnew=models.BooleanField('Is New',default=False)
    cerificate=models.FileField('Certificate',upload_to='project_name / media / products / files /',null=True,blank=True)
    rating=models.DecimalField('Rating',max_digits=1,decimal_places=1,null=True,blank=True)
    detailed_view_link=models.CharField('URL',max_length=300,null=True,blank=True)



    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'company_products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']

    def __str__(self):
        return self.name