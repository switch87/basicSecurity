from ui.AvocadoCrypto_ui import Ui_dialog
from ui.uicontroller import UiController


class MainWindow(Ui_dialog):
    def setup_ui(self, dialog):
        super(MainWindow, self).setupUi(dialog)
        self.controller = UiController(self)

        # Source
        self.radio_button_file_source.clicked.connect(self.controller.set_source)
        self.radio_button_text_source.clicked.connect(self.controller.set_source)
        self.button_file_select.clicked.connect(self.controller.select_source_file)
        self.button_decrypt.clicked.connect(self.controller.decrypt)
        self.button_encrypt.clicked.connect(self.controller.encrypt)

        # Keys
        # Tools
        self.button_gen_keys.clicked.connect(self.controller.generate_all_keys)
        self.button_gen_aes.clicked.connect(self.controller.generate_aes)
        self.button_gen_own_rsa.clicked.connect(self.controller.generate_own_rsa)
        self.button_gen_rec_rsa.clicked.connect(self.controller.generate_res_rsa)
        self.button_switch_rsa.clicked.connect(self.controller.switch_rsa)
        self.check_box_md5.stateChanged.connect(self.controller.toggle_md5)
