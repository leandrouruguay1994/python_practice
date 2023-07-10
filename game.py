from models.calcular import Calcular

def main() -> None:
    puntos: int = 0
    jugar(puntos)

def jugar(puntos: int) -> None:
    dificultad: int = int(input('Nivel de dificultad [1, 2, 3 o 4]: '))

    calc: Calcular = Calcular(dificultad)

    print('Informe el resultado para la siguiente operación: ')
    calc.mostrar_operacion() # 5 + 2 = ?

    resultado: int = int(input())

    if calc.check_resultado(resultado):
        puntos += 1
        print(f'Usted tiene {puntos} punto(s).')

    continuar: int = int(input('Desea continuar jugando? [1 - si, 0 - no] '))

    if continuar:
        jugar(puntos)
    else:
        print(f'Usted finalizó con {puntos} punto(s).')
        print('Hasta la próxima!')

if __name__ == '__main__':
    main()

