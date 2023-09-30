from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    discription = models.TextField(blank=True)
    imgage = models.ImageField(upload_to='category_image',blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('storeapp:products_by_Category', args=[self.slug])




    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    price = models.DecimalField(default=0, decimal_places=2,max_digits=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='product_image')
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('storeapp:prodcadetail', args=[self.category.slug, self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return '{}'.format(self.name)
