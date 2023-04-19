from funciones import reescribir_archivo, get_values_list
from AFN import regex_to_enfa, enfa_to_graphviz, generate_mega_enfa_graph

def main():
    file_name = "Ejemplo1.txt"

    with open(file_name, "r") as file:
        input_text = file.read()

    rewritten_text = reescribir_archivo(input_text)
    
    if rewritten_text is None:
        print("Se detectaron errores en el archivo de entrada. Por favor, corrige los errores e intenta nuevamente.")
        return

    print("Yalex nuevo\n" + rewritten_text)

    resultado = get_values_list(rewritten_text)
    print("Resultados:")
    print(resultado)
    
    enfas = [regex_to_enfa(regex) for regex in resultado]

# Modificar el diccionario de categorías para tener conjuntos como claves
    categorias = {
        '0|1|2': "numero",
        'a|b|c|A|B|C': "letra"
    }


    enfas = [regex_to_enfa(regex) for regex in resultado]

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
