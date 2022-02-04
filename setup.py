from http.server import executable
from optparse import Option
import cx_Freeze

executables = [cx_Freeze.Executable('Run.py')]

cx_Freeze.setup(
    name="Sys Cadastro",
    option={'build_exe': {'packages':['PyQt5', 'Janelas', 'Validacao', 'Banco_db'],
                          'include_files':['Banco_db', 'Consulta', 'img', 'Janelas', 'Validacao']}},
    
    executables = executables     
    
)