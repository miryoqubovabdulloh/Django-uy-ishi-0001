from django.contrib import admin
from django.urls import path
from uyishi.views import uyishi_list
from dars.views import dars_list
from telefon.views import telefon_list
from shaxar.views import shaxar_list
from rang.views import rang_list
from poyezd.views import poyezd_list
from maxsulot.views import maxsulot_list
from komputer.views import kp_list


urlpatterns = [
    path('uyishi/', uyishi_list),
    path('poyez/', poyezd_list),
    path('tel/', telefon_list),
    path('dars/', dars_list),
    path('kp/', kp_list),
    path('rang/', rang_list),
    path('tavar/', maxsulot_list),
    path('city/', shaxar_list),
    path('admin/', admin.site.urls),
]
