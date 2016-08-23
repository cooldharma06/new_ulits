
import re

n = str(input("Enter the ip address to validate.."))


''' this one using normal range validation and the performance will lack.
    So going for REGULAR Expression
'''
'''
temp = n.split('.')
if len(temp)==4:
    try:
        if ((int(temp[0]) in range(0,256)) and (int(temp[1]) in range(0,256)) and (int(temp[2]) in range(0,256)) and (int(temp[3]) in range(0,256))):
            print('Nice Try..!!! Valid ip address')
        else:
            print('Sorry, Invalid ip address. \nIp address is in the format of 0-255.0-255.0-255.0-255')
    except:
        print('Sorry, Invalid ip format. \nIp address is in the format of 0-255.0-255.0-255.0-255')
else:
    print('Sorry, Invalid ip address/format. \nIp address is in the format of 0-255.0-255.0-255.0-255')
'''

print(n)

# this is the generalised form of regular expression and based on the range we needs
#0.0.0.0 to 255.255.255.255
#for the fixed range means we have to rearrange(fix) the [0-9] tokens

pattern = r'(((^[1][0-9][0-9])|(^[2][0-4][0-9])|(^[2][0-5][0-5])|(^[0-9][0-9])|(^[0])|(^[0-9]))\.(([1][0-9][0-9])|([2][0-4][0-9])|([2][0-5][0-5])|([0-9][0-9])|([0])|([0-9]))\.(([1][0-9][0-9])|([2][0-4][0-9])|([2][0-5][0-5])|([0-9][0-9])|([0])|([0-9]))\.(([1][0-9][0-9])|([2][0-4][0-9])|([2][0-5][0-5])|([0-9][0-9])|([0])|([0-9])))'

if re.match(pattern,n):
    print('Nice try..!! it\'s an ip address')
else:
    print('Sorry, its not matching. please try again')


'''
Sample result:

>>> ================================ RESTART ================================
>>> 
Enter the ip address to validate..0.0.125.36
0.0.125.36
Nice try..!! it's an ip address
>>> ================================ RESTART ================================
>>> 
Enter the ip address to validate..#.23.67.9
#.23.67.9
Sorry, its not matching. please try again

'''
