from threading import Thread
from remi import start
from wwbox.web import *


class WWWewThread(Thread):
    def __init__(self, App):
        Thread.__init__(self)
        self.app = App
        self.server

    def run(self):
        self.server = start(self.app, address='0.0.0.0', port=8080, start_browser=True,
                            multiple_instance=True)


t = WWWewThread(WebApp)
#t.start()
t.server._gui.ui = 'poll'
print(t.server._gui.ui)
