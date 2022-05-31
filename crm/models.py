from django.db import models


class SliderCrm(models.Model):

    sl_img = models.ImageField(upload_to='static/img')
    sl_title = models.CharField(max_length=50, verbose_name='Описание')
    sl_text = models.CharField(max_length=200, verbose_name='Текст')
    sl_css = models.CharField(max_length=20, null=True, default='-', verbose_name='Slider_CSS')

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'

    def __str__(self):
        return self.sl_title
