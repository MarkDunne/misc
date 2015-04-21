grid1 = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'


# grid string -> dict([(x, y) -> Square])
def parse_grid(grid_str):
    res = dict()
    for pos, value in enumerate(grid_str):
        x, y = pos % 9, pos / 9
        res[(x, y)] = Square(int(value), x, y)
    return res


def display(grid_dict):
    output = []
    for y in range(9):
        if y % 3 == 0 and y > 0:
            output.append('---------+---------+---------\n')
        for x in range(9):
            if x % 3 == 0 and x > 0:
                output.append('|')
            output.append(' ' + str(grid_dict[(x, y)]) + ' ')
        output.append('\n')
    print ''.join(output)


class Square():

    def __init__(self, value, x, y):
        self.x = x
        self.y = y
        self.init_value = value

        self.box_unit = [1.0 / 9.0] * 9
        self.row_unit = [1.0 / 9.0] * 9
        self.col_unit = [1.0 / 9.0] * 9

        if value != 0:
            self.update_all_units(value, 1.0)

    def update_all_units(self, value, prob):
        self.box_unit = self.update_unit(value, prob, self.box_unit)
        self.row_unit = self.update_unit(value, prob, self.row_unit)
        self.col_unit = self.update_unit(value, prob, self.col_unit)

    def update_unit(self, value, prob, unit):
        unit = map(lambda prob: prob + unit[value - 1] / 8, unit)
        unit[value - 1] = prob
        return unit

    def __str__(self):
        if self.init_value == 0:
            return '.'
        else:
            return str(self.init_value)


display(parse_grid(grid1))

d = parse_grid(grid1)

print d[(0, 0)]
print d[(1, 0)]
print d[(2, 0)]
