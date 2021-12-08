from django.shortcuts import render
from .models import Fixture, Team

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def fixture(request):
    fixture = Fixture.objects.all()
    
    all_completed = all(f.game_finished for f in fixture)
    context = {
        'fixtures':fixture,
        'all_completed':all_completed
        }
    
    if request.htmx:
        if all_completed:
            response = return render (request,'partials/fixture-list.html',context)
            request['HX_REFRESH'] = true 
            return response
        
        return render (request,'partials/fixture-list.html',context)
    else:
        return render (request,'fixture.html',context)