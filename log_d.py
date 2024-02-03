def AND(v1A = 0, v2A = 0):
    And = 0
    if v1A == 1 and v2A == 1:
        And = 1
    else:
        And = 0
    return And

def OR(v1O = 0, v2O = 0):
    Or = 0
    if v1O == 1 or v2O == 1:
        Or = 1
    else:
        Or = 0
    return Or

def NOT(v1N = 0):
    Not = 0
    if v1N == 1:
        Not = 0
    else:
        Not = 1
    return Not

def NAND(v1N = 0, v2N = 0):
    Nand = 0
    if v1N == 1 and v2N == 1:
        Nand = 0
    else:
        Nand = 1
    return Nand

def XOR(v1X = 0, v2X = 0):
    Xor = 0
    if v1X == 1 and v2X == 1:
        Xor = 0
    elif v1X == 1 or v2X == 1:
        Xor = 1
    else:
        Xor = 0
    return Xor

def NOR(v1NO = 0, v2NO = 0):
    Nor = 0
    if v1NO == 0 and v2NO == 0:
        Nor = 1
    else:
        Nor = 0
    return Nor

def XNOR(v1XNO = 0, v2XNO = 0):
    Xnor = 0
    if v1XNO == 0 and v2XNO == 0 or v1XNO ==1 and v2XNO ==1:
        Xnor = 1
    else:
        Xnor = 0
    return Xnor

def CODIFICADOR(entrada = 0):
    formato_binario = '{0:00b}'
    salida_binaria = formato_binario.format(entrada)
    salida_entero = int(salida_binaria)
    return salida_entero

def DECODIFICADOR(entrada_binaria = 0, salidas = 0):
    int_binario = entrada_binaria
    str_binario = str(int_binario)
    decimal = int(str_binario, 2)
    if decimal < len(salidas):
        return salidas[decimal]
    else:
        return "Error: Entrada fuera de rango"

def MUX(dat_a = 0, dat_b = 0, selector = 0):
    if selector == 0:
        return dat_a
    elif selector == 1:
        return dat_b
    else:
        return "Error: selector no valido"

state = 0
def FLIPFLOP(input_value = 0, clock = 0):
    global state
    if clock == 1:
        state = input_value
        return state

def DMUX(input_signal, control):
    if control == 0:
        output_0 = input_signal
        output_1 = 0
    else:
        output_0 = 0
        output_1 = input_signal
    return output_0, output_1

def CONTADOR(inicio, fin, paso, ascendente=True):
    if ascendente:
        return list(range(inicio, fin + 1, paso))
    else:
        return list(range(fin, inicio - 1, - paso))