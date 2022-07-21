from django.shortcuts import render
from .models import Member
from django.utils import timezone
from django.http import HttpResponse
import datetime

def signup(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')
        user_name = request.POST.get('user_name')
        user_birth = request.POST.get('user_birth')
        if datetime.date.today().year - int(datetime.datetime.strptime(user_birth, "%Y-%m-%d").year) < 19:
            return HttpResponse(
        "<script>alert('나이가 너무 어립니다.\\n\\n메인페이지로 돌아갑니다.');location.href='/sstest/main';</script>")
        user_gender = request.POST.get('user_gender')

        m = Member(
            user_id=user_id, user_pw=user_pw, user_name=user_name, user_birth=user_birth, user_gender=user_gender
        )
        m.date_joined = timezone.now()
        m.save()
        return HttpResponse(
            '가입 완료<br>%s %s %s %s %s' % (user_id, user_pw, user_name, user_birth, user_gender))
    else:
      return render(request, 'member/signup.html')
