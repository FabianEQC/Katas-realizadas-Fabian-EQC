Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    return f"El total de agua que queda después de {days_left} días es: {total_water_left} litros"
print(water_left(5, 100, 2))

def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(
            f"No hay suficiente agua para los {astronauts} astronautas después de {days_left} días!")
    return f"El total de agua que queda después de {days_left} días es: {total_water_left} litros"

water_left(5, 100, 2)

try:
    water_left(5, 100, 2)
except RuntimeError as err:
    print(err)

water_left("3", "200", None)

def water_left(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            argument / 10
        except TypeError:

            raise TypeError(
                f"Todos los argumentos deben ser de tipo int, pero se reciben: '{argument}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(
            f"No hay suficiente agua para los {astronauts} astronautas después de {days_left} días!")
    return f"El total de agua que queda después de {days_left} días es: {total_water_left} litros"
water_left("3", "200", None)