import platform
import sys

try:
    from screeninfo import get_monitors
except ImportError:
    get_monitors = None

try:
    import locale
except ImportError:
    locale = None


class Settings:
    def __init__(self):
        self.system = self.get_system()
        self.os_version = self.get_os_version()
        self.screen_width, self.screen_height = self.get_screen_resolution()
        self.keyboard_layout = self.get_keyboard_layout()

    def get_system(self):
        return platform.system()

    def get_os_version(self):
        return platform.release()

    def get_screen_resolution(self):
        resolution=[]
        if get_monitors:
            try:
                monitor = get_monitors()[0]  # Monitor principal
                resolution.append(monitor.width)
                resolution.append(monitor.height)
                return resolution
            except Exception:
                return None, None
        else:
            try:
                import tkinter as tk
                root = tk.Tk()
                width = root.winfo_screenwidth()
                height = root.winfo_screenheight()
                root.destroy()
                resolution.append(width)
                resolution.append(height)
                return width, height
            except Exception:
                return None, None

    def get_keyboard_layout(self):
        if locale:
            try:
                lang_code, _ = locale.getdefaultlocale()
                return lang_code  # Ej: 'es_ES', 'en_US'
            except Exception:
                return None
        return None

    def __str__(self):
        return (
            f"Sistema: {self.system} {self.os_version}\n"
            f"Resolución: {self.screen_width}x{self.screen_height}\n"
            f"Distribución teclado: {self.keyboard_layout}"
        )


# Instancia global para usar en cualquier parte
settings = Settings()