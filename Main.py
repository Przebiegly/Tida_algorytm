import random
import string


class CodeGenerator:
    def __init__(self, length: int):
        if length not in [4, 6, 12, 16]:
            raise ValueError("Długość kodu musi wynosić 4, 6, 12 lub 16")
        self.length = length
        self.code = self.generate_code()

    def generate_code(self):
        if self.length in [4, 6]:
            return ''.join(random.choices(string.digits, k=self.length))
        else:
            return ''.join(random.choices(string.digits + string.ascii_letters, k=self.length))

    def display_code(self):
        print(f"Generowany kod: {self.code}")


try:
    generator2 = CodeGenerator(6)
    generator2.display_code()

    generator4 = CodeGenerator(16)
    generator4.display_code()

except ValueError as e:
    print(e)
