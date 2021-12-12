import math

if __name__ == '__main__':
    r = 123
    # 球圓面積 & 球體積 (利用 math api 取得圓周率)
    area = math.pi * math.pow(r, 2)
    ball = 4 / 3 * math.pi * math.pow(r, 3)

    print('area = %.2f' % area)
    print('ball = %.2f' % ball)

    # 加上千分位
    area = format(float('%.2f' % area), ',')
    print(area)

