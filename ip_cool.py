
n = str(input("Enter the ip address to validate.."))

temp = n.split('.')

if len(temp)==4:
    try:
        if ((int(temp[0]) in range(0,256)) and (int(temp[1]) in range(0,256)) \
            and (int(temp[2]) in range(0,256)) and (int(temp[3]) in range(0,256))):
            print('Nice Try..!!! Valid ip address')
        else:
            print('Sorry, Invalid ip address. \nIp address is in the format of 0-255.0-255.0-255.0-255')
    except:
        print('Sorry, Invalid ip format. \nIp address is in the format of 0-255.0-255.0-255.0-255')
else:
    print('Sorry, Invalid ip address/format. \nIp address is in the format of 0-255.0-255.0-255.0-255')
