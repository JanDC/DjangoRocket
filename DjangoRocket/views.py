from django.http import HttpResponse
from django.template import RequestContext, loader
import Rocket

def home(request):
    Rocket()
    template = loader.get_template('home.html')
    context = RequestContext(request, {})
    return HttpResponse(template._render(context))

def move(request):
    rocket = Rocket()
    direction=  request.REQUEST['direction']
    magnitude=request.REQUEST['magnitude']
    if direction == 'LEFT':
        rocket.send_cmd(rocket.LEFT,magnitude)
    if direction == 'RIGHT':
        rocket.send_cmd(rocket.RIGHT,magnitude)
    if direction == 'UP':
        rocket.send_cmd(rocket.UP,magnitude)
    if direction == 'DOWN':
        rocket.send_cmd(rocket.DOWN,magnitude)
    return HttpResponse("Moved " + direction + " by "+ magnitude)
def fire(request):
    rocket = Rocket()
    noOfTimes=  request.REQUEST['amount']
    for i, name in noOfTimes:
        rocket.send_cmd(rocket.FIRE)
    return HttpResponse("Fired "+ noOfTimes +" rocket"+ (noOfTimes>1?"s":""))

