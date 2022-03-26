from django.http import HttpResponse
from django.shortcuts import render, redirect

from website.forms import NameForm


def index(request):
    condition = False
    list_of_names = ['Muammar', 'Dhay', 'Haider']
    name_form = NameForm()

    if request.method == 'POST':
        name_form = NameForm(request.POST)
        if name_form.is_valid():
            print(name_form)
            return redirect('website:say-hi', 'Layth')
        else:
            print('+++++++++++++++++ Invalid form submit')
            return redirect('website:say-hi', 'Layth')



    return render(request, 'website/lists.html', context={
        'condition': condition,
        'list_of_names': list_of_names,
        'form': name_form,
    })


def say_hi(request, name: str):
    capitalized_name = name.capitalize()
    condition = False
    list_of_names = ['Muammar', 'Dhay', 'Haider']

    return render(request, 'website/index.html', context={
        'name': capitalized_name,
        'condition': condition,
        'list_of_names': list_of_names,
    })
