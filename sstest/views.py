from django.shortcuts import render


def main(request):
    return render(request, 'sstest/main.html')


def qSet(request):
    return render(request, 'sstest/question.html')


def result(request):
    return result(request, 'sstest/result.html')
