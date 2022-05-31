from django.db import models


class PriceCard(models.Model):

    pc_price = models.CharField(max_length=20, verbose_name='Цена')
    pc_description = models.CharField(max_length=200, verbose_name='Описание')

    class Meta:
        verbose_name = 'Цены'
        verbose_name_plural = 'Цены'

    def __str__(self):
        return self.pc_price


class PriceTable(models.Model):

    pt_title = models.CharField(max_length=50, verbose_name='Услуга')
    pt_new_price = models.CharField(max_length=20, verbose_name='Старая цена')
    pt_old_price = models.CharField(max_length=20, verbose_name='Новая цена')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.pt_title
