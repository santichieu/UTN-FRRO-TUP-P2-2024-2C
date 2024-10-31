class Persona: #clase padre
    def __init__(self, nombre, apellido, dni, email, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.email = email
        self.telefono = telefono

class Alumno(Persona): #hago que herede los atributos de persona y agrego atributo nro_legajo
    def __init__(self, nombre, apellido, dni, email, telefono, nro_legajo):
        super().__init__(nombre, apellido, dni, email, telefono)
        self.nro_legajo = nro_legajo
        self.asistencias = {}
        self.inasistencias = {}

    def sumar_asistencia(self,   cod_asignatura):
        self.asistencias[  cod_asignatura] = self.asistencias.get(  cod_asignatura, 0) + 1

    def sumar_inasistencia(self,   cod_asignatura):
        self.inasistencias[  cod_asignatura] = self.inasistencias.get(  cod_asignatura, 0) + 1

class Administrativo(Persona): #aca como no necesito agregar nada hago que herede los atributos de persona y uso pass para que no haya ningun error
    pass

class Asignatura:
    def __init__(self, nombre,  cod_asignatura):
        self.nombre = nombre
        self. cod_asignatura =  cod_asignatura
        self.alumnos = []

    def inscribir_alumno(self, alumno):
        self.alumnos.append(alumno)

    def listar_alumnos(self):
        print(f"{'DNI':<10} {'Apellido':<15} {'Nombre':<20} {'Email':<25}")
        print("-" * 60)
        for alumno in self.alumnos:
            print(f"{alumno.dni:<10} {alumno.apellido:<15} {alumno.nombre:<20} {alumno.email:<25}")

class Registrodatos: #creamos clase registro para crear las funciones correspondientes
    def __init__(self):
        self.alumnos = []
        self.administrativos = []
        self.asignaturas = []

    def registrar_alumno(self, nombre, apellido, dni, email, telefono, nro_legajo):
        alumno = Alumno(nombre, apellido, dni, email, telefono, nro_legajo)
        self.alumnos.append(alumno)
        return alumno

    def registrar_administrativo(self, nombre, apellido, dni, email, telefono):
        administrativo = Administrativo(nombre, apellido, dni, email, telefono)
        self.administrativos.append(administrativo)
        return administrativo

    def registrar_asignatura(self, nombre,  cod_asignatura):
        asignatura = Asignatura(nombre,  cod_asignatura)
        self.asignaturas.append(asignatura)
        return asignatura

    def mostrar_alumnos_por_asignatura(self,   cod_asignatura):
        asignatura = next((a for a in self.asignaturas if a. cod_asignatura ==   cod_asignatura), None)
        if asignatura:
            asignatura.listar_alumnos()
        else:
            print(f"No se encontro la asignatura,  cod_asignatura: {  cod_asignatura}")
            
    def sumar_asistencia(self, dni,   cod_asignatura):
        alumno = next((a for a in self.alumnos if a.dni == dni), None)
        if alumno:
            alumno.sumar_asistencia(  cod_asignatura)
            print(f"Asistencia agregada para el alumno {alumno.nombre} {alumno.apellido} en la asignatura {  cod_asignatura}.")
        else:
            print(f"No se encontró ningun alumno con DNI: {dni}")

    def sumar_inasistencia(self, dni,   cod_asignatura):
        alumno = next((a for a in self.alumnos if a.dni == dni), None)
        if alumno:
            alumno.sumar_inasistencia(  cod_asignatura)
            print(f"Inasistencia agregada para el alumno {alumno.nombre} {alumno.apellido} en la asignatura {  cod_asignatura}.")
        else:
            print(f"No se encontró ningun alumno con DNI: {dni}")

if __name__ == "__main__":
    registro = Registrodatos()

    #Harcodeamos los alumnos, administrativos
    alumno1 = registro.registrar_alumno("Santiago", "Chieu", "12345678", "santi@ejemplo.com", "3415413471", "4507")
    alumno2 = registro.registrar_alumno("Roberto", "Lopez", "87654321", "roberto@ejemplo.com", "3413123456", "4508")
    alumno3 = registro.registrar_alumno("Juana", "De Arco", "9851322", "JuanitaLaArquerita@ejemplo.com", "3414513223", "1502")

    
    administrativo1 = registro.registrar_administrativo("Juan Carlos", "Rodriguez", "98765432", "JuanCarlos@ejemplo.com", "3415123456")

    
    asignatura1 = registro.registrar_asignatura("Probabilidad y estadistica", "PRB105")
    asignatura2 = registro.registrar_asignatura("Programacion II", "PRO106")

    #incribimos a varios a los alumnos a las diferentes materias
    asignatura1.inscribir_alumno(alumno1)
    asignatura1.inscribir_alumno(alumno2)
    asignatura1.inscribir_alumno(alumno3)
    
    asignatura2.inscribir_alumno(alumno1)
    asignatura2.inscribir_alumno(alumno3)
    
    #sumamos asistencias e inasistencias de los alumnos
    print("\n")
    registro.sumar_asistencia("12345678", "PRB105")
    registro.sumar_asistencia("12345678", "PRO106")  
    registro.sumar_asistencia("87654321", "PRO106")
     
    print("\n")
    registro.sumar_inasistencia("12345678", "PRO106")
    registro.sumar_inasistencia("87654321", "PRB105")
    registro.sumar_inasistencia("9851322", "PRB105")
    registro.sumar_inasistencia("9851322", "PRO106")
     
     
    #mostramos a los alumnos en cada materia
    print("\n")
    print("Alumnos inscriptos en Probabilidad y estadistica:")
    registro.mostrar_alumnos_por_asignatura("PRB105")
    print("\n")
    print("Alumnos inscriptos en Programacion II:")
    registro.mostrar_alumnos_por_asignatura("PRO106")
    
    #hacemos que muestre que no hay materia con ese cod_asignatura
    print("\n")
    print("Alumnos inscriptos en Programacion I:")
    registro.mostrar_alumnos_por_asignatura("PRO105")
    