#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio
"""

# librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import json

def main():
    # leer csv
    df = pd.read_csv("data/estado1_5.csv")

    # arrar de variables
    array_variables = ["prec",
                        "tmax",
                        "tmin",
                        "tmed",
                        "velvmax",
                        "velv",
                        "dirv",
                        "radg",
                        "humr"]
    array_titulos = ['Precipitación mm',
                        "Temperatura máxima ºC",
                        "Temperatura media ºC",
                        "Temperatura mínima ºC",
                        "Velocidad máxima del viento km/h",
                        "Velocidad promedio del viento km/h",
                        "Dirección del viento ºAz",
                        "Radiación global W/m2",
                        "Humedad relativa"]

    # Ciclo de información por estación
    for estacion in df['nombre'].unique():
        # data frame temporal para guardar la información
        df_temporal = df.where(df['nombre'] == estacion).dropna()

        for elemento in range(len(array_variables)):

            # generar una figura en blanco
            fig = plt.figure(figsize=(15,5))

            # crear gráfica
            axes = fig.add_axes([0.1,0.1,0.8,0.8])

            # valor de x
            x = np.arange(len(df_temporal['nombre']))

            # valor de y
            y = df_temporal[array_variables[elemento]]

            # mapeo de datos
            axes.plot(x,y)

            # agregar título a la gráfica
            axes.set_title(estacion)

            # agregar nomenclatura para eje Y
            axes.set_ylabel(array_titulos[elemento])

            # agregar nomenclatura para eje X
            axes.set_xlabel("Día")

            # guardar archivo
            nombre_grafica = "graphs/{}_{}.png".format(estacion, array_variables[elemento])
            fig.savefig(nombre_grafica, dpi=300)

            # limpiar el espacio de trabajo
            fig.clf()

if __name__ == '__main__':
    main()
