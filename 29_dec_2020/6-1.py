def in_IP_range(number):
    return number >= 0 and number <= 255


def number_with_leading_zeros(number):
    return str(int(number)) != number


def ip_addresses(number):
    results = []
    ptr1, ptr2, ptr3 = 1, 2, 3

    while True:
        if not in_IP_range(int(number[:ptr1])) or number_with_leading_zeros(number[:ptr1]):
            break
        elif not in_IP_range(int(number[ptr1:ptr2])) or number_with_leading_zeros(number[ptr1:ptr2]):
            ptr1 += 1
        elif not in_IP_range(int(number[ptr2:ptr3])) or number_with_leading_zeros(number[ptr2:ptr3]):
            ptr2 += 1
        elif not in_IP_range(int(number[ptr3:])) or number_with_leading_zeros(number[ptr3:]):
            ptr3 += 1
        else:
            results.append('{}.{}.{}.{}'.format(
                number[0:ptr1], number[ptr1:ptr2], number[ptr2:ptr3], number[ptr3:]))
            if ptr3 != len(number) - 1:
                ptr3 += 1
            elif ptr2 != len(number) - 2:
                ptr2 += 1
            elif ptr1 != len(number) - 3:
                ptr1 += 1
            else:
                break

    return results


print(ip_addresses('1592551013'))
print(ip_addresses('10000'))
print(ip_addresses('127001'))
