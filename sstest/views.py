from django.shortcuts import render

def main(request):
    return render(request, 'sasang/main.html')

def qSet(request):
    return render(request, 'sasang/question.html')

def result(request):
    return result(request, 'sasang/result.html')