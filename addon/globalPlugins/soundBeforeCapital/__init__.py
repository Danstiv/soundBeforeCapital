import os

import globalPluginHandler
from speech import commands, speech

PATH_TO_SOUND = os.path.join(os.path.dirname(__file__), 'click.wav')


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.old_get_spelling_speech = speech.getSpellingSpeech
        speech.getSpellingSpeech = self.decorator(speech.getSpellingSpeech)

    def decorator(self, func):
        def wrapper(*args, **kwargs):
            for i in func(*args, **kwargs):
                if isinstance(i, commands.BeepCommand) and i.hz==2000 and i.left==50 and i.right==50 and i.length==50:
                    i = commands.WaveFileCommand(PATH_TO_SOUND)
                yield i
        return wrapper

    def terminate(self):
        speech.getSpellingSpeech = self.old_get_spelling_speech
