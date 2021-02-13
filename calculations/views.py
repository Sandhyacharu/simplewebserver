from django.shortcuts import render

# Create your views here.

def tables(request):
    context = {}
    result = {}

    if request.method == 'POST':
        n = int(request.POST.get('value_n',0))
        for i in range(1,11):
            result[i]= i*n
        context['result'] = result.items
        context['n'] = 0
        

    if request.method == 'GET':
       context['n'] = 0
       context['result'] = result.items

    return render(request,'calculations/tables.html', context) 