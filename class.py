# More on Functions
# - return
# - global and local variable

def profile_builder(name, age, qualification, income, **other_info):
    profile = {}
    profile = ['name'] = name
    profile = ['age'] = age
    profile = ['qualification'] = qualification
    profile = ['income'] = income
    profile = ['other_info'] = other_info
    print(name)
    print(age)
    print(qualification)
    print(income)
    print(other_info)
    print(profile)
    


profile_builder('Zuhaib',20,'Not defined','Not defined',**{'city':'Karachi','country':'Pakistan'})

def add(a,b):
    return a+b , "Hello world"

ans = add(2,3)
print(ans)


#  Salesman: commission
#  TaxCalc 
#  Payment
def taxCalc(income):
    if income >= 50000:
        return income*0.10
    elif income >= 40000:
        return income*0.05
    elif income >= 30000:
        return income*0.03
    else:
        return income*0

def commissionCalculator(units_sale):
    if units_sale >= 500:
        return 10000
    elif units_sale >= 250:
        return 5000
    elif units_sale >= 100:
        return 2000
    else:
        return 1000

def SallaryCalculator(basic, units_sale):
    commission = commissionCalculator(units_sale)
    total = basic+commission
    tax = taxCalc(total)
    net = total - tax
    return net

print(SallaryCalculator(50000,100))

def sum_list(lst):
    sq = {}
    s = 0
    for a in lst:
        s+=a
    return s 
print(sum_list([9,8,7,6,5,4,3,2,1,10]))


def max_list1(lst):
    return max(lst)

print(max_list1([12,34,222,33,255,7,55,3,99]))


def max_list(lst1):
    
    max_num = lst1[0]
    for n in lst1:
        if n > max_num:
            max_num = n



print(max_list1([12,34,23,45,65,78,90,34,2]))



class Students():
    name = 'Zuhaib'
    age = 20
    city = 'karachi'

s1 = Students()

s1.name
    