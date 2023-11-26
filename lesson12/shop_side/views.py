from django.shortcuts import render, redirect
from shop_side.models import Product, Category, Shop


def product_create_view(request):
    context = {'category_list': Category.objects.all(),'shop_list': Shop.objects.all()}

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        category = request.POST.get('category')
        shops = request.POST.getlist('shop')


        product = Product()
        product.name = name
        product.price = price
        product.quantity = quantity
        product.category = Category.objects.get(
            pk=category
        )
        product.save()
        for shop in shops:
            product.shop.add(Shop.objects.get(pk=shop))
        return redirect('product_list')

    return render(request,
                  'shop_side/product_create.html',
                  context)


def product_delete_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    product.delete()

    return redirect('product_list')


def product_update_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)

    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        category = request.POST.get('category')
        shops = []
        for i in range(Shop.objects.count()):
            shops.append(request.POST.get(f'{i+1}', True))
        print(shops)

        product.name = name
        product.price = price
        product.quantity = quantity
        product.category = Category.objects.get(
            pk=category
        )
        product.save()
        for i in range(len(shops)):
            if shops[i] == True :
                product.shop.remove(Shop.objects.get(pk=(i+1)))
            else:
                product.shop.add(Shop.objects.get(pk=i+1))



        return redirect('product_list')


    context = {
        'product': product,
        'category_list': Category.objects.all(),
        'shop_list': Shop.objects.all()

    }
    return render(request,
                  'shop_side/product_update.html',
                  context)









