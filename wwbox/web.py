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

    def construct_root_ui(self):
        self.hboxMain = HBox()
        self.hboxMain.attributes.update(
            {"class": "HBox", "editor_constructor": "()", "editor_varname": "hboxMain", "editor_tag_type": "widget",
             "editor_newclass": "False", "editor_baseclass": "HBox"})
        self.hboxMain.style.update(
            {"margin": "0px", "width": "1019px", "height": "844px", "top": "9px", "left": "12px",
             "position": "absolute",
             "display": "flex", "justify-content": "space-around", "align-items": "center", "flex-direction": "row",
             "overflow": "auto"})
        self.vboxMain = VBox()
        self.vboxMain.attributes.update(
            {"class": "VBox", "editor_constructor": "()", "editor_varname": "vboxMain", "editor_tag_type": "widget",
             "editor_newclass": "False", "editor_baseclass": "VBox"})
        self.vboxMain.style.update(
            {"margin": "0px", "width": "882.0px", "height": "735.0px", "top": "86.0px", "position": "static",
             "display": "flex", "justify-content": "space-around", "align-items": "center", "flex-direction": "column",
             "overflow": "auto", "order": "-1", "left": "116.0px"})

    def construct_basic_ui(self):

        self.lblTitle = Label('WW-Box')
        self.lblTitle.attributes.update(
            {"class": "Label", "editor_constructor": "('WW-Box')", "editor_varname": "lblTitle",
             "editor_tag_type": "widget", "editor_newclass": "False",
             "editor_baseclass": "Label"})
        self.lblTitle.style.update(
            {"margin": "0px", "width": "169.0px", "height": "42.0px", "top": "20px", "position": "static",
             "overflow": "auto", "order": "-1", "font-size": "40px", "font-weight": "bolder",
             "font-style": "normal"})

        self.lblText = Label('Wenn du mitspielen möchtest drücke auf ')
        self.lblText.attributes.update(
            {"class": "Label", "editor_constructor": "('Wenn du mitspielen möchtest drücke auf ')",
             "editor_varname": "lblText", "editor_tag_type": "widget", "editor_newclass": "False",
             "editor_baseclass": "Label"})
        self.lblText.style.update(
            {"margin": "0px", "width": "260.0px", "height": "27.0px", "top": "380.0px", "position": "static",
             "overflow": "auto", "order": "-1", "left": "382.0px"})

        self.lblText2 = Label('Wenn du ein Spiel starten oder konfigurieren möchtest drücke auf ')
        self.lblText2.attributes.update({"class": "Label",
                                         "editor_constructor": "('Wenn du ein Spiel starten oder konfigurieren möchtest drücke auf ')",
                                         "editor_varname": "lblText2", "editor_tag_type": "widget",
                                         "editor_newclass": "False", "editor_baseclass": "Label"})
        self.lblText2.style.update(
            {"margin": "0px", "width": "217.0px", "height": "57.0px", "top": "20px", "position": "static",
             "overflow": "auto", "order": "-1"})

        self.ddScenario = DropDown()
        self.ddScenario.attributes.update(
            {"class": "DropDown", "editor_constructor": "()", "editor_varname": "ddScenario",
             "editor_tag_type": "widget",
             "editor_newclass": "False", "editor_baseclass": "DropDown"})
        self.ddScenario.style.update(
            {"margin": "0px", "width": "188.0px", "height": "65.0px", "top": "20px", "position": "static",
             "overflow": "auto", "order": "-1"})

        self.btStart = Button('Spiel starten')
        self.btStart.attributes.update(
            {"class": "Button", "editor_constructor": "('Spiel starten')", "editor_varname": "btStart",
             "editor_tag_type": "widget", "editor_newclass": "False", "editor_baseclass": "Button"})
        self.btStart.style.update(
            {"margin": "0px", "width": "186.0px", "height": "66.0px", "top": "20px", "position": "static",
             "overflow": "auto", "order": "-1"})
        self.btStart.onclick.do(self.on_start_pressed)

        self.btLogin = Button('Anmelden')
        self.btLogin.attributes.update(
            {"class": "Button", "editor_constructor": "('Anmelden')", "editor_varname": "btLogin",
             "editor_tag_type": "widget", "editor_newclass": "False",
             "editor_baseclass": "Button"})
        self.btLogin.style.update(
            {"margin": "0px", "width": "123.0px", "height": "38.0px", "top": "20px", "position": "static",
             "overflow": "auto", "order": "-1"})
        self.btLogin.onclick.do(self.on_login_pressed)

        self.btConf = Button('Konfigurieren')
        self.btConf.attributes.update(
            {"class": "Button", "editor_constructor": "('Konfigurieren')", "editor_varname": "btConf",
             "editor_tag_type": "widget", "editor_newclass": "False", "editor_baseclass": "Button"})
        self.btConf.style.update(
            {"margin": "0px", "width": "118.0px", "height": "38.0px", "top": "20px", "position": "static",
             "overflow": "auto", "order": "-1"})
        self.btConf.onclick.do(self.on_config_pressed)

        self.lblMadeBy = Label('made by Henry & Christopher with ❤️')
        self.lblMadeBy.attributes.update(
            {"class": "Label", "editor_constructor": "('made by Henry & Christopher with ❤️')",
             "editor_varname": "lblMadeBy", "editor_tag_type": "widget",
             "editor_newclass": "False",
             "editor_baseclass": "Label"})
        self.lblMadeBy.style.update(
            {"margin": "0px", "width": "236.0px", "height": "264.0px", "top": "20px", "position": "static",
             "overflow": "auto", "order": "-1", "box-shadow": "0 0 10px rgb(33,150,243)"})

        self.imgPicture = Image('bild.png')
        self.imgPicture.attributes.update(
            {"class": "Image", "src": "bild.png", "editor_constructor": "('bild.png')", "editor_varname": "imgPicture",
             "editor_tag_type": "widget", "editor_newclass": "False", "editor_baseclass": "Image"})
        self.imgPicture.style.update(
            {"margin": "0px", "width": "100px", "height": "100px", "top": "20px", "position": "static",
             "overflow": "auto", "order": "-1"})

        self.listRoles = TableWidget(2, 2, True, False)
        self.listRoles.attributes.update(
            {"class": "TableWidget", "editor_constructor": "(2,2,True,False)", "editor_varname": "listRoles",
             "editor_tag_type": "widget", "editor_newclass": "False", "editor_baseclass": "TableWidget"})
        self.listRoles.style.update(
            {"margin": "0px", "width": "100px", "height": "100px", "top": "20px", "position": "static", "float": "none",
             "display": "table", "overflow": "auto", "order": "-1"})

        items = []
        self.lvPoll = ListView.new_from_list(items, width=300, height=120, margin='10px')
        self.lvPoll.onselection.do(self.lvPoll_on_selected)

        self.lvTutorial = ListView.new_from_list(items, width=300, height=120, margin='10px')
        self.lvTutorial.onselection.do(self.lvTutorial_on_selected)

    def construct_config_ui(self):
        self.construct_root_ui()

        self.vboxMain.append(self.lblTitle, 'lblTitle')

        self.vboxMain.append(self.lblText, 'lblText')

        self.vboxMain.append(self.ddScenario, 'ddScenario')

        self.vboxMain.append(self.btStart, 'btStart')

        self.vboxMain.append(self.lblMadeBy, 'lblMadeBy')
        self.hboxMain.append(self.vboxMain, 'vboxMain')

        self.config_ui = self.hboxMain
        return self.config_ui

    def construct_end_ui(self):
        self.construct_root_ui()

        self.vboxMain.append(self.lblTitle, 'lblTitle')
        self.vboxMain.append(self.lblText, 'lblText')

        self.vboxMain.append(self.listRoles, 'listRoles')
        self.hboxMain.append(self.vboxMain, 'vboxMain')

        self.end_ui = self.hboxMain
        return self.end_ui

    def construct_info_ui(self):
        self.construct_root_ui()

        self.vboxMain.append(self.lblTitle, 'lblTitle')

        self.vboxMain.append(self.lblText, 'lblText')

        self.vboxMain.append(self.imgPicture, 'imgPicture')
        self.hboxMain.append(self.vboxMain, 'vboxMain')

        self.info_ui = self.hboxMain
        return self.info_ui

    def construct_login_ui(self):
        self.construct_root_ui()

        self.vboxMain.append(self.lblTitle, 'lblTitle')

        self.vboxMain.append(self.lblText, 'lblText')

        self.vboxMain.append(self.btLogin, 'btLogin')

        self.vboxMain.append(self.lblText2, 'lblText2')

        self.vboxMain.append(self.btConf, 'btConf')

        self.vboxMain.append(self.lblMadeBy, 'lblMadeBy')
        self.hboxMain.append(self.vboxMain, 'self.vboxMain')

        self.login_ui = self.hboxMain
        return self.login_ui

    def construct_poll_ui(self):
        self.construct_root_ui()

        self.vboxMain.append(self.lblTitle, 'lblTitle')

        self.vboxMain.append(self.lblText, 'lblText')

        self.vboxMain.append(self.lvPoll, 'lvPoll')
        self.hboxMain.append(self.vboxMain, 'vboxMain')

        self.poll_ui = self.hboxMain
        return self.poll_ui

    def construct_tutorial_ui(self):
        self.construct_root_ui()

        self.vboxMain.append(self.lblTitle, 'lblTitle')

        self.vboxMain.append(self.lblText, 'lblText')

        self.vboxMain.append(self.ddScenario, 'ddScenario')

        self.vboxMain.append(self.lvTutorial, 'lvTutorial')

        self.vboxMain.append(self.lblMadeBy, 'lblMadeBy')
        self.hboxMain.append(self.vboxMain, 'vboxMain')

        self.tutorial_ui = self.hboxMain
        return self.tutorial_ui

    def on_start_pressed(self):
        print('Start!')  # TODO

    def on_login_pressed(self):
        print('LOGIN')  # TODO

    def on_config_pressed(self):
        print('CONFIG')  # TODO

    def lvPoll_on_selected(self, widget, selected_item_key):
        """ The selection event of the listView, returns a key of the clicked event.
            You can retrieve the item rapidly
        """
        # self.lbl.set_text('List selection: ' + self.listView.children[selected_item_key].get_text())
        print('POLL_Abstimmung')  # TODO

    def lvTutorial_on_selected(self, widget, selected_item_key):
        """ The selection event of the listView, returns a key of the clicked event.
            You can retrieve the item rapidly
        """
        # self.lbl.set_text('List selection: ' + self.listView.children[selected_item_key].get_text())
        print('TUTORIAL_SELECTED')  # TODO


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
