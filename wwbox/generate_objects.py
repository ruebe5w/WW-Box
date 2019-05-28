from wwbox.scenario import Scenario
from wwbox.role import Role

s = Scenario(name='Flos Kuenstler-WG', author='Florian', description='Description',
             audios={'town_sleep': '../scenarios/audios/story_audio.mp3',
                     'story_audio': '../scenarios/audios/story_audio.mp3'}, img='',
             roles={})
s.write_to_file()

werwolf = Role('Werwolf', 'm', 1, 'Werwolf', )
