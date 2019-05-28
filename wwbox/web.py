from remi.gui import *
from remi import start as remi_start
from remi import App
from threading import Thread

ui = 'login'


class WebApp(App):
    def __init__(self, *args, **kwargs):
        if not 'editing_mode' in kwargs.keys():
            super(WebApp, self).__init__(*args, static_file_path={'my_res': './res/'})

    def idle(self):
        """idle function called every update cycle"""
        if ui == 'config':
            self.set_root_widget(self.login_ui)
        if ui == 'end':
            self.set_root_widget(self.end_ui)
        if ui == 'info':
            self.set_root_widget(self.info_ui)
        if ui == 'login':
            self.set_root_widget(self.login_ui)
        if ui == 'poll':
            self.set_root_widget(self.poll_ui)
        if ui == 'tutorial':
            self.set_root_widget(self.tutorial_ui)

    def main(self):
        self.construct_config_ui()
        self.construct_end_ui()
        self.construct_info_ui()
        self.construct_login_ui()
        self.construct_poll_ui()
        self.construct_tutorial_ui()
        return self.login_ui

    def construct_config_ui(self):
        hboxMain = HBox()
        hboxMain.attributes.update(
            {"class": "HBox", "editor_constructor": "()", "editor_varname": "hboxMain", "editor_tag_type": "widget",
             "editor_newclass": "False", "editor_baseclass": "HBox"})
        hboxMain.style.update(
            {"margin": "0px", "width": "1019px", "height": "844px", "top": "9px", "left": "12px",
             "position": "absolute",
             "display": "flex", "justify-content": "space-around", "align-items": "center", "flex-direction": "row",
             "overflow": "auto"})
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
             "overflow": "auto", "order": "-1", "font-size": "40px", "font-weight": "bolder",
             "font-style": "normal"})
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
        ddScenario = DropDown()
        ddScenario.attributes.update(
            {"class": "DropDown", "editor_constructor": "()", "editor_varname": "ddScenario",
             "editor_tag_type": "widget",
             "editor_newclass": "False", "editor_baseclass": "DropDown"})
        ddScenario.style.update(
            {"margin": "0px", "width": "188.0px", "height": "65.0px", "top": "20px", "position": "static",
             "overflow": "auto", "order": "-1"})
        vboxMain.append(ddScenario, 'ddScenario')
        btStart = Button('Spiel starten')
        btStart.attributes.update(
            {"class": "Button", "editor_constructor": "('Spiel starten')", "editor_varname": "btStart",
             "editor_tag_type": "widget", "editor_newclass": "False", "editor_baseclass": "Button"})
        btStart.style.update(
            {"margin": "0px", "width": "186.0px", "height": "66.0px", "top": "20px", "position": "static",
             "overflow": "auto", "order": "-1"})
        vboxMain.append(btStart, 'btStart')
        lblMadeBy = Label('made by Henry & Christopher with ❤️')
        lblMadeBy.attributes.update({"class": "Label", "editor_constructor": "('made by Henry & Christopher with ❤️')",
                                     "editor_varname": "lblMadeBy", "editor_tag_type": "widget",
                                     "editor_newclass": "False",
                                     "editor_baseclass": "Label"})
        lblMadeBy.style.update(
            {"margin": "0px", "width": "236.0px", "height": "264.0px", "top": "20px", "position": "static",
             "overflow": "auto", "order": "-1", "box-shadow": "0 0 10px rgb(33,150,243)"})
        vboxMain.append(lblMadeBy, 'lblMadeBy')
        hboxMain.append(vboxMain, 'vboxMain')

        self.config_ui = hboxMain
        return self.config_ui

    def construct_end_ui(self):
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
        listRoles = TableWidget(2, 2, True, False)
        listRoles.attributes.update(
            {"class": "TableWidget", "editor_constructor": "(2,2,True,False)", "editor_varname": "listRoles",
             "editor_tag_type": "widget", "editor_newclass": "False", "editor_baseclass": "TableWidget"})
        listRoles.style.update(
            {"margin": "0px", "width": "100px", "height": "100px", "top": "20px", "position": "static", "float": "none",
             "display": "table", "overflow": "auto", "order": "-1"})
        vboxMain.append(listRoles, 'listRoles')
        hboxMain.append(vboxMain, 'vboxMain')

        self.end_ui = hboxMain
        return self.end_ui

    def construct_info_ui(self):
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
        imgPicture = Image('bild.png')
        imgPicture.attributes.update(
            {"class": "Image", "src": "bild.png", "editor_constructor": "('bild.png')", "editor_varname": "imgPicture",
             "editor_tag_type": "widget", "editor_newclass": "False", "editor_baseclass": "Image"})
        imgPicture.style.update(
            {"margin": "0px", "width": "100px", "height": "100px", "top": "20px", "position": "static",
             "overflow": "auto", "order": "-1"})
        vboxMain.append(imgPicture, 'imgPicture')
        hboxMain.append(vboxMain, 'vboxMain')

        self.info_ui = hboxMain
        return self.info_ui

    def construct_login_ui(self):
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

        self.login_ui = hboxMain
        return self.login_ui

    def construct_poll_ui(self):
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

        self.poll_ui = hboxMain
        return self.poll_ui

    def construct_tutorial_ui(self):
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
        ddScenario = DropDown()
        ddScenario.attributes.update({"class": "DropDown", "editor_constructor": "()", "editor_varname": "ddScenario",
                                      "editor_tag_type": "widget", "editor_newclass": "False",
                                      "editor_baseclass": "DropDown"})
        ddScenario.style.update(
            {"margin": "0px", "width": "188.0px", "height": "65.0px", "top": "20px", "position": "static",
             "overflow": "auto", "order": "-1"})
        vboxMain.append(ddScenario, 'ddScenario')
        ListViewesdklfjasdfklj = Label('Durch ListView ersetzen')
        ListViewesdklfjasdfklj.attributes.update({"class": "Label", "editor_constructor": "('Durch ListView ersetzen')",
                                                  "editor_varname": "ListViewesdklfjasdfklj",
                                                  "editor_tag_type": "widget", "editor_newclass": "False",
                                                  "editor_baseclass": "Label"})
        ListViewesdklfjasdfklj.style.update(
            {"margin": "0px", "width": "100px", "height": "30px", "top": "20px", "position": "static",
             "overflow": "auto", "order": "-1"})
        vboxMain.append(ListViewesdklfjasdfklj, 'ListViewesdklfjasdfklj')
        lblMadeBy = Label('made by Henry & Christopher with ❤️')
        lblMadeBy.attributes.update({"class": "Label", "editor_constructor": "('made by Henry & Christopher with ❤️')",
                                     "editor_varname": "lblMadeBy", "editor_tag_type": "widget",
                                     "editor_newclass": "False", "editor_baseclass": "Label"})
        lblMadeBy.style.update(
            {"margin": "0px", "width": "236.0px", "height": "264.0px", "top": "20px", "position": "static",
             "overflow": "auto", "order": "-1", "box-shadow": "0 0 10px rgb(33,150,243)"})
        vboxMain.append(lblMadeBy, 'lblMadeBy')
        hboxMain.append(vboxMain, 'vboxMain')

        self.tutorial_ui = hboxMain
        return self.tutorial_ui


class WebThread(Thread):
    def __init__(self, App):
        Thread.__init__(self)
        self.app = App

    def run(self):
        # Configuration
        configuration = {'config_project_name': 'Login', 'config_address': '0.0.0.0', 'config_port': 8081,
                         'config_multiple_instance': True, 'config_enable_file_cache': False,
                         'config_start_browser': True, 'config_resourcepath': './res/'}

        # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
        remi_start(WebApp, address=configuration['config_address'], port=configuration['config_port'],
                   multiple_instance=configuration['config_multiple_instance'],
                   enable_file_cache=configuration['config_enable_file_cache'],
                   start_browser=configuration['config_start_browser'])


t = WebThread(WebApp)
t.start()
ui = 'poll'
