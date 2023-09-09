from django.db import models

# どんなフィールドがあるか適宜検索
class Task(models.Model):
    title = models.CharField('タイトル', max_length=30)
    description = models.TextField('説明', blank=True)
    deadline = models.DateField('〆切日')

    def __str__(self):
        return self.title