def get_description(): # смотрите строку документации
    """Return random weather, just like the pros"""

    from random import choice
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilities)
