from django.shortcuts import render 
import requests
from django.http import HttpResponseNotAllowed
from .forms import AnswerForm


# Create your views here.
def index(request):
    response = requests.get('https://shadify.dev/api/countries/capital-quiz')
    game = response.json()
    context = {'game':game}
    request.session['game'] = game
    return render(request, 'index.html', context)
   

def check_answer(request):
    game = request.session['game']
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.cleaned_data['answer']
            if answer == game['answer']:
                # Render a template with a message saying the answer is correct
                return render(request, 'correct_answer.html')
            else:
                # Render a template with a message saying the answer is incorrect
                return render(request, 'incorrect_answer.html')
    else:
        form = AnswerForm()
    return render(request, 'check_answer.html', {'form': form})




