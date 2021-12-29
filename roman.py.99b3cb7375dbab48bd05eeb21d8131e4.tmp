class Interval:
    def __init__(self, n):
        # 781 => 10 ** (len('781') - 1) => 10 ** 2
        ten_power = int(10 ** (len(str(n)) - 1))

        self.start = 1 * ten_power
        self.mid = 5 * ten_power
        self.end = 10 * ten_power


symbols = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M",
}


def decompose(n):
    n_to_str = str(n)
    decomposition = []

    for i in range(len(n_to_str)):
        number = n_to_str[i]
        zeroes = '0' * (len(n_to_str) - (i + 1))
        new_number = int(number + zeroes)

        if new_number > 0:
            decomposition.append(new_number)
    return decomposition


def romanize(val):
    itv = Interval(val)

    # More than a thousand
    if val >= 1000:
        return "M" * int(val / 1000)

    # Less than a thousand
    itv_symbol = {
        "start": symbols[itv.start],
        "mid": symbols[itv.mid],
        "end": symbols[itv.end],
    }
    times = int(val / itv.start)

    if val == (itv.mid - itv.start):
        return itv_symbol["start"] + itv_symbol["mid"]
    elif val == (itv.end - itv.start):
        return itv_symbol["start"] + itv_symbol["end"]
    elif val < itv.mid:
        return itv_symbol["start"] * times
    elif val == itv.mid:
        return itv_symbol["mid"]
    elif val > itv.mid:
        return itv_symbol["mid"] + (itv_symbol["start"] * (times - 5))
    else:
        return ""


def from_numeral_to_roman(n):
    # Guard
    if n > 99999:
        return "Value should be less than 99999."

    decomposition = decompose(n)
    roman = ''

    for compo in decomposition:
        roman += romanize(int(compo))

    return roman


# Test
test_suite = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
              10, 20, 30, 40, 50, 60, 70, 80, 90,
              100, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000,
              2022, 99999]

for test in test_suite:
    print(from_numeral_to_roman(test))
