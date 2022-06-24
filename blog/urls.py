
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
     path('admin/', admin.site.urls),
     path('conteudo/',include('conteudo.urls')),
     path('contato/',include('contato.urls')),
     path('pagamento/', include ('pagamento.urls')),
]
