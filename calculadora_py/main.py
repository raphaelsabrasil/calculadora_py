import sys
from main_window import MainWindow
from PySide6.QtWidgets import QApplication  # QLabel
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON
from display import Display
from info import Info
from styles import setupTheme
from buttons import ButtonsGrid


# def temp_label(texto):
#     label1 = QLabel(texto)
#     label1.setStyleSheet('font-size: 50px;')
#     return label1


if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
        

    # label1 = QLabel('O meu texto')
    # label1.setStyleSheet('font-size: 50px;')
    # window.addWidgeToVLayout(label1)
    # window.addWidgeToVLayout(temp_label('Label 2')) # escreve usando def temp_label
    # window.adjustFixedSize()  # já aparece na função acima

    # Info
    # info = Info('2.0^10.0 = 1024')
    info = Info('Sua conta')
    # window.addToVLayout(info)
    window.addWidgetToVLayout(info)

    # Display
    display = Display()     # pode definir texto dentro ()
    # display.setPlaceholderText('Digite algo')   # inclui placeholder
    window.addWidgetToVLayout(display)    # adicionando display na janela
    # window.addToVLayout(Display('Display 2'))
    # window.addToVLayout(Display('Display 3'))

    # button = Button('Texto do botão')
    # window.addWidgetToVLayout(button)

    # button2 = Button('Texto do botão')
    # window.addWidgetToVLayout(button2)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()


# snake_case    variáveis, métodos
# PascalCase    geralmente classe
# camelCase     variáveis, métodos
# para mudar em todas as variáveis ou métodos iguais > seleciona e F2

#####################################################################
'''
# Installar PyInstaller >> para empacotamento PySide6, aplicações para Windows (pip install pyinstaller)

# https://www.pythonguis.com/tutorials/packaging-pyside6-applications-windows-pyinstaller-installforge/

# https://pyinstaller.org/en/stable/

# Depois de instalado, atualizar em 'requirements.txt' (pip freeze > requeriments.txt)



# Executando direto no terminal (python aula202_calculadora/main.py)

# No Windows sem uma IDE, pode executar pelo powershell: >>>>>>>>
# Instalar ambiente virtual venv e ativar (caso dê erro, entrar no powershell como administrador e digitar 'Set-ExecutionPolicy Unrestricted e confirmar 'S');
# Instalar PySide6 (atualizar se necessário quando aparecer [notice] no terminal);
# Instalar pyqtdarktheme;
# e PyInstaller;
# Comando para gerar arquivo e pasta de saída: pyinstaller --name="Calculadora" --noconfirm --noconsole --onefile --add-data='../aula202_calculadora/files/;files/' --icon='../aula202_calculadora/files/icone_br.png' --clean --log-level=WARN --distpath="projeto_calculadora/dist" --workpath="projeto_calculadora/build" --specpath="projeto_calculadora/" aula202_calculadora/main.py
# Instalar pillow (se necessário para carregar ícone). <<<<<<<<<

dispath >> gera pasta de distribuição (dist) do arquivo executável
workpath >> gera pasta build com arquivos temporários compilados
specpath >> gera arquivo spec com arquivo compilado 
arquivo spec >> em caso de apagar arquivos, pode usar o spec para gerar de novo a aplicação > no terminal 'pyinstaller projeto_calculadora/Calculadora.spec'
dist e build >> para gerar estas pastas > no terminal 'pyinstaller --dispath projeto_calculadora/dist --workpath projeto_calculadora/build projeto_calculadora/Calculadora.spec'
--noconsole >> para não abrir terminal quando executar arquivo
--add-data >> dados do arquivo (não é o código) ('../aula202_calculadora/files/' << arquivo onde busca / ';files/' << arquivo para onde vai)
'''
##############################################################

# LINUX

# Para instalação de ambiente virtual no terminal Linux: sudo apt install python3-virtualenv

# Para verificar a instalação, digite:
# $ virtualenv --version

# Para criar um ambiente virtual python com o virtualenv, digite em seu terminal:
# $ virtualenv <nome_do_projeto>

# Para ativar o ambiente, digite:
# $ cd nome_do_projeto
# $ source bin/activate

# E o resultado será:
# (nome_do_projeto)$

# Para desativar o ambiente, digite:
# (nome_do_projeto)$ deactivate

# Que retornará:
# $

# Vantagens em se utilizar o virtualenv:
# Isola o seu projeto do Python nativo do ambiente Linux;
# Organiza seus projetos e módulos, sem encher o pip nativo do Linux.

#Encontrando caminho do arquivo: $ find / -name nome_do_projeto

# Em diretório específico: $ find /home/oem/Desktop -iname *main.py*

# Com Locate: $ locate main.py

################################

# No LINUX sem uma IDE, pode executar pelo terminal: >>>>>>>>
# Instalar ambiente virtual venv e ativar;
# Instalar PySide6 (atualizar se necessário quando aparecer [notice] no terminal);
# Instalar pyqtdarktheme;
# Instalar PyInstaller;
# Instalar libxcb-cursor0 se necessário (sudo apt-get install libxcb-cursor0)
# Para executar arquivo que está no venv:  
#       $ python3 /home/oem/venv/calculadora/main.py

# Comando para gerar arquivo e pasta de saída do app para usuário: 
#       pyinstaller --name="Calc" --noconfirm --noconsole --onefile --add-data='/:files/' --icon='/icone_br.png' --clean --log-level=WARN --distpath="projeto_calc/dist" --workpath="projeto_calc/build" --specpath="projeto_calc/" calculadora/main.py

# Instalar pillow (se necessário para carregar ícone). <<<<<<<<<

