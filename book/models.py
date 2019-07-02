from django.db import models


# Create your models here.
class GameInfo(models.Model):
    TYPE_CHOICES = ((0, 'MOBA'), (1, 'FPS'), (2, 'RPG'))
    models.Man
    gname = models.CharField(max_length = 20, verbose_name = '游戏名')
    gtype = models.SmallIntegerField(choices = TYPE_CHOICES,
                                     default = 0, verbose_name = '游戏类型')
    gpub_date = models.DateField(verbose_name = '发布时间')
    gpalyer = models.IntegerField(default = 0, verbose_name = '玩家数量')
    gis_delete = models.BooleanField(default = 0, verbose_name = '逻辑删除')

    class Meta:
        db_table = 'tb_games'
        verbose_name = '游戏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.gname


class HeroInfo(models.Model):
    GENDER_CHOICES = ((0, 'MAN'), (1, 'WOMEN'))

    hname = models.CharField(max_length = 20, verbose_name = '英雄名')
    hgender = models.SmallIntegerField(choices = GENDER_CHOICES,
                                       default = 0, verbose_name = '性别')
    hskill = models.CharField(max_length = 20, verbose_name = '技能')
    hgame = models.ForeignKey(GameInfo, on_delete = models.CASCADE,
                              verbose_name = '所属游戏')
    his_delete = models.BooleanField(default = 0, verbose_name = '逻辑删除')

    class Meta:
        db_table = 'tb_heros'
        verbose_name = '英雄'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hname
