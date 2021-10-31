
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
import json



class HttpResponseThen(HttpResponse): 
    def __init__(self, data, then_callback, **kwargs):
        super().__init__(data, **kwargs)
        self.then_callback = then_callback

    def close(self):
        super().close()
        return_value = self.then_callback


@csrf_exempt
def index(request):
    print(request)
    template = loader.get_template('calc/index.html')
    return HttpResponse(template.render())

@csrf_exempt
def test():
    print("Hello World MAN")
@csrf_exempt
def buy(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    print(body)
    return HttpResponseThen(" ", then_callback=test())
