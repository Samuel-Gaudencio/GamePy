from calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:

    dificuldade: int = int(input(f'Infome o nivel de dificuldade desejado [1, 2, 3 ou 4]: '))

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado da seguinte operação: ')
    calc.mostrar_operacao()

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} ponto(s)')

    continuar: int = int(input('Deseja continuar [1 - sim, 0 - não]: '))

    if continuar:
        jogar(pontos)
    else:
        print(f'Voce finalizou com {pontos} ponto(s)')
        print('Até a proxima!')


if __name__ == '__main__':
    main()

