from django.shortcuts import render
from django.http import JsonResponse
import openai
from decouple import config
# Create your views here.


API_KEY='sk-proj-abcdef1234567890abcdef1234567890abcdef12-Jj5o-0-DCBINdV3qKvgJ0A-rXXIUdA9RllAu7w7d8f9JhT1LmT3BlbkFJ7-V0yRWxpiOdMSUVAu5IGjEXMnnUed9AgxhRlO9MuGgRQwPNxPgeqvTTmnMj4Bz6QELadRnIYA'
client = openai.OpenAI(api_key=API_KEY)


def ask_openAI(message):
    response=client.chat.completions.create(
    model="gpt-3.5-turbo",
        messages=[
        {"role": "user", "content": message}
    ],
    )
    answer=response.choices[0].text.strip()
    return answer

def chatbot(request):
    if request.method=='POST':
        message=request.POST.get('message')
        response=ask_openAI(message)
        return JsonResponse({'message':message,'response':response})
    return render(request,'chatbot.html')