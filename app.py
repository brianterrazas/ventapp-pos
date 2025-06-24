import os
import logging
import flet as ft
from config import constants
from config import conf_app
from ui.views.login_view import login_view
from ui.views import ventana_alerta
from config.Settings import settings    #importamos la instancia directamente con esto ya tenemos acceso a la info del equipo desde donde se ejecuta la app


def main(page: ft.Page):
    page.window.center=True
    page.title=constants.NOMBRE_APP
    page.clean()

    logging.info("LANZAR INICIAR_APP")
    page.add(login_view(page))

def configurarLogging():
    #configurar logging global
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] %(levelname)s: %(message)s (Archivo: %(filename)s | Línea: %(lineno)d)',
        datefmt='%d/%m/%Y %H:%M:%S',
        filename=constants.RUTA_LOG,   #donde guardar los logs
        filemode='a'    #a significa que agrega linea al log, w seria para crear de 0
    )

    #mostrar en consola además del archivo
    console=logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter=logging.Formatter('[%(levelname)s] %(message)s')
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)

if __name__ == "__main__":
    configurarLogging()
    if conf_app.validate_config():
        #inicio de app
        ft.app(target=main)
    else:
        logging.info("Error lanzando app")
