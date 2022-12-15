from django.shortcuts import render
from mainapp.models import Product, ProductCategory

def main(request):
    return render(request, 'mainapp/index.html')


def products(request):
    context = {
        "products": Product.objects.all(),
    }
    return render(request, 'mainapp/products.html', context=context)


def temp(request):
    context = {
        "name": "Santion",
        "friends": ["shamil", "misha", "bylik", 'some girl of my friend in intra']
    }
    return render(request, 'mainapp/temp.html', context=context)


def test_context(request):
    context = {
        'title': "Добро пожаловать!",
        'username': 'Shamil',
        'products': [
            {'name': "Black hudi", 'price': "2000 руб"},
            {'name': "White hoodi", 'price': "3000 руб"}
        ],
        'promotion': True,
        'promotion_products': [
            {'name': "books", 'price': "10 000 руб"}
        ]
    }
    return render(request, 'mainapp/context.html', context=context)
