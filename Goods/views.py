from django.shortcuts import render


def main(request):
    return render(request, 'base.html')

def login(request):
    return render(request, 'login-register.html')