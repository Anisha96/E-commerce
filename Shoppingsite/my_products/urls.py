from django.conf.urls import url
from my_products import views
from django.conf.urls.static import static, settings
from .models import Product, Dresses
from django.contrib import admin
from .forms import UserForm

urlpatterns = [
    url(r'^$', views.HomePageView, name='index'),
    url(r'^registration/$', views.UserFormView.as_view(), name='register'),
    url(r'^about/$', views.aboutView.as_view(), name='about'),
    url(r'^checkout/$', views.checkoutView.as_view(), name='checkout'),
    url(r'^dresses/$', views.dressesView.as_view(), name='dresses'),
    url(r'^faq/$', views.faqView.as_view(), name='faq'),
    url(r'^jeans/$', views.jeansView.as_view(), name='jeans'),
    url(r'^mail/$', views.mailView.as_view(), name='mail'),
    url(r'^products/$', views.productsView.as_view(), name='products'),
    url(r'^index/$', views.product_list),
    url(r'^dress/$', views.dress_list),
    url(r'^jean/$', views.jeans_list),
    url(r'^summerstore/$', views.products_list),
    url(r'^salwar/$', views.salwars_list),
    url(r'^sandal/$', views.sandals_list),
    url(r'^saree/$', views.sarees_list),
    url(r'^shirt/$', views.shirts_list),
    url(r'^skirt/$', views.skirts_list),
    url(r'^sweater/$', views.sweaters_list),
    url(r'^salwars/$', views.salwarsView.as_view(), name='salwars'),
    url(r'^sandals/$', views.sandalsView.as_view(), name='sandals'),
    url(r'^sarees/$', views.sareesView.as_view(), name='sarees'),
    url(r'^shirts/$', views.shirtsView.as_view(), name='shirts'),
    url(r'^short-codes/$', views.kidsView.as_view(), name='short-codes'),
    url(r'^single/(?P<pk>[0-9]+)/$', views.singleView, name='single'),
    url(r'^single//(?P<pk>[0-9]+)/$', views.single_sweaterView, name='single_sweater'),
    url(r'^single///(?P<pk>[0-9]+)/$', views.single_skirtsView, name='single_skirts'),
    url(r'^single///(?P<pk>[0-9]+)//$', views.single_jeansView, name='single_jeans'),
    url(r'^single////(?P<pk>[0-9]+)/$', views.single_shirtsView, name='single_shirts'),
    url(r'^single/(?P<pk>[0-9]+)//$', views.single_salwarsView, name='single_salwars'),
    url(r'^single/(?P<pk>[0-9]+)///$', views.single_sareesView, name='single_sarees'),
    url(r'^single//(?P<pk>[0-9]+)//$', views.single_sandalsView, name='single_sandals'),
    url(r'^single//(?P<pk>[0-9]+)///$', views.single_indexView, name='single_index'),
    url(r'^single////(?P<pk>[0-9]+)//$', views.single_kidsView, name='single_kids'),
    url(r'^single///(?P<pk>[0-9]+)///$', views.single_productsView, name='single_products'),
    url(r'^skirts/$', views.skirtsView.as_view(), name='skirts'),
    url(r'^sweaters/$', views.sweatersView.as_view(), name='sweaters'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
