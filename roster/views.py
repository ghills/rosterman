from django.shortcuts import render_to_response, get_object_or_404
from roster.models import Team

# Create your views here.

def index(request):
    team_list = Team.objects.all().order_by('name')
    return render_to_response('roster/index.html', {'team_list': team_list})

def detail(request,team_id):
    t = get_object_or_404(Team, pk=team_id)
    return render_to_response('roster/detail.html', {'team': t})
