import remi.gui as gui
from remi import start, App


class WWWeb(App):
    def main(self):
        # creating a container GridBox type
        self.main_container = gui.GridBox(width='100%', height='100%',
                                          style={'margin': '0px auto', 'font-family': 'Verdana'})

        title = gui.Label('Hallo, herzlich willkommen zu Werwolf!', width='100%',
                          style={'font-size': '2em', 'display': 'block', 'margin': 'auto'})

        login = gui.Button('Anmelden', height='20%', style={'display': 'block', 'margin': 'auto'})

        login.onclick.do(self.on_button_pressed)
        config = gui.Button('Spiel konfigurieren', height='20%', style={'display': 'block', 'margin': 'auto'})

        config.onclick.do(self.on_button_pressed)
        # defining layout matrix, have to be iterable of iterable
        self.main_container.define_grid(['t',
                                         'a',
                                         'c'])
        self.main_container.append({'t': title, 'a': login, 'c': config})
        # setting sizes for rows and columns
        self.main_container.style.update({'grid-template-columns': '100%', 'grid-template-rows': '10% 45% 45%'})

        # returning the root widget

        return self.main_container
    def idle(self):
        print('Test')

    def onresize(self, emitter, width, height):
        # redefining grid layout
        if float(width) < float(height):
            self.main_container.define_grid(['t', 'a', 'c'])
            self.main_container.style.update({'grid-template-columns': '100%', 'grid-template-rows': '10% 45% 45%'})
        else:
            self.main_container.define_grid(['t',
                                             'a'])
            self.main_container.style.update({'grid-template-columns': '100%', 'grid-template-rows': '10% 45% 45%'})

    def on_button_pressed(self, button):
        button.set_text('Hi')


if __name__ == "__main__":
    # starts the webserver
    start(WWWeb, address='0.0.0.0', port=8080, start_browser=False, multiple_instance=True)
