from django.shortcuts import render


def main(request):
    return render(request, 'sstest/main.html')


def qSet(request):
    return render(request, 'sstest/question.html')


def result(request):
    
    return render(request, 'sstest/resultpage.html')

def result(request):
    if request.method == 'POST':
      answer_list = []
      
      for i in range(13):
          answer_list.append(request.POST.get(f'question-{i+1}'))

      s_list = [answer_list.count("1"), answer_list.count("2"), answer_list.count("3"), answer_list.count("4")]
      m = max(s_list)     
      result_type = []
      for i, v in enumerate(s_list):
        if v == m :
            result_type.append(i+1)
            return render(request,'sstest/result.html',  {'result_type': result_type})