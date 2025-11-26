import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--nombre")
parser.add_argument("--apellidos")

args = parser.parse_args()
print(args)

diccionario = vars(args)
print(diccionario)
