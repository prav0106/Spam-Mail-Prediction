from django.shortcuts import render
import pickle
import os
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .models import PredictionRecord
from django.contrib.auth.decorators import login_required



# Load ML Model and Vectorizer
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model = pickle.load(open(os.path.join(BASE_DIR, 'spam_model.pkl'), 'rb'))
vectorizer = pickle.load(open(os.path.join(BASE_DIR, 'vectorizer.pkl'), 'rb'))


@login_required(login_url='login')
def home(request):
    return render(request, 'spam_app/home.html')

@login_required
def predict(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        transformed = vectorizer.transform([message])
        result = model.predict(transformed)[0]
        prediction = "SPAM 🚫" if result == 1 else "NOT SPAM ✅"

        # Save to DB
        PredictionRecord.objects.create(
            user=request.user,
            message=message,
            prediction=prediction
        )

        return render(request, 'spam_app/result.html', {'message': message, 'result': prediction})



def register_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=email).exists():
            return render(request, 'spam_app/register.html', {'error': 'User already exists'})
        user = User.objects.create_user(username=email, email=email, password=password)
        return redirect('login')
    return render(request, 'spam_app/register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'spam_app/login.html', {'error': 'Invalid credentials'})
    return render(request, 'spam_app/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def history(request):
    records = PredictionRecord.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'spam_app/history.html', {'records': records})
