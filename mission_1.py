"""
   Misión 1

   ¡Bienvenido agente!. La función get_flagged_cells esta sacada directamente
   del libro Clean Code. En este libro nos muestran el código de esa
   función, nos comenta por qué el código tiene problemas y nos muestra
   la versión final. Para esta misión vamos a refactorizar paso a paso
   mientras mostramos unos principios de Clean Code y Refactring. 
   Para hacer el ejemplo más completo he creado un poco de código extra 
   para darle la forma de una clase de una aplicación real.
"""
class Game:
    def __init__(self):
        self.theList = [[0, 0, 2], [0, 1, 2], [0, 2, 4], [0, 3, 5]]

    def get_flagged_cells(self):
        list = []
        for x in self.theList:
            if x[2] == 4:
                list.append(x)
        return list

if __name__ == '__main__':
    print(Game().get_flagged_cells())