# Crea un script que le pida al usuario una lista de paises (separados por comas).
# Estos se deben almacenar en una lista. No deberia haber países repetidos (haz uso de set).
# Finalmente, muestra por consola la lista de países ordenados alfabeticamente y separados por comas.


def split_and_strip(countries):
    return [country.strip() for country in countries.title().split(',')]


def convert_to_set_and_sort(countries_list):
    return sorted(set(countries_list))


countries = input("Escribe paises separados por comas: ")
result = split_and_strip(countries)
sorted_result = convert_to_set_and_sort(result)
print(sorted_result)
