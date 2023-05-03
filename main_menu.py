import os
import sys
import pygame
import locale
from datetime import datetime

from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtGui import QAction
from PySide6.QtCore import Signal
from PySide6 import QtWidgets, QtGui, QtCore 
from PySide6.QtWidgets import QDialog, QLabel, QComboBox
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QFrame, QDialog, QFormLayout, QLineEdit, QDialogButtonBox
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QComboBox, QHBoxLayout, QLabel, QFormLayout, QSlider
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QHBoxLayout, QLabel

#from g_words import GameWords
from g_words import GameWords

import start_text_editor
from fonts import get_pyside6_fonts, get_font_paths
from settings import Settings
from text_icon_gen import Gen
from g_letter import GameLetterMix
from g_all_once import GameAllOnce
from g_remove_what import GameRemoveWhat

from color_constants import ColorConst
from translator import Translator


class MainWindow(QtWidgets.QMainWindow):
    # ToDo: No: Add choice for special characters or only AZ-az
    # ToDo: Add colors from settings to the buttons in the main menu
    # ToDo: Rethink "Char repeats" feature
    # ToDo: Add more fonts
    
    
    handleSettingsChanged = Signal()

    def __init__(self, app):
        super().__init__()
        pygame.init()
        
        self.trans = Translator()
        self.menu_texts = Settings.r_menu_text()
        
        self.settings = Settings.r_setup()
        self.lang_code = self.trans.get_code(self.settings["language"])
        self.background_color = self.settings["background_color"]
        self.text_color = self.settings["text_color"]
        
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.handleSettingsChanged.connect(self.on_handleSettingsChanged)
        
        self.setWindowTitle("ABC Trainer")
        self.read_menu_titles()
        
        self.gen = Gen()
        
         # Add QMenuBar
        menu_bar = self.menuBar()
        self.fileMenu = menu_bar.addMenu(self.mt_file)

        self.settingsAction = QAction(self.mt_settings, self)
        self.settingsAction.triggered.connect(self.showSettingsDialog)
        self.fileMenu.addAction(self.settingsAction)
        
        self.textEditorActionWords = QAction(f'{self.mt_open} words_{self.lang_code}.txt')
        
        self.textEditorActionWords.triggered.connect(self.startTextEditor)
        self.fileMenu.addAction(self.textEditorActionWords)
        
        self.exitAction = QAction(self.mt_exit_program, self)
        self.exitAction.triggered.connect(app.quit)
        self.fileMenu.addAction(self.exitAction)
        
        # Create an action for the "About" menu item
        self.about_action = QAction(self.mt_about, self)
        self.about_action.triggered.connect(self.showAboutDialog)
        menu_bar.addAction(self.about_action)
        
        self.build_GUI()
        
        
        
    def read_menu_titles(self):
        self.lang_code = self.trans.get_code(self.settings["language"])
        self.mt_file = self.menu_texts[self.lang_code]["File"]
        self.mt_settings = self.menu_texts[self.lang_code]["Settings"]
        self.mt_open = self.menu_texts[self.lang_code]["Open"]
        self.mt_exit_program = self.menu_texts[self.lang_code]["Exit program"]
        self.mt_user_pref = self.menu_texts[self.lang_code]["User preferences"]
        self.mt_instructions = self.menu_texts[self.lang_code]["Instructions in games"]
        self.mt_slow_speech = self.menu_texts[self.lang_code]["Slow speech"]
        self.mt_username = self.menu_texts[self.lang_code]["Username"]
        self.mt_repetitions = self.menu_texts[self.lang_code]["Repetitions for Mixed"]
        self.mt_volume = self.menu_texts[self.lang_code]["Audio volume"]
        self.mt_game_screens = self.menu_texts[self.lang_code]["Game screens"]
        self.mt_full_screen = self.menu_texts[self.lang_code]["Full screen"]
        self.mt_background_color = self.menu_texts[self.lang_code]["Background color"]
        self.mt_text_color_text = self.menu_texts[self.lang_code]["Text color"]
        self.mt_window_width = self.menu_texts[self.lang_code]["Window width"]
        self.mt_window_height = self.menu_texts[self.lang_code]["Window height"]
        self.mt_language = self.menu_texts[self.lang_code]["Language"]
        self.mt_font = self.menu_texts[self.lang_code]["Font"]
        self.mt_case = self.menu_texts[self.lang_code]["Letter case"]
        self.mt_excluded_chars = self.menu_texts[self.lang_code]["Excluded characters"]
        self.mt_about = self.menu_texts[self.lang_code]["About"]
        
        self.mt_mixed_txt = self.menu_texts[self.lang_code]["Mixed"]
        self.mt_mixed_txt = self.get_right_case(self.mt_mixed_txt)
        
        self.mt_words_txt = self.menu_texts[self.lang_code]["Words"]
        self.mt_words_txt = self.get_right_case(self.mt_words_txt)
        
        self.mt_unique_txt = self.menu_texts[self.lang_code]["Unique"]
        self.mt_unique_txt = self.get_right_case(self.mt_unique_txt)
        
        
    def trans_menu(self):
        self.fileMenu.setTitle(self.mt_file)
        self.settingsAction.setText(self.mt_settings)
        self.formLayout.labelForField(self.instructionsCheckBox).setText(self.mt_instructions)
        self.about_action.setText(self.mt_about)
        self.textEditorActionWords.setText(f'{self.mt_open} words_{self.lang_code}.txt')
        self.exitAction.setText(self.mt_exit_program)
        self.user_pref.setText(self.mt_user_pref)
        self.game_screens.setText(self.mt_game_screens)
        
        self.formLayout.labelForField(self.slow_speechCheckBox).setText(self.mt_slow_speech)
        self.formLayout.labelForField(self.userNameLineEdit).setText(self.mt_username)
        self.formLayout.labelForField(self.repetitionsLineEdit).setText(self.mt_repetitions)
        self.formLayout.labelForField(self.volume_slider).setText(self.mt_volume)
        self.formLayout.labelForField(self.fullScreenCheckBox).setText(self.mt_full_screen)
        
        self.formLayout.labelForField(self.hbox_background).setText(self.mt_background_color)
        self.formLayout.labelForField(self.text_color_hbox).setText(self.mt_text_color_text)
        self.formLayout.labelForField(self.windowWidthLineEdit).setText(self.mt_window_width)
        self.formLayout.labelForField(self.windowHeightLineEdit).setText(self.mt_window_height)
        self.formLayout.labelForField(self.languageComboBox).setText(self.mt_language)
        self.formLayout.labelForField(self.fontComboBox).setText(self.mt_font)
        self.formLayout.labelForField(self.caseComboBox).setText(self.mt_case)
        self.formLayout.labelForField(self.excludedCharsLineEdit).setText(self.mt_excluded_chars)
    
    
    def get_right_case(self, text):
        case = self.settings["letter_case"]
        if case == "UPPER":
            return text.upper()
        elif case == "lower":
            return text.lower()
        elif case == "Both":
            return text.title()
        else:
            #raise ValueError(f"Invalid letter_case setting: {case}")
            print(f"Warning: Invalid letter_case setting: {case}. Using 'UPPER' as default.")
            return text.upper()

        
    def reconfig_buttons(self):
        
        self.lang_code = self.trans.get_code(self.settings["language"])
        self.font_paths = get_font_paths()
        self.pyside6_fonts = get_pyside6_fonts(self.font_paths, 16)
        self.font_name_in_use = self.settings["font"]
        
        self.background_color = self.settings["background_color"]
        self.text_color = self.settings["text_color"]

        random_letters_pic = self.gen.text_image(self.pyside6_fonts[self.font_name_in_use][1], self.mt_mixed_txt, file_name="random_letters.png", background_color=self.background_color, text_color=self.text_color) # Random letters ".png")
        self.button1.setIcon(QtGui.QIcon(random_letters_pic))

        pic_txt = {"UPPER": "A-Z", "lower": "a-z", "Both": "A-Z & a-z"}
        pic_txt = pic_txt[self.settings["letter_case"]]
        self.window_icon_path = f"{pic_txt}.png"
        file_name = self.gen.text_image(self.pyside6_fonts[self.font_name_in_use][1], pic_txt, file_name=self.window_icon_path, background_color=self.background_color, text_color=self.text_color)
        
        self.button2.setIcon(QtGui.QIcon(file_name))
        
        # Set the window icon
        icon = QIcon(file_name)
        self.setWindowIcon(icon)
        
        words_pic_path = self.gen.text_image(self.pyside6_fonts[self.font_name_in_use][1], self.mt_words_txt, file_name="words.png", background_color=self.background_color, text_color=self.text_color) # Words
        self.button3.setIcon(QtGui.QIcon(words_pic_path))
        
        unique_file_path = self.gen.text_image(self.pyside6_fonts[self.font_name_in_use][1], self.mt_unique_txt, file_name="unique.png", background_color=self.background_color, text_color=self.text_color)
        self.button4.setIcon(QtGui.QIcon(unique_file_path))
      
        
    def build_GUI(self):
        # ToDo: Fix picture text to represent correct exercise and language from settings
        
        self.settings = Settings.r_setup()
        self.font_paths = get_font_paths()
        
        self.pyside6_fonts = get_pyside6_fonts(self.font_paths, 16)
        
        self.font_name_in_use = self.settings["font"]
        
        random_letters_pic = self.gen.text_image(self.pyside6_fonts[self.font_name_in_use][1], self.mt_mixed_txt, file_name="random_letters.png", background_color=self.background_color, text_color=self.text_color) # Random letters ".png")

        self.button1 = QtWidgets.QPushButton() 
        self.button1.setIcon(QtGui.QIcon(random_letters_pic))
        self.button1.clicked.connect(self.show_pygame_1)
        
        pic_txt = {"UPPER": "A-Z", "lower": "a-z", "Both": "A-Z & a-z"}
        pic_txt = pic_txt[self.settings["letter_case"]]
        
        self.window_icon_path = f"{pic_txt}.png"
        
        window_icon_pic = self.gen.text_image(self.pyside6_fonts[self.font_name_in_use][1], pic_txt, file_name=self.window_icon_path, background_color=self.background_color, text_color=self.text_color)
        
        self.button2 = QtWidgets.QPushButton() 
        self.button2.setIcon(QtGui.QIcon(window_icon_pic))
        self.button2.clicked.connect(self.show_pygame_2)
        
        # Set the window icon
        icon = QIcon(window_icon_pic)
        self.setWindowIcon(icon)
        
        words_pic_path = self.gen.text_image(self.pyside6_fonts[self.font_name_in_use][1], self.mt_words_txt, file_name="words.png", background_color=self.background_color, text_color=self.text_color) # Words

        self.button3 = QtWidgets.QPushButton() 
        self.button3.setIcon(QtGui.QIcon(words_pic_path))
        self.button3.clicked.connect(self.show_pygame_3)
        
        unique_file_path = self.gen.text_image(self.pyside6_fonts[self.font_name_in_use][1], self.mt_unique_txt, file_name="unique.png", background_color=self.background_color, text_color=self.text_color)

        self.button4 = QtWidgets.QPushButton()
        self.button4.setIcon(QtGui.QIcon(unique_file_path))
        self.button4.clicked.connect(self.show_pygame_4)

        self.grid = QtWidgets.QGridLayout()
        self.grid.addWidget(self.button1, 0, 0)
        self.grid.addWidget(self.button2, 0, 1)
        self.grid.addWidget(self.button3, 1, 0)
        self.grid.addWidget(self.button4, 1, 1)

        for i in range(self.grid.count()):
            item = self.grid.itemAt(i).widget()
            item.setStyleSheet("QPushButton:hover { border: 50px solid gray;}")
            item.setIconSize(QtCore.QSize(300, 300))
            
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(self.grid)
        self.setCentralWidget(central_widget)
        
        self.show()
        
        
    def on_handleSettingsChanged(self):
        # Perform an action when the signal is received
        # For example, you can update the GUI, write the settings to a file, or show a message box.
        print("Settings changed")
        
        
    def startTextEditor(self):
        path = os.path.join("words", f"words_{self.lang_code}.txt")
        start_text_editor.open_with_webbrowser(path)
    
        
    def updateBackgroundColorLabel(self):
        # Get the selected color from the combo box and update the label
        selected_color = self.background_color_combo.currentData()
        self.background_label.setStyleSheet("background-color: %s;" % selected_color.name())
        self.background_label.setText(selected_color.name())
    
    
    def updateTextColorLabel(self):
        # Get the selected color from the combo box and update the label
        selected_color = self.text_color_combo.currentData()
        self.text_color_label.setStyleSheet("background-color: %s;" % selected_color.name())
        self.text_color_label.setText(selected_color.name())
        
        
    def createColorIcon(self, color):
        # Create a color icon with the given color
        pixmap = QPixmap(16, 16)
        pixmap.fill(color)
        icon = QIcon(pixmap)
        return icon

        
    def showAboutDialog(self):
        aboutDialog = QDialog(self)
        aboutDialog.setWindowTitle(self.mt_about)

        layout = QtWidgets.QVBoxLayout(aboutDialog)
        current_year = str(datetime.now().year)
        #label = QtWidgets.QLabel(f"This app is free to use.\nDonations are much apprecieated and makes\ncontinued developement possible. \
                                 #\n\nWebsite: wartem.se\n\nCopyright © {current_year} Mårten Wasteson. All rights reserved.\nAlias Wartem.")
        label = QLabel(f"""<b>ABC Trainer</b><br>Version 1.0<br><br>ABC Trainer is a specialized to helps users learn the letters of the alphabet<br>through 
                       four interactive exercises. The goal of each excersise<br>is to press the correct keys (A-Z) on your keyboard.
                       <br>
                       <br>Customize your experience from the settings menu, accessed by clicking on 'File' in the menu bar.
                       <br>Settings such as audio volume, language and color scheme can be adjusted here.
                       
                       <br>
                       <br>This app is free to use and offered to users without any cost.
                       <br>We greatly appreciate donations, as they support our ongoing development efforts.<br>
                      <br>For more information, please visit our website at: <a href="https://wartem.se">wartem.se</a><br><br>Copyright © {current_year} Mårten Wasteson. All rights reserved.<br>Alias Wartem.""")
    
        # Set text interaction flags to enable link interaction
        label.setTextInteractionFlags(Qt.TextBrowserInteraction)

        # Connect the linkActivated signal to a slot
        label.linkActivated.connect(self.link_clicked)
        
        layout.addWidget(label)
        aboutDialog.exec()
        
        
    def link_clicked(self, link):
        import webbrowser
        webbrowser.open(link)
    

    def showSettingsDialog(self):
        settingsDialog = QDialog(self)
        settingsDialog.setWindowTitle('Settings')

        self.formLayout = QFormLayout()
        
        # Screen category
        self.user_pref = QLabel('<b>User preferences</b>')
        self.formLayout.addRow(self.user_pref)
        
        self.instructionsCheckBox = QtWidgets.QCheckBox()
        instructions_checked = Qt.Checked if self.settings["instructions"] else Qt.Unchecked
        self.instructionsCheckBox.setCheckState(instructions_checked)
        self.formLayout.addRow('Instructions in games', self.instructionsCheckBox)
        #self.instructionsCheckBox.setVisible(False)
        
        self.slow_speechCheckBox = QtWidgets.QCheckBox()
        slow_speech_checked = Qt.Checked if self.settings["slow_speech"] else Qt.Unchecked
        self.slow_speechCheckBox.setCheckState(slow_speech_checked)
        self.formLayout.addRow('Slow speech', self.slow_speechCheckBox)
        
        self.userNameLineEdit = QLineEdit(self.settings["user_name"])
        self.userNameLineEdit.setToolTip("These letters are used as initial letters used in the exercise 'Mixed'")
        self.formLayout.addRow('Username', self.userNameLineEdit)
        
        self.repetitionsLineEdit = QLineEdit(str(self.settings["repetitions"]))
        self.repetitionsLineEdit.setToolTip("Number of times chars are used in the exercise 'Mixed'")
        self.formLayout.addRow('Repetitions for Mixed', self.repetitionsLineEdit)
        
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setValue(self.settings["volume"])
        self.volume_slider.setToolTip("Volume slider")
        self.formLayout.addRow("Audio volume", self.volume_slider)
        
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        self.formLayout.addRow(line)

        self.formLayout.addRow(QLabel('<br>'))
        
        # Screen category
        self.game_screens = QLabel('<b>Game Screens</b>')
        self.formLayout.addRow(self.game_screens)
        
        self.fullScreenCheckBox = QtWidgets.QCheckBox()
        full_screen_checked = Qt.Checked if self.settings["full_screen"] else Qt.Unchecked
        self.fullScreenCheckBox.setCheckState(full_screen_checked)
        self.formLayout.addRow('Full screen', self.fullScreenCheckBox)
        
        colors = {k.title() : QColor(v) for k,v in ColorConst().colors_gpt.items()}
        
        # Create the combo box and add the background color items
        self.background_color_combo = QComboBox(self)
        for color_name, color_value in colors.items():
            color_icon = self.createColorIcon(color_value)
            self.background_color_combo.addItem(color_icon, color_name, color_value)

        # Connect the combo box to a slot to update the label
        self.background_color_combo.currentIndexChanged.connect(self.updateBackgroundColorLabel)

        # Create a label to show the selected color
        self.background_label = QLabel(self)
        self.background_label.setMinimumSize(100, 20)

        # Create the layout and add the combo box and label
        self.hbox_background = QHBoxLayout()
        self.hbox_background.addWidget(self.background_color_combo)
        self.hbox_background.addWidget(self.background_label)
        self.setLayout(self.hbox_background)

        # Set the initial label text
        self.updateBackgroundColorLabel()

        # Set the default value of the combo box to self.settings["background_color"]
        self.background_color = self.settings["background_color"]
        for i in range(self.background_color_combo.count()):
            if self.background_color_combo.itemData(i) == self.background_color:
                self.background_color_combo.setCurrentIndex(i)
                break

        self.formLayout.addRow('Background Color', self.hbox_background)
        

        # Create the combo box and add the text color items
        self.text_color_combo = QComboBox(self)
        for color_name, color_value in colors.items():
            color_icon = self.createColorIcon(color_value)
            self.text_color_combo.addItem(color_icon, color_name, color_value)

        # Connect the combo box to a slot to update the label
        self.text_color_combo.currentIndexChanged.connect(self.updateTextColorLabel)

        # Create a label to show the selected color
        self.text_color_label = QLabel(self)
        self.text_color_label.setMinimumSize(100, 20)

        # Create the layout and add the combo box and label
        self.text_color_hbox = QHBoxLayout()
        self.text_color_hbox.addWidget(self.text_color_combo)
        self.text_color_hbox.addWidget(self.text_color_label)
        self.setLayout(self.text_color_hbox)

        # Set the initial label text
        self.updateTextColorLabel()

        self.formLayout.addRow('Text Color', self.text_color_hbox)
        
        self.windowWidthLineEdit = QLineEdit(str(self.settings["window_width"]))
        self.formLayout.addRow('Window width', self.windowWidthLineEdit)
        
        self.windowHeightLineEdit = QLineEdit(str(self.settings["window_height"]))
        self.formLayout.addRow('Window height', self.windowHeightLineEdit)
        
        self.languageComboBox = QComboBox()
        _lang = ['English', 'French', 'German', 'Italian', 'Spanish', 'Portuguese', 'Swedish', 'Danish', 'Norwegian', 
                                        'Finnish', 'Polish', 'Dutch','Afrikaans', 'Albanian', 'Esperanto', 'Estonian', 'Croatian', 
                                        'Haitian Creole', 'Hungarian', 'Indonesian', 'Icelandic', 'Latvian', 'Lithuanian', 'Romanian', 
                                        'Slovak', 'Slovenian', 'Tagalog (Filipino)', 'Czech', 'Turkish', 'Vietnamese']
        _lang.sort()
        self.languageComboBox.addItems(_lang)

        index = self.languageComboBox.findText(self.settings["language"])
        
        if index != -1:
            self.languageComboBox.setCurrentIndex(index)
            
        self.formLayout.addRow('Language', self.languageComboBox)
        
        self.fontComboBox = QComboBox() # , 'Futura''
        self.fontComboBox.addItems(self.pyside6_fonts.keys())
        index = self.fontComboBox.findText(self.settings["font"].title())

        if index != -1:
            self.fontComboBox.setCurrentIndex(index)
            
        self.formLayout.addRow('Font', self.fontComboBox)
        
        self.caseComboBox = QComboBox()
        self.caseComboBox.addItems(['UPPER', 'lower', 'Both'])
        index = self.caseComboBox.findText(self.settings["letter_case"])
        
        if index != -1:
            self.caseComboBox.setCurrentIndex(index)
            
        self.formLayout.addRow('Letter case', self.caseComboBox)
        
        self.excludedCharsLineEdit = QLineEdit(self.settings["excluded_characters"])
        self.excludedCharsLineEdit.setToolTip("(Case sensitive)")
        self.formLayout.addRow('Excluded characters', self.excludedCharsLineEdit)
        
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(settingsDialog.accept)
        buttonBox.rejected.connect(settingsDialog.reject)
        self.formLayout.addRow(buttonBox)
        
        settingsDialog.setLayout(self.formLayout)
        settingsDialog.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        
        self.trans_menu()
        
        result = settingsDialog.exec() 
        
        if result == QDialog.Accepted:
            # ToDO: Check types and type casting to avoid exceptions
            
            #try:
                new_settings = {
                "user_name": self.userNameLineEdit.text(),
                "slow_speech": self.slow_speechCheckBox.checkState() == Qt.Checked,
                "language": self.languageComboBox.currentText(),
                "repetitions": int(self.repetitionsLineEdit.text()) if self.repetitionsLineEdit.text().isdigit() else 1,
                "letter_case": self.caseComboBox.currentText(),
                "instructions": self.instructionsCheckBox.checkState() == Qt.Checked,
                "font": self.fontComboBox.currentText(),
                "text_color": self.text_color_label.text(),
                "full_screen": self.fullScreenCheckBox.checkState() == Qt.Checked,
                "window_width": int(self.windowWidthLineEdit.text()),
                "window_height": int(self.windowHeightLineEdit.text()),
                "background_color": self.background_label.text(),
                "excluded_characters": self.excludedCharsLineEdit.text(),
                "volume": self.volume_slider.value()
                }
                
                Settings.write_settings(new_settings)
                
                self.handleSettingsChanged.emit()
                self.settings = new_settings
                self.read_menu_titles()
                self.trans_menu()
                self.reconfig_buttons()
                
    
    def init_pygame(self):
        self.setVisible(False)
        pygame.init()
        
    def set_icon(self):
        icon = pygame.image.load(self.window_icon_path).convert_alpha() 
        pygame.display.set_icon(icon)

    def update_menu(self):
        self.setVisible(True)
        pygame.quit()
    
    
    # ToDO: Add try catch for all
    
    def show_pygame_1(self):
        self.init_pygame()
        game = GameLetterMix()
        self.set_icon()
        game.game_loop()
        self.update_menu()
    
    def show_pygame_2(self):
        self.init_pygame()
        game = GameAllOnce()
        self.set_icon()
        game.game_loop()
        self.update_menu()
    
    def show_pygame_3(self):
        self.init_pygame()
        game = GameWords()
        self.set_icon()
        game.game_loop()
        self.update_menu()
    
    def show_pygame_4(self):
        self.init_pygame()
        game = GameRemoveWhat()
        self.set_icon()
        game.game_loop()
        self.update_menu()
        

def start():
    locale.setlocale(locale.LC_ALL, "") # toDo: Can this be put in main.py? "unused" - gpt
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(app)
    window.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
    window.show()
    
    sys.exit(app.exec())
