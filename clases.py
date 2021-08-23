#clases

class Persona():
    edad=0
    nombre=''
    apellido=''


    def __init__(self,apellido): #CONSTRUCTOR
        self.edad=18
        self.apellido=apellido

        

    def nombre_completo(self): #self indica q el metodo pertenece a la clase
        return self.nombre+ ' '+self.apellido #self es similar al this

persona= Persona('ramirez') # INICIALIZO EL OBJETO COMO PERSONA p = new Persona()
persona.nombre='jeremy'

print(persona.edad)
print(persona.nombre_completo())
