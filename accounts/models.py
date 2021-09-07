from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext as _
import datetime
from django_countries.fields import CountryField
from django.utils.text import slugify
from django.urls import reverse

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_id')
    phone = models.CharField(max_length=15, blank=True, null=True)
    image = models.ImageField(_('Image'), upload_to = 'profile', blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    country = CountryField()
    slug = models.SlugField(blank=True, null=True)
    join = models.DateTimeField(_("Join Date"), default= datetime.datetime.now)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)
    
    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('accounts:profile_detail', kwargs={'user_slug': self.slug})

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user = instance
        )