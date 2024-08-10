class Conversor:
    def __init__(self):
        self.valores_decimais = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        self.simbolos_romanos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    def decimal_para_romano(self, num):
        numero_romano = ''
        i = 0
        while num > 0:
            for _ in range(num // self.valores_decimais[i]):
                numero_romano += self.simbolos_romanos[i]
                num -= self.valores_decimais[i]
            i += 1
        return numero_romano