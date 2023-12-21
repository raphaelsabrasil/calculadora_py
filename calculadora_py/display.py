from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from utils import isEmpty, isNumOrDot
from variables import BIG_FONT_SIZE, MINIMUM_WIDTH, TEXT_MARGIN


class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)      # informando o tipo do argumento
    operatorPressed = Signal(str)
    negativePressed = Signal()      # sinal para botão de '-ou+' no módulo buttons

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.configStyle()                 # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    def configStyle(self):      # só será chamado se estiver ativo acima
        margins = [TEXT_MARGIN for _ in range(4)]  
        # for qualquer coisa [BIG_FONT_SIZE, MINIMUM_WIDTH, TEXT_MARGIN]
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)


    # Para capturar teclas pressionadas
    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()  # strip remove espaços das pontas
        key = event.key()        
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete, KEYS.Key_D]
        isEsc = key in [KEYS.Key_Escape, KEYS.Key_C]
        isOperator = key in [KEYS.Key_Plus, KEYS.Key_Minus, KEYS.Key_Slash, KEYS.Key_Asterisk, KEYS.Key_P]
        isNegative = key in [KEYS.Key_N]

        if isEnter:
            # print(f'EQ {text} pressionado, sinal emitido', type(self).__name__)
            self.eqPressed.emit()
            return event.ignore()
        
        if isDelete:
            # print(f'isDelete {text} pressionado, sinal emitido', type(self).__name__)
            self.delPressed.emit()
            return event.ignore()
        
        if isEsc:
            # print('isEsc pressionado, sinal emitido', type(self).__name__)
            self.clearPressed.emit()
            return event.ignore()
        
        if isOperator:
            if text.lower() == 'p':
                text = '^'
            self.operatorPressed.emit(text)
            return event.ignore()
        
        if isNegative:
            self.negativePressed.emit()
            return event.ignore()

        
        # Não passar daqui se não tiver texto (letras)
        if isEmpty(text):
            return event.ignore()
        
        if isNumOrDot(text):
            # print('inputPressed pressionado, sinal emitido', type(self).__name__)
            self.inputPressed.emit(text)
            return event.ignore()