def is_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    h = max(a, b, c)
    ss = [i for i in [a, b, c] if i != h]
    return h ** 2 == ss[0] ** 2 + ss[1] ** 2

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b