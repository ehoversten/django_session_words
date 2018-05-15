from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 1

    return render(request, 'survey_form/index.html')

def process(request):
    if request.method == 'POST':
        print('*'*50)
        print(request.POST)
        request.session['count'] += 1
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['fav'] = request.POST['fav']
        request.session['comments'] = request.POST['comments']
        print("*"*50)
        return redirect('/success')
    else:
        return redirect('/')

def success(request):
    return render(request, 'survey_form/success.html')

def reset(request):
    # request.session.clear()
    return redirect('/')
