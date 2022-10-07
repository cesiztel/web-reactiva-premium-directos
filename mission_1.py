"""
   Misión 1

   ¡Bienvenido agente!. La función get_flagged_cells esta sacada directamente
   del libro Clean Code. En este libro nos muestran el código de esa
   función, nos comenta por qué el código tiene problemas y nos muestra
   la versión final. Para esta misión vamos a refactorizar paso a paso
   mientras mostramos unos principios de Clean Code y Refactring. 
   Para hacer el ejemplo más completo he creado un poco de código extra 
   para darle la forma de una clase de una aplicación real.

   1. Reveal intention and rename variables
      Por el contexto del código podemos intuir lo que tiene
      que hacer el código, pero el código no es directo y
      expresivo. theList no nos dice que estamos manejando,
      list tampoco nos dice que contendrá y x no nos da
      ninguna información. Nombrar elementos del código (variables, classes, etc)
      es una actividad muy complicada, pero siempre que esos elementos
      tengan nombres que revelen la intención de ese elemento, nuestro
      código será mucho más claro de leer.

      Acciones:
      - Por el contexto podemos averiguar que `theList` es algún tipo
      de board. Renombramos las ocurrencias de `theList` por `board`
      - Por el nombre de la función `get_flagged_cells` podemos
      saber que lo que devuelve es la lista de las flagged_cells, por
      lo que tiene sentido renombrar las ocurrencias de `list` 
      por `flagged_cells`. 
      - Si `get_flagged_cells` devuelve una lista de flagged_cells, 
      entonces x que está en un loop será una cell de ese board.
      Por lo que renombramos las ocurrencias de `x` por `cell`
"""
class Game:
    def __init__(self):
        self.board = [[0, 0, 2], [0, 1, 2], [0, 2, 4], [0, 3, 5]]

    def get_flagged_cells(self):
        flagged_cells = []
        for cell in self.board:
            if cell[2] == 4:
                flagged_cells.append(cell)
        return flagged_cells

if __name__ == '__main__':
    print(Game().get_flagged_cells())