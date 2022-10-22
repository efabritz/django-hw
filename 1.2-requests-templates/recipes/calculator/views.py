from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def home(request):
    context = {
        'data': DATA,
    }
    return render(request, 'home.html', context)

def find_recipe(request, recipe):
    amount = int(request.GET.get('servings', 1))
    recipe.update((key, value * amount) for key, value in recipe.items())

    context = {
        'recipe': recipe
    }

    return render(request, 'calculator/index.html',context)

def omlet(request):
    recipe = DATA['omlet']
    return find_recipe(request, recipe)

def pasta(request):
    recipe = DATA['pasta']
    return find_recipe(request, recipe)

def buter(request):
    recipe = DATA['buter']
    return find_recipe(request, recipe)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
