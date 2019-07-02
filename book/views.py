from django.db.models import F, Avg, Count
from django.shortcuts import render
from .models import HeroInfo, GameInfo
# Create your views here.
from django.http import HttpResponse
from django.views import View
from datetime import date


class InterView(View):
    def get(self, request):
        # b=GameInfo.objects.filter(gpalyer__gt = 1000000)
        a = GameInfo.objects.aggregate(Count('gpalyer'))
        print(a)

        # HeroInfo.objects.create(hname='Saber',hgender=3,hskill='Excalibur',hgame_id = 3)
        return HttpResponse('ok')
        # a = GameInfo.objects.aggregate(Avg('gpalyer'))
        # print(a)
        # a = GameInfo.objects.filter(gpalyer__gt = GameInfo.objects.aggregate(Avg('gpalyer'))['gpalyer__avg'])
        # return render(request, 'model.html', {'a': a})

    def post(self, request):
        a = HeroInfo.objects.all()

        return render(request, 'hr.html', {'a': a})
