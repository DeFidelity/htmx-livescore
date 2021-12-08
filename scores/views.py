from django.shortcuts import render
from .models import Fixture, Team
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def fixture(request):
    fixture = Fixture.objects.all()
    
    search = request.GET.get('search')
    
    if search:
        fixture = fixture.filter(
            Q(home_team__name__icontains=search) | Q(away_team__name__icontains=search)
        )
    
    
    all_completed = all(f.game_finished for f in fixture)
    context = {
        'fixtures':fixture,
        'all_completed':all_completed
        }
    
    if request.htmx:
        import time 
        time.sleep(0.6)
        if all_completed:
            # fixture = Fixture.objects.get(home_team__name="real betis")
            # fixture.game_finished = True
            response = render (request,'partials/fixture-list.html',context)
            response['HX_Refresh'] = "true"
            return response
        
        return render (request,'partials/fixture-list.html',context)
    else:
        return render (request,'fixture.html',context)