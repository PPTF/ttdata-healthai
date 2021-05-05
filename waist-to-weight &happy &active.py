##waist to weight  number = waist/weight
number=float(input())

def waist_weight(number):
    if number<0.2 or number>0.8:
        print('potential error input')
    elif 0.4 <= number < 0.5:
        print('green')
    elif 0.5 <= number <0.6:
        print('yellow')
    elif number<0.4 or number >= 0.6 :
        print('red')

waist_weight(number)

## happies index  
hi=int(input())

def happies_index(hi):
    if hi>10 :
        print('error input')
    elif 7 < hi <= 10:
        print('green')
    elif 4 < hi <= 6:
        print('yellow')
    elif hi<= 3 :
        print('red')

happies_index(hi)

##active index  
hi=int(input())

def active_index(ai):
    if ai>10 :
        print('error input')
    elif 7 < ai <= 10:
        print('green')
    elif 4 < ai <= 6:
        print('yellow')
    elif ai<= 3 :
        print('red')

active_index(hi)