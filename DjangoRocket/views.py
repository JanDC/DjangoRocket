from django.http import HttpResponse,HttpResponseNotFound
from django.template import RequestContext, loader
from django.conf import settings
from Rocket import Rocket
from Webcam import Webcam

def home(request):
    template = loader.get_template('home.html')
    context = RequestContext(request, {'image': 'sdfsdf'})
    return HttpResponse(template.render(context))

def move(request):
    rocket = Rocket()
    direction= request.GET['direction']
    magnitude= float(request.GET['magnitude'])
    if direction == 'LEFT':
        rocket.send_move(rocket.LEFT,magnitude)
    if direction == 'RIGHT':
        rocket.send_move(rocket.RIGHT,magnitude)
    if direction == 'UP':
        rocket.send_move(rocket.UP,magnitude)
    if direction == 'DOWN':
        rocket.send_move(rocket.DOWN,magnitude)
    return HttpResponse("Moved " + direction + " by "+ magnitude.__str__())
def fire(request):
    rocket = Rocket()
    rocket.send_cmd(rocket.FIRE)
    return HttpResponse("Fired rocket")
def abort(request):
    rocket = Rocket()
    rocket.send_cmd(rocket.STOP)
    return HttpResponse("Aborted current command")
def loadUp(request):
    rocket = Rocket()
    duration=float(request.GET["duration"])
    rocket.send_move(rocket.FIRE,duration)
    return HttpResponse("Loaded for "+ duration.__str__()+ " ms")
def files(request):
    import os.path
    import mimetypes
    mimetypes.init()
    file_url = 'flowplayer-3.2.18.swf'
    try:
        file_path = 'files/' + file_url
        fsock = open(file_path,"r")
        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)
        print "file size is: " + str(file_size)
        response = HttpResponse(fsock)
        response['Content-Disposition'] = 'attachment; filename=' + file_name
    except IOError:
        response = HttpResponseNotFound('boom')
    return response

