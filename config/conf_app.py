from config.Settings import settings

def validate_config():
    if settings.screen_height and settings.screen_width:
        return True
    else: 
        return False

    