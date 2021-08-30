from django.db import models

from django.utils.translation import ugettext as _
# Create your models here.

class Product(models.Model):

    prdname = models.CharField(max_length=100, verbose_name=_('Name'))
    # category
    prddesc = models.TextField(verbose_name=_('Description'))
    prdprice = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_('Price'))
    prdcost = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_('Cost'))
    prdcreated = models.DateTimeField(verbose_name=_('Created At'))

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.prdname

class ProductImage(models.Model):
    prdiproduct = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('Product'))
    prdiProductImage = models.ImageField(upload_to='product/', verbose_name=_('Image'))

    def __str__(self):
        # this is id
        return str(self.prdiproduct)


class Category(models.Model):
    catname = models.CharField(max_length=50, verbose_name=_('Name'))
    # recursive relationship
    catparent = models.ForeignKey("self", limit_choices_to={'catparent__isnull':True}, on_delete=models.CASCADE, verbose_name=_('Main Category'), blank=True, null=True)
    catdesc = models.TextField(verbose_name=_('Description'))
    catimg = models.ImageField(upload_to = 'category/', verbose_name=_('Image'))

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.catname

class Product_Alternative(models.Model):

    palnproduct = models.ForeignKey(Product, verbose_name=_("Product"), on_delete=models.CASCADE, related_name='main_product')
    palnalternatives = models.ManyToManyField(Product, verbose_name=_("Alternatives"), related_name='alternative_produts')
    

    class Meta:
        verbose_name = 'Product Alternative'
        verbose_name_plural = 'Product Alternatives'

    def __str__(self):
        return str(self.palnproduct)

class Product_Accessories(models.Model):
    
    paccproduct = models.ForeignKey(Product, verbose_name=_("Product"), on_delete=models.CASCADE, related_name='mainAccessory_product')
    paccalternatives = models.ManyToManyField(Product, verbose_name=_("Accessories"), related_name='accessories_products')
    

    class Meta:
        verbose_name = 'Product Accessory'
        verbose_name_plural = 'Product Accessories'
    
    def __str__(self):
        return str(self.paccproduct)