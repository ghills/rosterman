from django.shortcuts import render_to_response, get_object_or_404
from roster.models import Team, Player
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

def index(request):
    team_list = Team.objects.all().order_by('name')
    return render_to_response('roster/index.html', {'team_list': team_list})

def detail(request,team_id):
    t = get_object_or_404(Team, pk=team_id)
    return render_to_response('roster/detail.html', {'team': t})
    
def add_player(request,team_id):
    t = get_object_or_404(Team,pk=team_id)
    try:
        p = Player()
        p.first_name = request.POST['first_name']
        p.last_name = request.POST['last_name']
        p.number = request.POST['number']
        p.height = request.POST['height']
    except (KeyError):
        return render_to_response("roster/%d" % team_id, {
                                   'error_message' : "You forgot fields"})
    else:
        p.team = t
        p.save()
        return HttpResponseRedirect(reverse('roster',args=(team_id)))