from django.shortcuts import render
from member.models import Member


def main(request):
    return render(request, 'sstest/main.html')


def qSet(request):
    return render(request, 'sstest/question.html')


def result(request):
    if request.method == 'POST':
        answer_list = []
        for i in range(13):
            answer_list.append(request.POST.get(f'question-{i+1}'))

        s_list = [answer_list.count("1"), answer_list.count("2"), answer_list.count("3"), answer_list.count("4")]
        m = max(s_list)     
        result_type = []
        for i, v in enumerate(s_list):
            if v == m:
                if i == 0 : result_type.append("태양인")
                elif i == 1 : result_type.append("태음인")
                elif i == 2 : result_type.append("소양인")
                elif i == 3 : result_type.append("소음인")
                
        return render(request,'sstest/result.html',  {
            's_list':s_list, 
            'm' : m,
            'result_type': result_type,
            
            })