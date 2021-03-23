import sys, random

first = ('Baby Oil1', "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
         'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield', 'Chewy',
         'Chigger", "Cinnabuns', 'Cleet', 'Huggy', 'Ignatious', 'Jimbo',
         "Joe 'Pottin Soil'", 'Johnny', 'Lemongrass', 'Lil Debil', 'Longbranch',
         '"Lunch Money"', 'Mergatroid', '"Mr Peabody"', 'Oil-Сап', 'Oinks',
         'Old Scratch', 'Ovaltine', 'Pennywhistle', 'Pitchfork Ben',
         'Potato Bug', 'Pushmeet', 'Rock Candy', 'Schlomo')

last = ('Baby Oil1', "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
        'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield', 'Chewy',
        'Chigger", "Cinnabuns', 'Cleet', 'Huggy', 'Ignatious', 'Jimbo',
        "Joe 'Pottin Soil'", 'Johnny', 'Lemongrass', 'Lil Debil', 'Longbranch',
        '"Lunch Money"', 'Mergatroid', '"Mr Peabody"', 'Oil-Сап', 'Oinks',
        'Old Scratch', 'Ovaltine', 'Pennywhistle', 'Pitchfork Ben',
        'Potato Bug', 'Pushmeet', 'Rock Candy', 'Schlomo')

print('Welcome to "Project_1"\n')

while True:
    firstName = random.choice(first)
    lastName = random.choice(last)

    fullName = firstName + lastName

    print('\nYour random name is: {}\n'.format(fullName), file=sys.stderr)

    try_again = input('One more time?(Enter E (enter) or N (for exit))\n')
    if try_again.lower() == 'n':
        break

print('\nEnd programme')
