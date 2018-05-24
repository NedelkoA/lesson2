import re


class StringCalculator:
    def add(self, numbers_str):
        if numbers_str == '':
            return 0
        else:
            if re.search('//', numbers_str):
                numbers_str = numbers_str.replace('//', '')
                numbers_str = numbers_str.replace(numbers_str[0], ' ')
                numbers = numbers_str.split()
            else:
                numbers_str = numbers_str.replace(',', ' ')
                numbers = numbers_str.split()
            summa = 0
            negative_nums = ''
            for number in numbers:
                if int(number) < 0:
                    negative_nums += number+','
                elif int(number) > 1000:
                    continue
                else:
                    summa += int(number)
            if negative_nums != '':
                return 'Отрицательные числа запрещены: '+negative_nums[:-1]
            else:
                return summa
