
from .registro import Register
from . import errors

class FWDataFile(object):
    
    def __init__(self, specs_dirpath: str):
        self._lines = []
        self._specs_dirpath = specs_dirpath
        self._registers = Register(self._specs_dirpath)

    @property
    def specs_dirpath(self):
        return self._specs_dirpath

    @specs_dirpath.setter
    def specs_dirpath(self, value):
        self._specs_dirpath = value
        self._registers = Register(self._specs_dirpath)
        
    def __str__(self):
        if not self._lines:
            raise errors.EmptyFileError()

        result = []
        result.extend(str(line) for line in self._lines)
        result.append('')
        return '\r\n'.join(result)
    
    def append_line(self, register, **kwargs):
        # registro = list(self._registers.__dict__)[0]
        self._lines.append(getattr(self._registers,register)(**kwargs))
        
        
        
        
        