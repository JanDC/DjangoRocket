from django.http import HttpResponse
from django.template import RequestContext, loader
from Rocket import Rocket
from Webcam import Webcam

def home(request):
    webcam = Webcam()
    webcam.startCamera()
    image = webcam.getImage()
    template = loader.get_template('home.html')
    context = RequestContext(request, {'image': str(image)})
    return HttpResponse(template._render(context))

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

