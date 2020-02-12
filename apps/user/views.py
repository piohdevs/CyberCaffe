from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import User
from .form import UserForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
#def home(request):
 #   return render(request, 'user/home.html')

class Home(TemplateView):
    template_name = 'user/home.html'

class ListUser(ListView):
    model = User
    template_name = 'user/list.html'
    context_object_name = 'users'
    queryset = User.objects.all()


class RegisterUser(CreateView):
    model = User
    template_name = 'user/register.html'
    form_class = UserForm
    success_url = reverse_lazy('user:list_user')


class EditUser(UpdateView):
    model = User
    template_name = 'user/register.html'
    form_class = UserForm
    success_url = reverse_lazy('user:list_user')

def deleteUser(request, id):
    user = User.objects.get(id = id)
    user.delete()

    return redirect('user:list_user')


def listUser(request):
    query = request.GET.get('search')
    users = User.objects.all()
    if query:
        users = User.objects.filter(
            Q(first_name__icontains = query)|
            Q(dni__icontains = query)
        )
    paginator = Paginator(users, 10)
    page = request.GET.get('page')
    users = paginator.get_page(page)
    return render(request, 'user/list.html',{"users":users})

'''def editUser(request, id):
    user_form = None
    error = None
    try:
        user = User.objects.get(id = id)
        if request.method == 'GET':
            user_form = UserForm(instance = user)
        else:
            user_form = UserForm(request.POST, instance = user)
            if user_form.is_valid():
                user_form.save()
                return redirect('user:list_user')
        
    except ObjectDoesNotExist as identifier:
        error = identifier
    
    return render(request, 'user/register.html', {'user_form':user_form,'error':error})
'''
'''def registerUser(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('user:list_user')
    else:
        user_form = UserForm()
    
    return render(request, 'user/register.html',{'user_form':user_form})
'''