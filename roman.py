#!/usr/bin/env python3
"""
Import packages
"""


class Roman:
    """
    Manage Roman number
    """

    # /
    # Get roman number
    # parameter: roman(string)
    # Requirement: roman(string)
    # Return: It will filter the raw string to roman number
    # /
    def filter(self, roman):
        """
        M = 1000, D = 500, C = 100, L = 50, X = 10, V = 5, I = 1
        DCCCC = 500 + 100 + 100 + 100 + 100 = 900 = 1000 - 100 = CM, So replace with CM
        CCCC = 100 + 100 + 100 + 100 = 400 = 500 - 100 = CD
        LXXXX = 50 + 10 + 10 + 10 + 10 = 90 = 100 - 10 = XC
        XXXX = X + X + X + X = 10 + 10 + 10 + 10 = 40 = 50 - 10 = XL
        VIIII = 5 +1 + 1 + 1 + 1 = 9 = 10 - 1 = IX
        IIII = 1 + 1 + 1 + 1 = 4 = 5 - 1 = IV
        :param roman:
        :return:
        """
        return roman.replace("DCCCC", "CM").replace("CCCC", "CD"). \
            replace("LXXXX", "XC").replace("XXXX", "XL"). \
            replace("VIIII", "IX").replace("IIII", "IV")

    # /
    # Get roman number
    # parameter: num(int)
    # Requirement: num(int)
    # Return: It will filter the raw string to roman number
    # /
    def num_roman(self, num):
        """
        divmod():  take numerator and denominator
        it calculate both x/y and x%y and return both
        """
        if type(num) is not int:    # verify number
            raise ValueError('Non integers can not be converted')

        m, remainder = divmod(num, 1000)
        d, remainder = divmod(remainder, 500)
        c, remainder = divmod(remainder, 100)
        l, remainder = divmod(remainder, 50)
        x, remainder = divmod(remainder, 10)
        v, i = divmod(remainder, 5)
        roman_num = 'M' * m + 'D' * d + 'C' * c + 'L' * l + 'X' * x + 'V' * v + 'I' * i
        return self.filter(roman_num)


