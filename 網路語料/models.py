import json

from django.db import models
from django.forms.models import ModelForm


class 語料表(models.Model):
    收錄時間 = models.DateField(auto_now_add=True)
    上尾修改時間 = models.DateField(auto_now=True)

    華語內容 = models.TextField(blank=True)
    華語來源 = models.TextField(blank=True)
    臺語內容 = models.TextField()
    臺語來源 = models.TextField(default=json.dumps({
        '名': '',
        '網址': 'http://',
    }, indent=2, ensure_ascii=False, sort_keys=True))
    文本內容 = models.TextField()
    音標內容 = models.TextField()
    文本音標來源 = models.TextField()

    備註 = models.CharField(max_length=200, blank=True)


class 語料表格(ModelForm):

    class Meta:
        model = 語料表
        fields = ['華語來源', '華語內容', '臺語來源', '臺語內容', '備註']


class 正規化表格(ModelForm):

    class Meta:
        model = 語料表
        fields = ['臺語來源', '臺語內容', '文本音標來源', '文本內容', '音標內容', ]
