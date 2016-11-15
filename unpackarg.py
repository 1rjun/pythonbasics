def total_price(apple,banana,orange):
    total=apple*4+banana*2+orange*5
    return total
arjun=[4,12,8]
arjun_bill=total_price(*arjun) #*arjun act as a unpacked argument of list
print(arjun_bill)
