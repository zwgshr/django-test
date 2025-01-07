from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)  # 书名
    author = models.CharField(max_length=100)  # 作者
    published_date = models.DateField()  # 出版日期
    isbn = models.CharField(max_length=13, unique=True)  # ISBN
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 价格

    def __str__(self):
        return self.title
