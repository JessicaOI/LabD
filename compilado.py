import re

entero = r"0|1|2|3|4|5|6|7|8|9"
decimal = r"(0|1|2|3|4|5|6|7|8|9)\.(0|1|2|3|4|5|6|7|8|9)"
hexadecimal = r"0[xX][0-9a-fA-F]+"
operador = r"\+|\-|\*"
potenciacion = r"\^"
tabulaciones = r"\t|\n "

# Compilaci�n de todas las expresiones regulares en una sola expresi�n
expresion_total = re.compile(f"({entero}|{decimal}|{hexadecimal}|{operador}|{potenciacion}|{tabulaciones})")
print(expresion_total)

# Analizar el archivo de entrada
archivo_entrada = "10 20.5 0xA1B2 + - * / ^42 3.14 0x12345 * / ^ + -"

def analizar(entrada):
    tokens = expresion_total.finditer(entrada)
    for token in tokens:
        match = token.group()
        if re.match(entero, match):
            print(f"Entero: {match}")
        elif re.match(decimal, match):
            print(f"Decimal: {match}")
        elif re.match(hexadecimal, match):
            print(f"Hexadecimal: {match}")
        elif re.match(operador, match):
            print(f"Operador: {match}")
        elif re.match(potenciacion, match):
            print(f"Potenciacion: {match}")
        elif re.match(tabulaciones, match):
            print(f"Tabulaciones: {match}")
        else:
            print(f"No reconocido: {match}")

analizar(archivo_entrada)
