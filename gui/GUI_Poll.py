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
        hboxMain.style.update(
            {"margin": "0px", "display": "flex", "justify-content": "space-around", "align-items": "center",
             "flex-direction": "row", "width": "1019px", "height": "844px", "top": "9px", "left": "12px",
             "position": "absolute", "overflow": "auto"})
        vboxMain = VBox()
        vboxMain.attributes.update(
            {"class": "VBox", "editor_constructor": "()", "editor_varname": "vboxMain", "editor_tag_type": "widget",
             "editor_newclass": "False", "editor_baseclass": "VBox"})
        vboxMain.style.update(
            {"margin": "0px", "display": "flex", "justify-content": "space-around", "align-items": "center",
             "flex-direction": "column", "width": "882.0px", "height": "735.0px", "top": "86.0px", "position": "static",
             "overflow": "auto", "order": "-1"})
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
             "overflow": "auto", "order": "-1"})
        vboxMain.append(lblText, 'lblText')
        ListViewWidGEDSDFJAKSDFAS = Label('Bitte durch ListView ersetzen')
        ListViewWidGEDSDFJAKSDFAS.attributes.update(
            {"class": "Label", "editor_constructor": "('Bitte durch ListView ersetzen')",
             "editor_varname": "ListViewWidGEDSDFJAKSDFAS", "editor_tag_type": "widget", "editor_newclass": "False",
             "editor_baseclass": "Label"})
        ListViewWidGEDSDFJAKSDFAS.style.update(
            {"margin": "0px", "width": "100px", "height": "30px", "top": "20px", "position": "static",
             "overflow": "auto", "order": "-1"})
        vboxMain.append(ListViewWidGEDSDFJAKSDFAS, 'ListViewWidGEDSDFJAKSDFAS')
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
