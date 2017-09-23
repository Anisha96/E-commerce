from django.views.generic import TemplateView
from .models import Product, Dresses, Sweaters, Skirts, Jeans, Shirts, Sarees, Salwars, Sandals, Products, Kids
from django.views import generic
from django.template import loader
from .forms import UserForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import View
from .serializers import ProductSerializer, DressesSerializer, SweatersSerializer, SkirtsSerializer, JeansSerializer, \
    ShirtsSerializer, SareesSerializer, SalwarsSerializer, SandalsSerializer, ProductsSerializer
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


# Create your views here.

def HomePageView(request):
    all_products = Product.objects.all()

    template = loader.get_template('my_products/index.html')
    context = {'all_products': all_products,
               }
    return render(request, 'my_products/index.html', context)


class aboutView(TemplateView):
    template_name = "about.html"


class checkoutView(generic.ListView):
    template_name = "checkout.html"

    context_object_name = "all_products"

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super(checkoutView, self).get_context_data(**kwargs)
        context['all_dresses'] = Dresses.objects.all()[:5]
        # ^^^ bad duplication.
        return context


class dressesView(generic.ListView):
    template_name = "dresses.html"
    context_object_name = 'all_dresses'

    def get_queryset(self):
        return Dresses.objects.all()
    def get_context_data(self, **kwargs):
         context = super(dressesView, self).get_context_data(**kwargs)
         context['all_sandals'] = Sandals.objects.all()[:5]
            # ^^^ bad duplication.
         return context



class faqView(TemplateView):
    template_name = "faq.html"


class jeansView(generic.ListView):
    template_name = "jeans.html"
    context_object_name = 'all_jeans'

    def get_queryset(self):
        return Jeans.objects.all()

    def get_context_data(self, **kwargs):
        context = super(jeansView, self).get_context_data(**kwargs)
        context['all_shirts'] = Shirts.objects.all()[:5]
        # ^^^ bad duplication.
        return context


class mailView(TemplateView):
    template_name = "mail.html"


class productsView(generic.ListView):
    template_name = "products.html"
    context_object_name = 'all_product'

    def get_queryset(self):
        return Products.objects.all()

    def get_context_data(self, **kwargs):
        context = super(productsView, self).get_context_data(**kwargs)
        context['all_products'] = Product.objects.all()[:5]
        # ^^^ bad duplication.
        return context


class salwarsView(generic.ListView):
    template_name = "salwars.html"
    context_object_name = 'all_salwar'

    def get_queryset(self):
        return Salwars.objects.all()

    def get_context_data(self, **kwargs):
        context = super(salwarsView, self).get_context_data(**kwargs)
        context['all_sarees'] = Sarees.objects.all()[:5]
        # ^^^ bad duplication.
        return context


class sandalsView(generic.ListView):
    template_name = "sandals.html"
    context_object_name = 'all_sandals'

    def get_queryset(self):
        return Sandals.objects.all()
    def get_context_data(self, **kwargs):
         context = super(sandalsView, self).get_context_data(**kwargs)
         context['all_dresses'] = Dresses.objects.all()[:5]
            # ^^^ bad duplication.
         return context



class sareesView(generic.ListView):
    template_name = "sarees.html"
    context_object_name = 'all_sarees'

    def get_queryset(self):
        return Sarees.objects.all()

    def get_context_data(self, **kwargs):
         context = super(sareesView, self).get_context_data(**kwargs)
         context['all_salwars'] = Salwars.objects.all()[:5]
            # ^^^ bad duplication.
         return context

class kidsView(generic.ListView):
    template_name = "short-codes.html"
    context_object_name = 'all_kids'

    def get_queryset(self):
        return Kids.objects.all()
    def get_context_data(self, **kwargs):
        context = super(kidsView, self).get_context_data(**kwargs)
        context['all_products'] = Product.objects.all()[:5]
        # ^^^ bad duplication.
        return context


class shirtsView(generic.ListView):
    template_name = "shirts.html"
    context_object_name = 'all_shirts'

    def get_queryset(self):
        return Shirts.objects.all()
    def get_context_data(self, **kwargs):
        context = super(shirtsView, self).get_context_data(**kwargs)
        context['all_jeans'] = Jeans.objects.all()[:5]
        # ^^^ bad duplication.
        return context


def singleView(request, pk):
    dresses = Dresses.objects.get(pk=pk)
    context = {'dresses': dresses, }

    return render(request, 'my_products/single.html', context)



