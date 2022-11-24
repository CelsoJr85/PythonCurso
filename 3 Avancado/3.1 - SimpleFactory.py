""" SIMPLE FACTORY """
from abc import ABC, abstractmethod

# Criando uma classe veiculo
class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self, ) -> None:
        pass

class CarroLuxo(Veiculo):
    def buscar_cliente(self, ) -> None:
        print("Carro Luxo esta procurando cliente...")

class CarroPopular(Veiculo):
    def buscar_cliente(self, ) -> None:
        print("Carro Popular esta procurando cliente...")

class VeiculoFactory:
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        assert O, 'veiculo não existe'


if __name__ == "__main__":
    from random import choice
    carros_disponiveis = ['luxo', 'popular']

    for i in range(10):
        carro = VeiculoFactory.get_carro(choice(carros_disponiveis))
        carro.buscar_cliente()