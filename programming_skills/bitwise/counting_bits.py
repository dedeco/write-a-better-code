def count_bits(x):
    qty_ones = 0
    while x:
        qty_ones += x & 1
        x >>= 1
    return qty_ones


if __name__ == "__main__":
    print(count_bits(13))
