from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def contacts(request):
    return render(request, 'contacts.html')

# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         message = request.POST.get('message')
#         return HttpResponse(f'Спасибо, {name}! Сообщение получено.')
#     return render(request, "app/contacts.html")
#
# def home(request):
#     if request.method == 'GET':
#         return render(request, 'app/home.html')


