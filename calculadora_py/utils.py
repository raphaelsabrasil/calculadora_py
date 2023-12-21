import re       # import expressão regular

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')      # começa com e termina ^[]$ , apenas um caracter, como a calculadora.

def isNumOrDot(string: str):    # é número ou ponto
    return bool(NUM_OR_DOT_REGEX.search(string))

def converToNumber(string:str):
    number = float(string)

    if number.is_integer():
        number = int(number)
    
    return number

# para saber nº válido, converte string para float
def isValidNumber(string: str):     # é número válido
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False
    return valid


def isEmpty(string: str):       # é vazio
    return len(string) == 0