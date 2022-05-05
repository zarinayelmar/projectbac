from unicodedata import name
from django.shortcuts import render,redirect
from .models import Salt
from .models import Makal
from .models import Urum
from .forms import SaltForm
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import UserRegistrationForm,LoginUserForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
# Create your views here.

def send_message(request): 
    send_mail("Welcome to testing page","My content","200103107@stu.sdu.edu.kz",["200103107@stu.sdu.edu.kz","200103107@stu.sdu.edu.kz"], 
              fail_silently=False,html_message="<b>Bold text </b> <i>Italic text </i>" )
    return render (request,'project/successful.html')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'project/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'project/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'project/registor.html', {'user_form': user_form})

def home(request):
    salt = Salt.objects.all()
    return render(request,'project/first.html',{'salt': salt})

class NewsDetailView(DetailView):
    model = Salt
    template_name = 'project/details.html'
    context_object_name = 'salt'

class NewsUpdateView(UpdateView):
    model = Salt
    success_url = '/project/'
    template_name = 'project/update.html'
    form_class = SaltForm

class NewsDeleteView(DeleteView):
    model = Salt
    success_url = '/project/'
    template_name = 'project/delete.html'

def urum(request):
    urum = Urum.objects.all()
    return render(request,'project/urum.html',{'title':'Ырым тыйымдары','urum': urum}) 
def makal(request):
    makal = Makal.objects.all()
    return render(request,'project/makal.html',{'title':'Мақал','makal': makal}) 

def create(request):
    if request.method == 'POST':
          form = SaltForm(request.POST)
          if form.is_valid():
              form.save()
              return redirect('home')

    form = SaltForm()
    data = {
      'form': form
    }
    return render(request,'project/insert.html', data)

