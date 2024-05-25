import streamlit as st
import pandas as pd
from faker import Faker
import random
import datetime


st.title("Ejercicio Semana 9")

st.write("Dentro del select se encuentran ocho filtros en total")

#Primero se crea un objeto Faker para generar datos aleatorios
fake = Faker()

#Lueego se crea una lista vacía para almacenar los datos de los estudiantes
datas = []

#Generamos 50 filas de datos de estudiantes
for data in range(50):
    nombre = fake.first_name()
    apellido = fake.last_name()
    edad = round(random.uniform(5, 20))
    fecha_matriculacion = fake.date_between(start_date='-4y', end_date='today')
    promedio_rendimiento = round(random.uniform(1.0, 5.0), 2)
    nombre_madre = fake.first_name_female()
    nombre_padre = fake.first_name_male()
    activo = random.choice([True, False])
    datas.append([nombre, apellido, edad, fecha_matriculacion, promedio_rendimiento, nombre_madre, nombre_padre, activo])


#Creamos el DataFrame
df = pd.DataFrame(datas, columns=['Nombre', 'Apellido', 'Edad', 'Fecha de Matriculación', 'Promedio de Rendimiento', 'Nombre de la Madre', 'Nombre del Padre', 'Activo'])
df['Fecha de Matriculación'] = pd.to_datetime(df['Fecha de Matriculación'])

#Y luego los filtros que deseamos poner
def primer_filtro():
    st.write("Filtro para saber los estudiantes que ya superaron la mayoria de edad")
    st.table(df[df['Edad'] > 17])
    
def segundo_filtro():
    st.write("Filtro para saber los estudiantes que ya no son activos")
    st.table(df[df['Activo'] == False])

def tercer_filtro():
    st.write("Filtro para saber que estudiantes superaron la nota minima aprobable (3.0)")
    st.table(df[df['Promedio de Rendimiento'] >= 3.0])

def cuarto_filtro():
    st.write("Filtro para mostrar solo los estudiantes matriculados entre los años 2020 y 2021")
    st.table(df[(df['Fecha de Matriculación'].dt.year == 2020) | (df['Fecha de Matriculación'].dt.year == 2021)])

def quinto_filtro():
    st.write("Filtro para mostrar solo los estudiantes cuyo nombre empiece por A y sean menores o iguales de 17 años")
    st.table(df[(df['Nombre'].str.startswith('A')) & (df['Edad'] <= 17)])

def sexto_filtro():
    st.write("Filtro para mostrar los nombres de los padres de los estudiantes activos")
    PadresE = df[(df['Activo'] == True)]
    st.table(PadresE[['Nombre de la Madre', 'Nombre del Padre', 'Activo']])

def septimo_filtro():
    st.write("Filtro para mostrar solo los estudiantes que estén entre los 10 y 15 años")
    st.table(df[df['Edad'].isin([10, 15])])

def octavo_filtro():
    st.write("Tabla completa")
    st.table(df)

#Luego tenemos una lista con estos mismo filtros
filtros = [
    'Primer filtro',
    'Segundo filtro',
    'Tercer filtro',
    'Cuarto filtro',
    'Quinto filtro',
    'Sexto filtro',
    'Septimo filtro',
    'Octavo filtro'
]

#Y un select box para que la información no se sature, sino que se muestre según lo que queramos ver
seleccion_filtro = st.selectbox("Filtro", filtros)

if seleccion_filtro:
    index = filtros.index(seleccion_filtro)
    if index == 0:
        primer_filtro()
    elif index == 1:
        segundo_filtro()
    elif index == 2:
        tercer_filtro()
    elif index == 3:
        cuarto_filtro()
    elif index == 4:
        quinto_filtro()
    elif index == 5:
        sexto_filtro()
    elif index == 6:
        septimo_filtro()
    elif index == 7:
        octavo_filtro()