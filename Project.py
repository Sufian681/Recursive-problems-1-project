def extract_digits(n):
    if n < 10:
        print(n, end=" ")
    else:
        extract_digits(n // 10)
        print(n % 10, end=" ")


def reverse_num(n, rev=0):
    return rev if n == 0 else reverse_num(n // 10, rev * 10 + n % 10)


n = int(input("Enter a number: "))
extract_digits(n)
print("\nReversed number:", reverse_num(n))