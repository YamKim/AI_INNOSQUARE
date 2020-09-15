from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>안녕하세요. 김예함입니다.<br> \
            <a href=http://blog.naver.com/ahalinux>블로그 </a> \
                        <br> <a href=http://algomorgo.tistory.com> 카페 </a>")
