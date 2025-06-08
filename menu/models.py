from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Category(models.Model):
    name = models.CharField(_("نام دسته بندی"), max_length=20)
    img = models.ImageField(_("تصویر"), upload_to="categories/")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("دسته بندی")
        verbose_name_plural = _("دسته بندی ها")

class Food(models.Model):
    name = models.CharField(_("نام غذا"), max_length=50)
    description = models.CharField(_("توضیحات"), max_length=200)
    img = models.ImageField(_("تصویر"), upload_to="foods/")
    price = models.IntegerField(_("قیمت"))
    rate = models.IntegerField(_("امتیاز"), default=0)
    is_active = models.BooleanField(_("فعال"), default=True)
    default_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="foods", default=1)

    class Meta:
        verbose_name = _("غذا")
        verbose_name_plural = _("غذا ها")

    def __str__(self):
        return self.name