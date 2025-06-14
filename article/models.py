from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.
class Article(models.Model):
    title=models.CharField(_("عنوان"), max_length=100)
    summary=models.CharField(_("خلاصه"), max_length=500)
    description=models.TextField(_("توضیحات"))
    date=models.DateTimeField(_("زمان انتشار"), auto_now=False, auto_now_add=True)
    update=models.DateTimeField(_("زمان ویرایش"), auto_now=True, auto_now_add=False)
    img=models.ImageField(_("تصویر"), upload_to="article_images/", default="static/images/profile.jpg")
    author=models.ForeignKey(get_user_model(), verbose_name=_("نویسنده"), on_delete=models.CASCADE , related_name='articles')
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Article_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    article=models.ForeignKey("Article", on_delete=models.CASCADE , related_name='comments')
    comment=models.TextField(_("کامنت"))
    writer=models.ForeignKey(get_user_model(), verbose_name=_("نویسنده"), on_delete=models.CASCADE)