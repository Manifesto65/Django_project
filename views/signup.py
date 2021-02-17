from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer


def validateUser(customer):
    error_message = None
    if not customer.first_name:
        error_message = 'First name is required'
    elif len(customer.first_name) < 3:
        error_message = 'First  name should be more than 2 letters'
    elif not customer.last_name:
        error_message = 'Last name is required'
    elif len(customer.last_name) < 3:
        error_message = 'Last  name should be more than 2 letters'
    elif len(customer.email) < 5:
        error_message = 'email should be more than 5 letters'
    elif len(customer.password) < 4:
        error_message = 'password should be more than 2 letters'
    elif customer.isExist():
        error_message = 'Email address already exists'

    return error_message


def registerUser(request):
    postData = request.POST
    first_name = postData.get('fname')  # Write the name that is in the name flied of the input
    last_name = postData.get('lname')
    email = postData.get('email')
    password = postData.get('password')

    # Filling the already written form
    value = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email
    }

    error_message = None

    customer = Customer(first_name=first_name, last_name=last_name, email=
    email, password=password)

    error_message = validateUser(customer)

    if not error_message:
        # saving
        customer.password = make_password(customer.password)
        customer.register()
        return redirect('homepage')

    else:
        data = {
            'error': error_message,
            'values': value
        }

        return render(request, 'signup.html', data)

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        return registerUser(request)