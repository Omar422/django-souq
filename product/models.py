from django.db import models
from django.utils.translation import ugettext as _
from django.utils.text import slugify
from django.urls import reverse
# from django.core.urlresolvers import reverse

# Create your models here.

class Product(models.Model):

    prdname = models.CharField(max_length=100, verbose_name=_('Name'))
    prdcategory = models.ForeignKey('Category', verbose_name=_("Category"), on_delete=models.CASCADE, blank=True, null=True)
    prdbrand = models.ForeignKey("settings.Brand", verbose_name=_("Brand"), on_delete=models.CASCADE, blank=True, null=True)
    prddesc = models.TextField(verbose_name=_('Description'))
    prdimage = models.ImageField(upload_to='product/', verbose_name=_('Image'), blank=True, null=True)
    prdprice = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_('Price'))
    prddisprice = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_('Discount Price'))
    prdcost = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_('Cost'))
    prdslug = models.SlugField(verbose_name=_('Product URL') ,blank=True, null=True)
    prdisnew = models.BooleanField(default=True, verbose_name=_('New Product'))
    prdbestseller = models.BooleanField(default=False, verbose_name=_('Best Seller'))
    prdcreated = models.DateTimeField(verbose_name=_('Created At'))

    def save(self,*args, **kwargs):
        self.prdslug = slugify(self.prdname)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    # 
    def get_absolute_url(self):
        return reverse('products:product_detail', kwargs={'product_slug': self.prdslug})
    
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
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self) -> str:
        return self.catname

class Product_Alternative(models.Model):

    palnproduct = models.ForeignKey(Product, verbose_name=_("Product"), on_delete=models.CASCADE, related_name='main_product')
    palnalternatives = models.ManyToManyField(Product, verbose_name=_("Alternatives"), related_name='alternative_produts')
    

    class Meta:
        verbose_name = _('Product Alternative')
        verbose_name_plural = _('Product Alternatives')

    def __str__(self):
        return str(self.palnproduct)

class Product_Accessories(models.Model):
    
    paccproduct = models.ForeignKey(Product, verbose_name=_("Product"), on_delete=models.CASCADE, related_name='mainAccessory_product')
    paccalternatives = models.ManyToManyField(Product, verbose_name=_("Accessories"), related_name='accessories_products')
    

    class Meta:
        verbose_name = _('Product Accessory')
        verbose_name_plural = _('Product Accessories')
    
    def __str__(self):
        return str(self.paccproduct)