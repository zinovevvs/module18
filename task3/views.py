from django.shortcuts import render


def home_view(request):
    return render(request, 'third_task/home.html')


def games_view(request):
    games = {
        "Игры": [
            {"title": "Atomic Heart", "button": "Купить"},
            {"title": "Cyberpunk 2077", "button": "Купить"},
            {"title": "PayDay 2", "button": "Купить"},
        ]
    }
    return render(request, 'third_task/games.html', {'games': games})


def cart_view(request):
    return render(request, 'third_task/cart.html')

