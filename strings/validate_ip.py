### COPIED ###
def validate_ip(ip):
    ip = [int(token) for token in ip.split('.')]

    if len(ip) != 4:
        print('not ip')
        return

    for num in ip:
        if 0 <= num <= 255:
            continue
        print('not ip')
        return

    print('is ip')



if __name__ == '__main__':
    validate_ip('100.255.153.12')