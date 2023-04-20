from funciones import reescribir_archivo, get_values_list, get_variable_names
from AFN import regex_to_enfa, enfa_to_graphviz, generate_mega_enfa_graph

def main():
    yalex_file_name = "EjemploYalex.txt"
    input_file_name = "archivo_entrada.txt"

    with open(yalex_file_name, "r") as file:
        yalex_text = file.read()

    with open(input_file_name, "r") as file:
        input_text = file.read()

    rewritten_text = reescribir_archivo(yalex_text)

    if rewritten_text is None:
        print("Se detectaron errores en el archivo de entrada. Por favor, corrige los errores e intenta nuevamente.")
        return

    variable_names = get_variable_names(rewritten_text)
    resultado = get_values_list(rewritten_text)

    enfas = [regex_to_enfa(regex) for regex in resultado]

    # Modificar el diccionario de categorías para tener conjuntos como claves
    # categorias = {
    #     resultado[0]: "entero",
    #     resultado[1]: "decimal",
    #     resultado[2]: "hexadecimal",
    #     resultado[3]: "operador",
    #     resultado[4]: "potenciacion",
    #     resultado[5]: "tabulaciones"
    # }
    categorias = {}
    for i, var_name in enumerate(variable_names):
        if i < len(resultado):
            categorias[resultado[i]] = var_name

    # Graficar y guardar ENFA individuales con identificadores según categorías
    identifiers = [categorias.get(regex, "Desconocido") for regex in resultado]

    for idx, enfa in enumerate(enfas):
        identifier = identifiers[idx]
        enfa_graph = enfa_to_graphviz(enfa, identifier)
        enfa_graph.render(f"enfa_output_{idx}", view=True)

    # Generar y guardar el mega autómata con identificadores según categorías
    mega_enfa_graph = generate_mega_enfa_graph(enfas, identifiers)
    mega_enfa_graph.render("mega_enfa_output", view=True)

if __name__ == "__main__":
    main()
