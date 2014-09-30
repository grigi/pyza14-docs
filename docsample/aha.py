'''Contrived `ls` '''
import os

class aha():
    '''Aha! lists path contents'''

    def __init__(self, path):
        self.path = path

    @property
    def exists(self):
        '''Checks wether path exists'''
        return os.path.exists(self.path)

    def ls(self):
        '''Returns a list of path contents'''
        if self.exists:
            return os.listdir(self.path)
        else:
            return None
