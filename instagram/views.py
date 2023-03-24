from django.shortcuts import render
# from rest_framework.views import APIView
from django.http import HttpResponse

# html 변수 적용 예제
def index(request):
    print("index(request) 호출")
    html = '''<html>
                <body>
                    Hello ! 장고 홈이야!!!!
                </body>
            </html>'''
    return HttpResponse(html)


def welcome(request):
    print("welcome(request) 호출")
    html = '''<html>
                <body>
                    Welcome ! 장고!!!!
                </body>
            </html>'''
    return HttpResponse(html)

# html 변수 대신 템플릿 적용 예제
def template_test(request):
    print("template_test(request) 호출")
    # html = '''<html>
    #             <body>
    #                 Welcome ! 장고!!!!
    #             </body>
    #         </html>'''

    # 텝플릿 폴더 3가지 종류
    # 1. admin 앱 폴더
    # 2. 앱 폴더의 텝를릿 폴더
    # 3. 설정 폴더

    # render(request, template_name, context=None, content_type=None, status=None, using=None)

    # name 'test' is not defined  ==> 'test.html'   '' 없는 경우
    # TemplateDoesNotExist at /test/ test.html ==>  test.html 없는 경우 ==> html 등록 (텝플릿 폴더 3가지 종류 참조)

    # template_name = 'a.html'
    # return render(request, template_name)
    return render(request, 'test.html')
