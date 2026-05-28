#  Calculate interest using the standard formula.
# S.I = Principal * Rate * Time / 100

def si_calc(p, r, t):
    si = p*r*t/100
    return si

while True:
    try:
        # print("Enter the space seperated values of principal, rate, time :", end=" ")
        # p, r, t = map(float, input().split())
        p = float(input("Enter principal amount : "))
        r = float(input("Enter Rate : "))
        t = float(input("Enter time in years : "))
        print(f"Calclated Simple Interest is: {si_calc(p,r,t)}")
    except ValueError:
        print("Values must be numbers.")
        continue
    
    query = input("Do you want to continue? (y/n) ").lower()
    if query == 'n':
        break