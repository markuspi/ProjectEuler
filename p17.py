
ones = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

tens = {
    2: "twenty",
    3: "thirty",
    4: "fourty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninty"
}

def to_string(n):
    if n == 1000:
        return "one thousand"
    result = ""
    if n > 99:
        result += ones[n // 100] + " hundred"
        if n % 100 == 0:
            return result
        else:
            result += " and "
    n %= 100
    if n < 20:
        result += ones[n]
    elif n % 10 == 0:
        result += tens[n // 10]
    else:
        result += tens[n // 10] + "-" + ones[n % 10]
    return result

def numlen(n):
    s = to_string(n)
    return len(s.replace(" ", "").replace("-", ""))

print(sum(numlen(i) for i in range(1, 1001)))