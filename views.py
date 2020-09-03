from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

# render 함수는 3개의 인자를 받는다.
# 1 : 인수, 2 : template 이름, 3 : dict 자료형

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    total = text.split()
    word_dic = {}

    for i in total:
        if i not in word_dic:
            word_dic[i] = 1
        else:
            word_dic[i] += 1

    return render(request, 'result.html', {'full':text, 'total':len(total), \
        'dic' : word_dic.items()})