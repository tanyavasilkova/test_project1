from django.db import models
from django.urls import reverse_lazy


class Note(models.Model):
    name = models.CharField("Заметка", max_length=30)
    text = models.TextField("Текст")

    def get_absolute_url(self):
        return reverse_lazy("note_detail_view", kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Заметка"
        verbose_name_plural = "Заметки"



