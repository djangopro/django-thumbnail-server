# Create your views here.
from sorl.thumbnail import get_thumbnail
from django.http import *
from django.conf import settings
from django.utils.encoding import smart_str
import base64

def renderimg(request):
    name = str(request.GET.get('name', None))
    name = smart_str(base64.b64decode(name))

    xy = request.GET.get('xy', '100x100')
    qos= int(request.GET.get('qos', 99))
    crop = request.GET.get('crop', 'center')

    if name:
        try:
            im = get_thumbnail('%s%s%s' % (settings.MEDIA_ROOT, 'images/', name),'%s' % xy, crop=crop, quality=qos )
            return  HttpResponse('%s%s%s' % (settings.MEDIA_SERVER, settings.MEDIA_URL, im.name) )
        except:
            raise