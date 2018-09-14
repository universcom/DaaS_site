from django.shortcuts import render , redirect
from .activeDirectory import create_user_activedirectory
from .form import SignUpForm
from .openldap import create_user_ldap , add_connection_to_user
from .drive import create_drive


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            first_name=form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
           # print(username , raw_password , first_name , last_name)
            create_user_ldap(username , raw_password , first_name)
           ## create_user_activedirectory(username , raw_password , first_name)
           ## create_drive(username)
            if form.cleaned_data.get('matlab'): add_connection_to_user(1 , username , raw_password)
            if form.cleaned_data.get('revite'): add_connection_to_user(2 , username , raw_password)
            if form.cleaned_data.get('photoshop'): add_connection_to_user(3 , username , raw_password)
            if form.cleaned_data.get('max3d'): add_connection_to_user(4 , username , raw_password)
            #user = authenticate(username=username, password=raw_password)
           # login(request, user)
            return redirect('singup')
    else:
        form = SignUpForm()
    return render(request, 'singup_page.html', {'form': form})
