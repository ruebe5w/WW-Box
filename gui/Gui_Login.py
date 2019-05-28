# -*- coding: utf-8 -*-

import remi.gui as gui
from remi.gui import *
from remi import start, App


class Login(App):
    def __init__(self, *args, **kwargs):
        # DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        if not 'editing_mode' in kwargs.keys():
            super(Login, self).__init__(*args, static_file_path={'my_res': './res/'})

    def idle(self):
        # idle function called every update cycle
        pass

    def main(self):
        return Login.construct_ui(self)

    @staticmethod
    def construct_ui(self):
        # DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        hboxMain = HBox()
        hboxMain.attributes.update(
            {"class": "HBox", "editor_constructor": "()", "editor_varname": "hboxMain", "editor_tag_type": "widget",
             "editor_newclass": "False", "editor_baseclass": "HBox"})
        hboxMain.style.update({"margin": "0px", "width": "1019px", "height": "844px", "top": "9px", "left": "12px",
                               "position": "absolute", "display": "flex", "justify-content": "space-around",
                               "align-items": "center", "flex-direction": "row", "overflow": "auto"})
        vboxMain = VBox()
        vboxMain.attributes.update(
            {"class": "VBox", "editor_constructor": "()", "editor_varname": "vboxMain", "editor_tag_type": "widget",
             "editor_newclass": "False", "editor_baseclass": "VBox"})
        vboxMain.style.update(
            {"margin": "0px", "width": "882.0px", "height": "735.0px", "top": "86.0px", "position": "static",
             "display": "flex", "justify-content": "space-around", "align-items": "center", "flex-direction": "column",
             "overflow": "auto", "order": "-1", "left": "116.0px"})
        lblTitle = Label('WW-Box')
        lblTitle.attributes.update({"class": "Label", "editor_constructor": "('WW-Box')", "editor_varname": "lblTitle",
                                    "editor_tag_type": "widget", "editor_newclass": "False",
                                    "editor_baseclass": "Label"})
        lblTitle.style.update(
            {"margin": "0px", "width": "169.0px", "height": "42.0px", "top": "20px", "position": "static",
             "overflow": "auto", "order": "-1", "font-size": "40px", "font-weight": "bolder", "font-style": "normal"})
        vboxMain.append(lblTitle, 'lblTitle')
        lblText = Label('Wenn du mitspielen möchtest drücke auf ')
        lblText.attributes.update(
            {"class": "Label", "editor_constructor": "('Wenn du mitspielen möchtest drücke auf ')",
             "editor_varname": "lblText", "editor_tag_type": "widget", "editor_newclass": "False",
             "editor_baseclass": "Label"})
        lblText.style.update(
            {"margin": "0px", "width": "260.0px", "height": "27.0px", "top": "380.0px", "position": "static",
             "overflow": "auto", "order": "-1", "left": "382.0px"})
        vboxMain.append(lblText, 'lblText')
        btLogin = Button('Anmelden')
        btLogin.attributes.update({"class": "Button", "editor_constructor": "('Anmelden')", "editor_varname": "btLogin",
                                   "editor_tag_type": "widget", "editor_newclass": "False",
                                   "editor_baseclass": "Button"})
        btLogin.style.update(
            {"margin": "0px", "width": "123.0px", "height": "38.0px", "top": "20px", "position": "static",
             "overflow": "auto", "order": "-1"})
        vboxMain.append(btLogin, 'btLogin')
        lblText2 = Label('Wenn du ein Spiel starten oder konfigurieren möchtest drücke auf ')
        lblText2.attributes.update({"class": "Label",
                                    "editor_constructor": "('Wenn du ein Spiel starten oder konfigurieren möchtest drücke auf ')",
                                    "editor_varname": "lblText2", "editor_tag_type": "widget",
                                    "editor_newclass": "False", "editor_baseclass": "Label"})
        lblText2.style.update(
            {"margin": "0px", "width": "217.0px", "height": "57.0px", "top": "20px", "position": "static",
             "overflow": "auto", "order": "-1"})
        vboxMain.append(lblText2, 'lblText2')
        btConf = Button('Konfigurieren')
        btConf.attributes.update(
            {"class": "Button", "editor_constructor": "('Konfigurieren')", "editor_varname": "btConf",
             "editor_tag_type": "widget", "editor_newclass": "False", "editor_baseclass": "Button"})
        btConf.style.update(
            {"margin": "0px", "width": "118.0px", "height": "38.0px", "top": "20px", "position": "static",
             "overflow": "auto", "order": "-1"})
        vboxMain.append(btConf, 'btConf')
        lblMadeBy = Label('made by Henry & Christopher with ❤️')
        lblMadeBy.attributes.update({"class": "Label", "editor_constructor": "('made by Henry & Christopher with ❤️')",
                                     "editor_varname": "lblMadeBy", "editor_tag_type": "widget",
                                     "editor_newclass": "False", "editor_baseclass": "Label"})
        lblMadeBy.style.update(
            {"margin": "0px", "width": "236.0px", "height": "264.0px", "top": "20px", "position": "static",
             "overflow": "auto", "order": "-1"})
        vboxMain.append(lblMadeBy, 'lblMadeBy')
        hboxMain.append(vboxMain, 'vboxMain')

        self.hboxMain = hboxMain
        return self.hboxMain


# Configuration
configuration = {'config_project_name': 'Login', 'config_address': '0.0.0.0', 'config_port': 8081,
                 'config_multiple_instance': False, 'config_enable_file_cache': True, 'config_start_browser': True,
                 'config_resourcepath': './res/'}

if __name__ == "__main__":
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(Login, address=configuration['config_address'], port=configuration['config_port'],
          multiple_instance=configuration['config_multiple_instance'],
          enable_file_cache=configuration['config_enable_file_cache'],
          start_browser=configuration['config_start_browser'])
