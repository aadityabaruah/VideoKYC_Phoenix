from django.shortcuts import render
from django.http import JsonResponse
import textwrap
import google.generativeai as genai


model = None
chat = None

def initialize_chatbot():
    global model, chat
    genai.configure(api_key='no_api_key')
    model = genai.GenerativeModel('llama70b-pro')
    chat = model.start_chat(history=[])
    chat.send_message(initial_text)

def process_chatbot_response(response):
    if 'KYC_VERIFICATION_LAUNCH' in response:
        print("redirect to annish html")
        # response = response.replace('KYC_VERIFICATION_LAUNCH', '')
    return response

def chatbot_view(request):
    global model, chat
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        response = chat.send_message(user_input).text
        response = process_chatbot_response(response)
        return JsonResponse({'response': response})
    return render(request, 'chatbot/index.html')

# Initialize the chatbot when the server starts
initialize_chatbot()
