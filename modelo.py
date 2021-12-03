class Programa:
    def __init__(self, nome: str, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome: str):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'{self._nome} -  {self.ano} - {self._likes} Likes'


class Filme(Programa):
    def __init__(self, nome: str, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return  f'{self._nome} -  {self.ano} - {self.duracao} min -  {self._likes} Likes'


class Serie(Programa):
    def __init__(self, nome: str, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} -  {self.ano} - {self.temporadas} temporadas -  {self._likes} Likes'

class PlayList:
    def __init__(self, nome, programas):
        self.nome = nome
        self.programas = programas

    def tamanho(self):
        return len(self.programas)


vingadores = Filme('Vingadores - Guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme("Todo mundo em pânico", 1999,100)
demolidor = Serie("Demolidor", 2016,2)

vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = PlayList("Fim de semana", filmes_e_series)

for programa in playlist_fim_de_semana.programas:
    print(programa)
