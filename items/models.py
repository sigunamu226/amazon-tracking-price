from django.db import models

from main.settings import IMAGE_DIR

# Create your models here.

class Item(models.Model):
    """
    商品モデル
    """

    name = models.CharField('商品名', max_length=500, db_index=True)
    image = models.ImageField(
        '商品画像', upload_to=IMAGE_DIR, db_index=True)
    now_price = models.CharField('現在の価格', max_length=50, db_index=True)
    hope_price = models.CharField('希望価格', max_length=50, db_index=True)
    recent_average = models.CharField('直近の平均価格', max_length=50, db_index=True, null=True, blank=True)
    fluctuating_value = models.CharField('変動値', max_length=50, db_index=True, null=True, blank=True)
    url = models.CharField('URL', max_length=1000, db_index=True)

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品マスタ'

    def __str__(self):
        return self.name