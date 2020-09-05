# Worked exercise 4.6
# Pay Computation: 1.5 * rate when overwork < 40
# worked hours = 45
# rate = 10
# answer = 475

def computepay(hours, rate):
    print('in computepay:', hours, rate)

    print('''
    HOURS = %d
    RATE = %d
    '''%(hours, rate))

    if hours <= 40.0:
        pay = hours * rate
    elif hours > 40.0:
        overhourPay = (hours-40)*(rate*0.5)
        regPay = hours * rate
        pay = overhourPay + regPay
    print('RETURNING: '+ str(pay))
    return(pay)

while True:
    hours = input('HOURS: ')
    rate = input('RATE: ')
    try:
        fh = float(hours)
        fr = float(rate)
        break
    except ValueError:
        print('PLEASE TYPE IN A VALID NUMBER.')
        continue

xp = computepay(fh, fr)
print('Pay:', xp)
