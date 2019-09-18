from django.db import models
from django.urls import reverse_lazy


class Category(models.Model):
    name = models.CharField('Категория', max_length=30)

    def get_absolute_url(self):
        return reverse_lazy("category_detail_view", kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"




