from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy

from .models import Bookmark

# Create your views here.

# from rest_framework.views import APIView
from django.http import HttpResponse



# Bookmark 리스트 출력
class BookMarkListView(ListView):
    print("BookMarkListView 진입!!!!!")
    model = Bookmark


# Bookmark  등록
class BookMarkCreateView(CreateView):
    print("BookMarkCreateView 진입!!!!!")
    model = Bookmark

    #작성할 필드명 지정
    fields = ['site_name', 'url']

    # success_url은 성공시 redirect가 일어날 주소
    # 성공 후 redirect url 지정
    success_url = reverse_lazy('list')

    # #작성에 성공한 경우 보낼 탬플릿. 자동으로 생성된 후보 템플릿 이름에 추가할 접미사
    # 사용하는 탬플릿 명을 '모델명_create.html'로 바꾼다는 의미. 접미사만 바꾼다.
    # 기본 탬플릿은 '모델명_form.html'로 나타난다.
    # create와 update는 모델명_form.html을 불러오기 때문에 suffix 변경하여 사용
    # template_name_suffix = '_form'
    # template_name_suffix = '_detail'
    # template_name_suffix = '_confirm_delete'
    # template_name_suffix = '_update'
    
    template_name_suffix = '_create'


# Bookmark 상세조회 
class BookMarkDetailView(DetailView):
    print("BookMarkDetailView 진입!!!!!")
    model = Bookmark



# Bookmark  update
class BookMarkUpdateView(UpdateView):
    print("BookMarkUpdateView 진입!!!!!")
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'


# Bookmark  삭제
class BookMarkDeleteView(DeleteView):
    print("BookMarkDeleteView 진입!!!!!")
    model = Bookmark
    success_url = reverse_lazy('list')
    template_name_suffix = '_delete'



################################################


# html 변수 적용 예제
def book01(request):
    print("book01(request) 호출")
    html = '''<html>
                <body>
                    Hello ! book01 이야!!!!
                </body>
            </html>'''
    return HttpResponse(html)


# html 변수 대신 템플릿 적용 예제
def template_book01(request):
    print("template_book01(request) 호출")
  
    return render(request, 'book01.html')

