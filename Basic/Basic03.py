import math

if __name__ == '__main__':
    price_before = 10
    amount = 10
    value_B = amount * 1000 * price_before
    fee_B = math.floor(value_B * (1.425 / 1000)) if value_B * (1.425 / 1000) > 20 else 20
    cost_total = value_B + fee_B
    print(value_B, fee_B, cost_total)

    price_after = 11
    value_A = amount * 1000 * price_after
    fee_A = math.floor(value_A * (1.425 / 1000)) if value_A * (1.425 / 1000) > 20 else 20
    tax = math.ceil(value_A * (3 / 1000))
    ern = value_A - (value_B + fee_B + fee_A + tax)
    print(value_A, 'fee=', fee_A, 'tax=', tax)
    print('profit=', ern)
