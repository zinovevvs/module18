from django.shortcuts import render
def home_view(request):
    return render(request, 'fourth_task/home.html', context={'pagename': 'Главная'})


def games_view(request):
    games = ['Atomic Heart', 'Cyberpunk 2077']
    return render(request, 'fourth_task/games.html', context={'pagename': 'Игры', 'games': games})

def cart_view(request):
    return render(request, 'fourth_task/cart.html', context={'pagename': 'Корзина'})

# Create your views here.
