import json

from django.db import models
from django.forms.models import ModelForm
from django import forms


預設來源 = json.dumps({
    '名': '',
    '網址': '',
    '影片': '',
}, indent=2, ensure_ascii=False, sort_keys=True)


def 愛有名(value):
    try:
        資料 = json.loads(value)
    except:
        raise forms.ValidationError(
            ('愛是json'),
        )
    try:
        名 = 資料['名']
    except:
        raise forms.ValidationError(
            ('愛有名'),
        )
    if 名 == '':
        raise forms.ValidationError(
            ('名袂使是空的'),
        )


class 語料表(models.Model):
    收錄時間 = models.DateField(auto_now_add=True)
    上尾修改時間 = models.DateField(auto_now=True)

    華語內容 = models.TextField(blank=True)
    華語來源 = models.TextField(blank=True)
    臺語內容 = models.TextField()
    臺語來源 = models.TextField(default=預設來源, validators=[愛有名])
    文本內容 = models.TextField()
    音標內容 = models.TextField()
    文本音標來源 = models.TextField(default=預設來源, validators=[愛有名])

    備註 = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return '{} {}'.format(self.臺語內容.split()[0], self.備註)


class 語料表格(ModelForm):

    class Meta:
        model = 語料表
        fields = ['華語來源', '華語內容', '臺語來源', '臺語內容', '備註']

    def clean(self):
        cleaned_data = super(語料表格, self).clean()
        華語內容 = cleaned_data.get("華語內容")
        華語來源 = cleaned_data.get("華語來源")

        if 華語內容 != '':
            愛有名(華語來源)
        elif 華語來源 != '':
#             self.add_error('華語來源', '華語無內容有來源')
            raise forms.ValidationError(('華語無內容有來源'),)


class 正規化表格(ModelForm):

    class Meta:
        model = 語料表
        fields = ['臺語來源', '臺語內容', '文本音標來源', '文本內容', '音標內容', ]
