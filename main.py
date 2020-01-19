class Function(object):
    def __init__(self):
        self.function = {}

    def print(self, i):
        print()
        print("# Функция {} #".format(i))
        for input, output in self.function.items():
            print("{} => {}".format(input, output))

    # сбалансированность
    def is_balance(self):
        r = 0
        for input, output in self.function.items():
            if output == '0':
                r += 1
            else:
                r -= 1
        return r == 0

    # полином жегалкина
    def polinom(self):
        all_blocks = []

        def multiple(p1, p2):
            res = []
            for e1 in p1:
                for e2 in p2:
                    if e1 == "1" and e2 == "1":
                        res.append("1")
                    elif e1 == "1":
                        res.append(e2)
                    elif e2 == "1":
                        res.append(e1)
                    else:
                        res.append("{}{}".format(e1, e2))
            return res

        for input, output in self.function.items():
            if output == '1':
                blocks = []
                for i, symb in enumerate(input):
                    if symb == '1':
                        blocks.append(["x{}".format(i + 1)])
                    else:
                        blocks.append(["1", "x{}".format(i + 1)])
                while len(blocks) > 1:
                    blocks[1] = multiple(blocks[0], blocks[1])
                    del blocks[0]
                all_blocks.extend(blocks[0])
        res = []
        for object in set(all_blocks):
            if all_blocks.count(object) % 2 == 1:
                res.append(object)
        return " + ".join(res)

    # степень - максимальная степень монома среди всех мономов в полиноме жегалкина
    def degree(self):
        monoms = self.polinom().split(" + ")
        degree = 0
        for monom in monoms:
            degree = max(degree, monom.count("x"))
        return degree


def expand(res, size):
    while len(res) < size:
        res = "0" + res
    return res


def convert_to_2(fr, num, symb):
    res = str(bin(int(str(num), fr)))[2:]
    return expand(res, symb)


def main():
    table = []
    with open("in.txt") as f:
        line = f.readline()
        while line:
            table.append(line.replace('\n', '').split(' '))
            line = f.readline()

    functions = []
    # генерация функций
    for S_num, k in enumerate(table):
        f_part = []
        for i in range(4):
            f_part.append(Function())

        for i, block in enumerate(k):
            input = convert_to_2(10, i, 4)
            output = convert_to_2(16, k[i], 4)

            for i, symb in enumerate(output):
                f_part[i].function[input] = symb
        functions.extend(f_part)

    print("Начинаем исследование таблицы замен с помощью 32 булевых функций")

    for i, function in enumerate(functions):
        function.print(i)
        print("Сбалансированность:", function.is_balance())
        print("Полином Жегалкина:", function.polinom())
        print("Степень:", function.degree())


if __name__ == "__main__":
    main()
