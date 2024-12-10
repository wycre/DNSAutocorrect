from django.apps import AppConfig

"""
Modify the class name to match the format Module{providername}Config
i.e. ModulecloudflareConfig, ModulenamecheapConfig
"""
class ModuletemplateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    """
    Modify the name field to EXACLY MATCH the name of the folder this file is in
    """
    name = 'moduleTemplate'
