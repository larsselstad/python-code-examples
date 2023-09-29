def pow_arr(arr, exponent):
    values = []
    for x in arr:
        p = 1
        for _ in range(exponent):
            p *= x
        values.append(p)
    return values


def pow_arr_generator(arr, exponent):
    for x in arr:
        p = 1
        for _ in range(exponent):
            p *= x
        yield p

arr = range(10)

print(pow_arr(arr, 3))


# to use the generator
# this only returns the generator
print(pow_arr_generator(arr, 3))
# use list comprehension to get values
print([a for a in pow_arr_generator(arr, 3)])
