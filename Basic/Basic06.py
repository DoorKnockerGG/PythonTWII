

if __name__ == '__main__':
    amount = 83
    feet = 240
    """
    83 * 2 = 166
    240 - 166 = 74 <-- rabbits feet
    74/2 = 37
    83 - 37 = 46
    """
    if amount * 2 <= feet <= amount *4:
        rabbits = (feet - amount * 2)/(4-2)
        chicken = 83 - rabbits
        print('rabbits=', rabbits, 'chicken=', chicken)
    else:
        print('Question setting error.')
