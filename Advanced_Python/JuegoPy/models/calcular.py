from random import randint

class Calcular:

    def __init__(self: object, dificultad: int, /) -> None:
        self.__dificultad: int = dificultad
        self.__valor1: int = self._generar_valor
        self.__valor2: int = self._generar_valor
        self.__operacion: int = randint(1, 3) # 1 = sumar, 2 = restar, 3 = multiplicar
        self.__resultado: int = self._generar_resultado

    @property
    def dificultad(self: object) -> int:
        return self.__dificultad

    @property
    def valor1(self: object) -> int:
        return self.__valor1

    @property
    def valor2(self: object) -> int:
        return self.__valor2

    @property
    def operacion(self: object) -> int:
        return self.__operacion

    @property
    def resultado(self: object) -> int:
        return self.__resultado

    def __str__(self: object) -> str:
        opr: str = ''
        if self.operacion == 1:
            opr = 'Sumar'
        elif self.operacion == 2:
            opr = 'Restar'
        elif self.operacion == 3:
            opr = 'Multiplicar'
        else:
            opr = 'Operación desconocida'
        return f'Valor 1: {self.valor1} \nValor2: {self.valor2} \nDificultad: {self.dificultad} \nOperación: {opr}'

    @property
    def _generar_valor(self: object) -> int:
        if self.dificultad == 1:
            return randint(0, 10)
        elif self.dificultad == 2:
            return randint(0, 100)
        elif self.dificultad == 3:
            return randint(0, 1000)
        elif self.dificultad == 4:
            return randint(0, 10000)
        else:
            return randint(0, 100000)

    @property
    def _generar_resultado(self: object) -> int:
        if self.operacion == 1: # sumar
            return self.valor1 + self.valor2
        elif self.operacion == 2: # restar
            return self.valor1 - self.valor2
        else: # multiplicar
            return self.valor1 * self.valor2

    @property
    def _op_simbolo(self: object) -> str:
        if self.operacion == 1:
            return '+'
        elif self.operacion == 2:
            return '-'
        else:
            return '*'

    def check_resultado(self: object, respuesta: int) -> bool:
        correcto: bool = False

        if self.resultado == respuesta:
            print('Respuesta correcta!')
            correcto = True
        else:
            print('Respuesta incorrecta')
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado}')
        return correcto

    def mostrar_operacion(self: object) -> None:
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = ?')

