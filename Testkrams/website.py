import remi.gui as gui
from remi import start, App


class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)


    def main(self):
        container = gui.VBox(width='100%', height='100%')
        self.lbl = gui.Label('Herzlich willkommen bei Werwolf! \nUm dich anzumelden, drücke auf "Anmelden".\n')
        self.btLogin = gui.Button('Anmelden')

        # setting the listener for the onclick event of the button
        self.btLogin.onclick.do(self.on_button_pressed)

        # appending a widget to another, the first argument is a string key
        container.append(self.lbl)
        container.append(self.bt)

        # returning the root widget
        return container

    # listener function
    def on_button_pressed(self, widget):
        self.lbl.set_text('Button pressed!')
        self.btLogin.set_text('Hi')


# starts the web server
start(MyApp, address='127.0.0.1', port=8080, multiple_instance=True, update_interval=0.1, start_browser=False)
