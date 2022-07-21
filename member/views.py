from django.shortcuts import render
from .models import Member
from django.utils import timezone
from django.http import HttpResponse


def signup(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')
        user_name = request.POST.get('user_name')
        user_birth = request.POST.get('user_birth')
        user_gender = request.POST.get('user_gender')

        m = Member(
            user_id=user_id, user_pw=user_pw, user_name=user_name, user_birth=user_birth, user_gender=user_gender
        )
        m.date_joined = timezone.now()
        m.save()
        return HttpResponse(
            '가입 완료<br>%s %s %s' % (user_id, user_pw, user_name, user_birth, user_gender))
    else:
      return render(request, 'member/signup_custom.html')
