
def set_bit(num, i):
    return num | (1 << i)

def get_bit(num, i):
    return ((num & (1 << i)) != 0)


if __name__ == "__main__":
    num = 16 
    i   = 4
    print('get bit')
    print('num : ', str(num))
    print('i   : ', str(i))
    print(get_bit(num, i))

    print('set bit')
    i   = 2 
    print('i   : ', str(i))
    print(set_bit(num, i))
