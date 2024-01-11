from django.shortcuts import render


def catalog(request):
    context = {
        'title': "Услуги",
        'goods': [
            {'image': 'deps/images/goods/set of tea table and three chairs.jpg',
             'name': 'Услуга 1',
             'description': 'Описание 1',
             'price': 100.00},

            {'image': 'deps/images/goods/set of tea table and two chairs.jpg',
             'name': 'Услуга 2',
             'description': 'Описание 2',
             'price': 50.00},

            {'image': 'deps/images/goods/double bed.jpg',
             'name': 'Услуга 3',
             'description': 'Описание 3',
             'price': 200.00},

            {'image': 'deps/images/goods/kitchen table.jpg',
             'name': 'Услуга 4',
             'description': 'Описание 4',
             'price': 100.00},

            {'image': 'deps/images/goods/kitchen table 2.jpg',
             'name': 'Услуга 5',
             'description': 'Описание 5',
             'price': 210.00},

            {'image': 'deps/images/goods/corner sofa.jpg',
             'name': 'Услуга 6',
             'description': 'Описание 6',
             'price': 410.00},

            {'image': 'deps/images/goods/bedside table.jpg',
             'name': 'Услуга 7',
             'description': 'Описание 7',
             'price': 240.00},

            {'image': 'deps/images/goods/sofa.jpg',
             'name': 'Услуга 8',
             'description': 'Описание 8',
             'price': 100.00},

            {'image': 'deps/images/goods/office chair.jpg',
             'name': 'Услуга 9',
             'description': 'Описание 9',
             'price': 300.00},

            {'image': 'deps/images/goods/plants.jpg',
             'name': 'Услуга 10',
             'description': 'Описание 10',
             'price': 140.00},

            {'image': 'deps/images/goods/flower.jpg',
             'name': 'Услуга 11',
             'description': 'Описание 11',
             'price': 15.00},

            {'image': 'deps/images/goods/strange table.jpg',
             'name': 'Услуга 12',
             'description': 'Описание 12',
             'price': 245.00},
        ]
    }
    return render(request, 'services/catalog.html', context)


def product(request):
    return render(request, 'services/product.html')
