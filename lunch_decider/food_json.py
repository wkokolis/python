#!/usr/bin/python

def mylunch():

    import random
    import json

    ## Define the list of restaurants
    food = ['Apollo\'s',
        'Arby\'s',
        'B-dubs',
        'Bon Chon',
        'Buzz and Ned\'s',
        'Casa Grande',
        'Chaddar Thai',
        'Chick-fil-A',
        'Chipotle',
        'Christian\'s Pizza',
        'Dot\'s Back Inn',
        'Einstein Brother\'s Bagels',
        'El Jeffe',
        'Firehouse Subs',
        'Five Guys',
        'Home',
        'Kabab Bistro',
        'La Cabana',
        'Los Pollos Hermanos',
        'Mai Sushi',
        'Mekong',
        'Metro Diner',
        'Mission BBQ',
        'Noodles and Company',
        'Pho So 1',
        'Pho Tay Do',
        'Plaza Azteca',
        'Sonic',
        'Toast',
        'WaWa']

    ## Pick one and print to STDOUT as JSON
    secure_random = random.SystemRandom()
    print({'statusCode': 200, 'headers': { 'Content-Type': 'application/json' }, 'body': json.dumps({ 'Destination': secure_random.choice(food)})})
    return

mylunch()
