from django.shortcuts import render, redirect
from 網路語料.models import 語料表
from 網路語料.models import 語料表格


def 全部語料(request):
    return render(request, '網路語料/全部.html', {
        '語料': 語料表.objects.all(),
    })
    
def 加語料(request):
    if request.method == 'POST': 
        表格 = 語料表格(request.POST)
        if 表格.is_valid():
            _語料=表格.save()
            return redirect('首頁')
    else:
        表格 = 語料表格()
    return render(request, '網路語料/加.html', {
        '表格': 表格,
    })
    
def 看語料(request, pk):
    return render(request, '網路語料/看.html', {
        '語料': 語料表.objects.get(pk=pk),
    })