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

model_path = os.path.join(BASE_DIR, 'spam_model.pkl')
vectorizer_path = os.path.join(BASE_DIR, 'vectorizer.pkl')

model = pickle.load(open(model_path, 'rb'))
vectorizer = pickle.load(open(vectorizer_path, 'rb'))



@login_required(login_url='login')
def home(request):
    return render(request, 'spam_app/home.html')

@login_required
def predict(request):
    if request.method == 'POST':
        try:
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

            return render(request, 'spam_app/result.html', {
                'message': message,
                'result': prediction
            })
        except Exception as e:
            return render(request, 'spam_app/result.html', {
                'message': 'Something went wrong!',
                'result': f'Error: {str(e)}'
            })




def register_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            return render(request, 'spam_app/register.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=email).exists():
            return render(request, 'spam_app/register.html', {'error': 'User already exists'})

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
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
