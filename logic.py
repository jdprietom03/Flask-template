import random
from datetime import datetime
from model.Ciudadano import Ciudadano
from model.Localidad import Localidad
from model.Colegio import Colegio
from model.Social import Social
from model.Infancia import Infancia

from database.ciudadanos_repository import CiudadanoRepository
from database.colegios_repository import ColegioRepository
from database.localidades_repository import LocalidadRepository
from database.sociales_repository import SocialRepository
from database.infancias_repository import InfanciaRepository
from database.programas_repository import ProgramaRepository
from database.products_repository import ProductRepository

# n = random.randint(1,10)
n = 800

cantidad_colegios = 10
print("el algoritmo genero "+ str(n) + " registros")
timestamp = int(datetime.now().timestamp()*1e6)
f = open(str(timestamp)+".txt", "w")

CiudadanoRepository().delete_all()
ColegioRepository().delete_all()
LocalidadRepository().delete_all()

def generate_date():
    start_time = 946702800
    end_time = 1136005200
    return datetime.fromtimestamp(random.randint(start_time,end_time)).strftime("%d/%m/%Y")

def generate_sexo():
    if(random.randint(0,1)==0):
        return 'F'
    return 'M'

def generate_bool():
    if(random.randint(0,1)==0):
        return 'S'
    return 'N'

def generate_localidad():
    return random.randint(1,16)

def generate():
    dI = int(1e7)
    for i in range(n):
        dI +=1
        persona = {
            'Di' : dI,
            'fecha_nacimiento' : generate_date(),
            'sexo' : generate_sexo(),
            'primera_infancia' : generate_bool(),
            'programa_desarrollo' : generate_bool(),
            'especial_atencion' : generate_bool(),
            'localidad' : generate_localidad()
        }
        vals = persona.values()
        cadena = ""
        for val in vals:
            cadena += str(val)+';'
        f.write(cadena)
        f.write('\n')
    f.close()
#generate()


def read_personas():
    file = open("1669415500695966.txt", "r")
    lineas = file.readlines()
    # lineas = lineas[]
    listaPersonas = []
    for linea in lineas:
        linea = linea.split(';')
        persona = {
            'Di' : int(linea[0]), # Identificacion int
            'Fec_nac' : datetime.strptime(linea[1],'%d/%m/%Y'), #Fecha nacimiento datetime
            'Sexo' : linea[2], # Sexo F M
            'BPPI' : 'N', #beneficiario primera infancia S N
            'BPPS' : 'N', #beneficiario promocion social y economica S N
            'PE' : linea[5], #poblacion especial S N
            'Localidad' : int(linea[6]),# Indice de la localidad 1-16 (objeto)
            'Colegio' : random.randint(0,cantidad_colegios-1), #Indice del colegio int 0-99
            'Indicador' : random.randint(0,6) # Estrato aleatorio int 0-6
        }
        listaPersonas.append(Ciudadano(persona))
        CiudadanoRepository().create(Ciudadano(persona))
    file.close()
    return listaPersonas

def generate_tipo_colegio():
    rnd = random.randint(0,2)
    if(rnd == 0):
        return "Pr"
    elif(rnd == 1):
        return "Pb"
    return "M"

def generate_colegios(cantidad):
    listaColegios = []
    for i in range(cantidad):
        colegio = {
            'Id' : i,
            'Tipo' : generate_tipo_colegio(),
            'Cantidad' : random.randint(50,500),
            'Id_localidad' : random.randint(1,16)
        }
        listaColegios.append(Colegio(colegio))
        ColegioRepository().create(Colegio(colegio))
    return listaColegios

def generate_localidades(colegios):
    listaLocalidades = []
    cantidadesColegios = [0]*17
    for colegio in colegios:
        cantidadesColegios[colegio.Id_localidad] += 1
    for i in range(16):
        localidad = {
            'Id' : i+1,
            'Cantidad_colegios' : cantidadesColegios[i]
        }
        listaLocalidades.append(Localidad(localidad))
        LocalidadRepository().create(Localidad(localidad))
    return listaLocalidades


personas = read_personas()
colegios = generate_colegios(cantidad_colegios)
localidades = generate_localidades(colegios)
cantidad_social = int(input("Por favor ingrese la cantidad de beneficios a asignar al programa de promocion social\n"))
social = Social(
    {
        'Disponibles' : cantidad_social,
        'Asignados' : 0
    }
)

SocialRepository().create(social)

cantidad_infancia = int(input("Por favor ingrese la cantidad de beneficios a asignar al programa de primero MiInfancia\n"))
infancia = Infancia(
    {
        'Disponibles' : cantidad_infancia,
        'Asignados' : 0
    }
)

InfanciaRepository().create(infancia)

def assign_beneficios():
    random.shuffle(personas)
    beneficios_localidad = [0]*17
    beneficios_colegio = [0]*cantidad_colegios
    beneficios_estrato = [0]*7
    for persona in personas:
        if(social.Disponibles >= 1):
            persona.BPPS = 'S'
            social.Disponibles -= 1
            social.Asignados += 1
        elif(infancia.Disponibles >= 1):
            persona.BPPI = 'S'
            infancia.Disponibles -= 1
            infancia.Asignados += 1
        else: 
            break
        beneficios_localidad[persona.Localidad-1]+=1
        beneficios_colegio[persona.Colegio]+=1
        beneficios_estrato[persona.Indicador]+=1
    for i in range(len(beneficios_localidad)):
        print("A la localidad " + str(i+1) + " se le asigno "+str(beneficios_localidad[i])+" beneficios, lo cual representa un "+str(100*beneficios_localidad[i]/(cantidad_infancia+cantidad_social))+"'%' de los beneficios asignados")
    for i in range(len(beneficios_colegio)):
        print("Al colegio " + str(i) + " se le asigno "+str(beneficios_colegio[i])+" beneficios, lo cual representa un "+str(100*beneficios_colegio[i]/(cantidad_infancia+cantidad_social))+"'%' de los beneficios asignados")
    for i in range(len(beneficios_estrato)):
        print("Al Indicador Socio Economico " + str(i) + " se le asigno "+str(beneficios_estrato[i])+" beneficios, lo cual representa un "+str(100*beneficios_estrato[i]/(cantidad_infancia+cantidad_social))+"'%' de los beneficios asignados")
   
assign_beneficios()