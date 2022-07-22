from imaplib import _Authenticator
from django.shortcuts import redirect, render

from member.form import UserForm
from .models import Member
from django.utils import timezone
from django.http import HttpResponse

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = _Authenticator(username=username, password=raw_password)
            login(request, user)
            return redirect('member/login.html')
    else:
        form = UserForm()
    return render(request, 'member/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')
        try:
            m = Member.objects.get(user_id=user_id, user_pw=user_pw)
        except Member.DoesNotExist as e:
            return HttpResponse('로그인 실패')
    else:
        return render(request, 'member/login.html')

