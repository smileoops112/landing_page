from django.db import models


class StatusCms(models.Model):

    status_name = models.CharField(max_length=200, verbose_name='Названия статуса')

    class Meta:
        verbose_name = 'статус'
        verbose_name_plural = 'статусы'

    def __str__(self):
        return self.status_name


class Order(models.Model):

    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=50, verbose_name='Имя')
    order_phone = models.CharField(max_length=20, verbose_name="Телефон")
    order_status = models.ForeignKey(StatusCms, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.order_name


class CommentCms(models.Model):

    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заявка')
    comment = models.TextField(verbose_name='Коментарий')
    comment_dt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return self.comment


