# FIXME:  fire up tornado

from django.http import HttpResponse
from polls.models import Poll
from django.template import Context, loader

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    t = loader.get_template('polls/index.html')
    c = Context( {
        'latest_poll_list' : latest,
    })

    return HttpResponse(t.render(c))



def detail(request,poll_id):
    return HttpResponse("Poll is %s" % poll_id)

def results(request,poll_id):
    return HttpResponse("Results of poll %s" %poll_id)

def vote(request,poll_id):
    return HttpResponse("Youre voting on poll %s" %poll_id)


