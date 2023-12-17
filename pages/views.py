from django.shortcuts import render

def index(request):
    email = 'negar.tusi@gmail.com'
    phone_number = '+98 902 745 8376'
    name = 'Negar Toosi'
    address = 'satarkhan Street, Tehran'
    age = '21'
    context = {'email': email,
                'phone_number': phone_number,
                'name': name,
                'address': address,
                'age': age}
    return render(request, 'pages/index.html', context)
