from config.Settings import settings


class Size:
    def __init__(self):
        self.screen_width = settings.screen_width or 1080  #fallback
        self.screen_height = settings.screen_height or 720

        #Proporciones básicas
        self.btn_w = self.screen_width // 6
        self.btn_h = self.screen_height // 12
        self.login_btn_w = self.screen_width // 14
        self.login_btn_h = self.screen_height // 20

        #Tamaños de fuente
        self.font_small = int(self.screen_width * 0.015)  #Ej: 12 px
        self.font_medium = int(self.screen_width * 0.02)  #Ej: 16 px
        self.font_large = int(self.screen_width * 0.03)   #Ej: 24 px

        #Margen y padding
        self.margin = int(self.screen_width * 0.02)
        self.padding = int(self.screen_width * 0.015)

        #Tamaños de campos de texto o inputs
        self.input_width = self.screen_width // 3
        self.input_height = self.screen_height // 18

        #Cards, contenedores, etc.
        self.card_width = self.screen_width // 2
        self.card_height = self.screen_height // 3
        self.panel_width = self.screen_width // 2
        self.panel_height = self.screen_height // 3
        self.login_width = self.screen_width * 0.18
        self.login_height = self.screen_height * 0.37

#Instancia global para usar en toda la app
size = Size()