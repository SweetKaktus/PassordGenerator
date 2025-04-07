import random


class Password():
    def __init__(self,
                 chars: str='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!:;,/.?ù%*$-+',
                 password_generated: str=''):
        self.chars = chars
        self.password_generated: str = password_generated

    def generate_password(self, password_strength: str) -> None:
        chars: str = self.chars
        alnum_chars: str = ''
        match password_strength:
            case 'WEAK':
                for char in chars:
                    if char.isalnum():
                        alnum_chars += str(char)
                for i in range(8):
                    self.password_generated += random.choice(alnum_chars)
            case 'MEDIUM':
                for i in range(12):
                    self.password_generated += random.choice(chars)
            case 'STRONG':
                for i in range(18):
                    self.password_generated += random.choice(chars)
            case _:
                raise ValueError


if __name__ == '__main__':
    test = Password()
    test.generate_password('g')
    print(test.password_generated)