# Create your views here.
from sorl.thumbnail import get_thumbnail
from django.http import *
from django.conf import settings
import base64

def renderimg(request):
    src = str(request.GET.get('src', None))
    xy = request.GET.get('xy', '100x100')
    qos= int(request.GET.get('qos', 99))
    crop = request.GET.get('crop', 'center')
    print base64.encodestring(src)
    src = base64.decodestring(src)
    
    if src:
        try:
            im = get_thumbnail('%s%s%s' % (settings.MEDIA_ROOT, 'images/',src ),'%s' % xy, crop=crop, quality=qos )
            return  HttpResponse('%s%s%s' % (settings.MEDIA_SERVER, settings.MEDIA_URL,im.name) )
        except:
            return HttpResponse('....Aqui Default Image Error')