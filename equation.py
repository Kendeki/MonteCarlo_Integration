class Equation():
    def __init__(self, *args):
        self.coeficients = args[:]
        self.degree = len(args)-1

    def __str__(self):
        string = ''
        temporary_list = []

        for i in range(self.degree, -1, -1):
            temp_string = ''
            if self.coeficients[self.degree-i] != 1 and i != 0:
                temp_string += f"{self.coeficients[self.degree-i]}"
            if i > 1:
                temp_string += f"x^{i}"
            elif i == 1:
                temp_string += f"x"
            else:
                temp_string += f"{self.coeficients[self.degree-i]}"

            temporary_list.append(temp_string)
        string = " + ".join(temporary_list)

        return string

    def solve(self, x):
        y = 0

        for i in range(self.degree, -1, -1):
            y += self.coeficients[self.degree-i]*(x**i)

        return y
    
    def y_values(self, x_values):
        return tuple(self.solve(x) for x in x_values)