from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


API_KEY=''

def chatbot(request):
    if request.method=='POST':
        message=request.POST.get('message')
        response='HI IM CHAT'
        return JsonResponse({'message':message,'response':response})
    return render(request,'chatbot.html')