class skirtsView(generic.ListView):
    template_name = "skirts.html"
    context_object_name = 'all_skirt'

    def get_queryset(self):
        return Skirts.objects.all()
    def get_context_data(self, **kwargs):
        context = super(skirtsView, self).get_context_data(**kwargs)
        context['all_sweater'] = Sweaters.objects.all()[:5]
        # ^^^ bad duplication.
        return context


class sweatersView(generic.ListView):
    template_name = "sweaters.html"
    context_object_name = 'all_sweater'

    def get_queryset(self):
        return Sweaters.objects.all()
    def get_context_data(self, **kwargs):
        context = super(sweatersView, self).get_context_data(**kwargs)
        context['all_skirt'] = Skirts.objects.all()[:5]
        # ^^^ bad duplication.
        return context


def single_sweaterView(request, pk):
    sweater = Sweaters.objects.get(pk=pk)
    context = {'sweater': sweater, }

    return render(request, 'my_products/single.html', context)


def single_skirtsView(request, pk):
    skirt = Skirts.objects.get(pk=pk)
    context = {'skirt': skirt, }

    return render(request, 'my_products/single.html', context)

def single_kidsView(request, pk):
    kids = Kids.objects.get(pk=pk)
    context = {'kids': kids, }

    return render(request, 'my_products/single.html', context)


def single_jeansView(request, pk):
    jeans = Jeans.objects.get(pk=pk)
    context = {'jeans': jeans, }

    return render(request, 'my_products/single.html', context)

def single_productsView(request, pk):
    products = Products.objects.get(pk=pk)
    context = {'products': products, }

    return render(request, 'my_products/single.html', context)


def single_shirtsView(request, pk):
    shirts = Shirts.objects.get(pk=pk)
    context = {'shirts': shirts, }

    return render(request, 'my_products/single.html', context)


def single_salwarsView(request, pk):
    salwars = Salwars.objects.get(pk=pk)
    context = {'salwars': salwars, }

    return render(request, 'my_products/single.html', context)


def single_sareesView(request, pk):
    sarees = Sarees.objects.get(pk=pk)
    context = {'sarees': sarees, }

    return render(request, 'my_products/single.html', context)


def single_sandalsView(request, pk):
    sandals = Sandals.objects.get(pk=pk)
    context = {'sandals': sandals, }

    return render(request, 'my_products/single.html', context)


def single_indexView(request, pk):
    products = Product.objects.get(pk=pk)
    context = {'products': products, }

    return render(request, 'my_products/single.html', context)


class UserFormView(View):
    form_class = UserForm
    template_name = 'formtemp.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')

        return render(request, self.template_name, {'form': form})


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JSONResponse(serializer.data)


def dress_list(request):
    if request.method == 'GET':
        dresses = Dresses.objects.all()
        serializer = DressesSerializer(dresses, many=True)
        return JSONResponse(serializer.data)


def jeans_list(request):
    if request.method == 'GET':
        jeans = Jeans.objects.all()
        serializer = JeansSerializer(jeans, many=True)
        return JSONResponse(serializer.data)
def products_list(request):
    if request.method == 'GET':
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return JSONResponse(serializer.data)

def salwars_list(request):
    if request.method == 'GET':
        salwars = Salwars.objects.all()
        serializer = SalwarsSerializer(salwars, many=True)
        return JSONResponse(serializer.data)

def sandals_list(request):
    if request.method == 'GET':
        sandals = Sandals.objects.all()
        serializer = SandalsSerializer(sandals, many=True)
        return JSONResponse(serializer.data)

def sarees_list(request):
    if request.method == 'GET':
        sarees = Sarees.objects.all()
        serializer = SareesSerializer(sarees, many=True)
        return JSONResponse(serializer.data)

def shirts_list(request):
    if request.method == 'GET':
        shirts = Shirts.objects.all()
        serializer = ShirtsSerializer(shirts, many=True)
        return JSONResponse(serializer.data)

def skirts_list(request):
    if request.method == 'GET':
        skirts = Skirts.objects.all()
        serializer = SkirtsSerializer(skirts, many=True)
        return JSONResponse(serializer.data)

def sweaters_list(request):
    if request.method == 'GET':
        sweaters = Sweaters.objects.all()
        serializer = SweatersSerializer(sweaters, many=True)
        return JSONResponse(serializer.data)


