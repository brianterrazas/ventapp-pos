import flet as ft
from ui.views import ventana_alerta
from config import constants
from config.Size import size
#iniciamos y recuperamos conf de logs
import logging
log=logging.getLogger(__name__)

def login_view(page: ft.Page):

    #metodos
    def mostrar_dialogo():
        page.open(ventana_alerta.barra_error_mensaje("USUARIO O CONTRASEÑA INCORRECTOS"))

    # def ir_a_menu(e):
    #     usuario=Usuario.obtener_por_nombre_usuario(TextField_user_login.value)
    #     #usuario va a recibir el usuario si existe, si no, devuelve none con eso valido con un if si existe y luego la contraseña
    #     if usuario and usuario.contrasena == TextField_pass_login.value:
    #         from app.dashboard_view import dashboard_view
    #         page.clean()
    #         page.add(dashboard_view(page, usuario))
    #     else:
    #         mostrar_dialogo()

    #elementos para la vista
    textField_user_login=ft.TextField(label="Usuario", autofocus=True)
    textField_pass_login=ft.TextField(label="Contraseña", password=True, can_reveal_password=True) #, on_submit=lambda e: ir_a_menu(e))

    print(f"login sizes {size.login_width} y {size.login_height}")

    login_container=ft.Container(
        width=size.login_width,
        height=size.login_height,
        padding=20,
        border_radius=20,
        alignment=ft.alignment.center,
        bgcolor=constants.DARK_CARD,
        content=ft.Column(
            controls=[
                ft.Image(src="img/app_logo.png", fit=ft.ImageFit.CONTAIN),
                ft.Text("Iniciar Sesión", size=size.font_medium, weight="bold"),
                textField_user_login,
                textField_pass_login,
                ft.Row(
                    [
                        ft.ElevatedButton(
                            text="Entrar",
                            icon=ft.Icons.LOGIN,
                            width=size.login_btn_w,
                            height=size.login_btn_h
                            ),                            #, on_click=ir_a_menu),
                        ft.ElevatedButton(
                            text="Salir",
                            icon=ft.Icons.EXIT_TO_APP,
                            width=size.login_btn_w,
                            height=size.login_btn_h,
                            on_click=lambda e: page.window.close()
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.ElevatedButton(
                    text="Crear empresa/usuario",
                    icon=ft.Icons.BUSINESS_CENTER,
                    width=200,
                    height=size.login_btn_h
                    )
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

    background_login=ft.Container(
        border_radius=20,
        expand=True,
        alignment=ft.alignment.center,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[constants.PRIMARY_LIGHT, constants.PRIMARY, constants.PRIMARY_DARK]
        ),
        content=login_container
    )

    return background_login
