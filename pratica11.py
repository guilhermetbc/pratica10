class Autor:
  def __init__(self, primeironome, ultimonome, datanascimento, nomedomeio = ''):
    self.primeironome = primeironome
    self.nomedomeio = nomedomeio
    self.ultimonome = ultimonome
    self.datanascimento = datanascimento

  @property
  def nome_como_citado(self):
    return "{} {}.".format(self.ultimonome.upper(), self.primeironome[0])

  def __str__(self):
    return "Autor: " + str({self.nome_como_citado})

class Livro():
  def __init__(self, titulo, ano, autores=[]):
    self.titulo = titulo
    self.ano = ano
    self.autores = autores

  @property
  def titulo(self):
    return self._titulo

  @titulo.setter
  def titulo(self, val):
    if not val:
      raise ValueError("Erro: O titulo do livro não pode ser vazio")
    self._titulo = val

  def __str__(self):
    return "Livro: " + str({self.titulo})

class Biblioteca:
  def __init__(self, livros):
    self.livros = livros

  @property
  def livros_por_autor(self):
    livrosdoautor = {}
    for livro in self.livros:
      for autor in livro.autores:
        if not livrosdoautor.get(autor.nome_como_citado):
          livrosdoautor[autor.nome_como_citado] = []
        livrosdoautor[autor.nome_como_citado].append(livro)
    return livrosdoautor
  
  def __str__(self):
    return "Biblioteca: " + str(self.livros_por_autor)

def main():
  autor1 = Autor('Carlos', 'de Andrade', '31/10/1902', nomedomeio='Drummond')
  autor2 = Autor('Machado', 'de Assis', '21/06/1839')
  autor3 = Autor('Fernado', 'Pessoa', '13/06/1888')
  
  livro1 = Livro(titulo = 'Livro 1', ano = 1940, autores = [autor1, autor2])
  livro2 = Livro(titulo = 'Livro 2', ano = 1950, autores = [autor3])
  try:
    livro3 = Livro(titulo = '', ano = 1960, autores = [autor1])
  except ValueError as e:
    print(e)

  biblioteca = Biblioteca(livros = [livro1, livro2])

  print("\n")
  print(autor1)
  print(autor2)
  print(autor3)

  print("\n")
  print(livro1)
  print(livro2)

  print("\n")
  print(biblioteca.livros_por_autor)  

if __name__ == '__main__':
  main()