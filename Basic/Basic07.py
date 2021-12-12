def getRabbitAndChicken(amount, feet):
    if amount * 2 <= feet <= amount * 4:
        rabbits = (feet - amount * 2) / (4 - 2)
        chicken = amount - rabbits
        return rabbits, chicken
    else:
        print('Question setting error.')


if __name__ == '__main__':
    amount = 83
    feet = 240
    ra, ch = getRabbitAndChicken(amount, feet)
    print(ra, ch)
