# -*- coding: utf-8 -*-


class fwfileError(Exception):
    """Excessao base para o CNAB 240"""


class AssignmentFieldError(fwfileError):
    """Tentativa de atribuicao de valor indevido ao campo"""

    def __init__(self, field, value):
        self.field = field
        self.value = value
        super(AssignmentFieldError, self).__init__()

    def __str__(self):
        return 'field:{0} format:{1} decimals:{2} digits:{3} - value:{4}'.\
            format(
                self.field.name,
                self.field.formatting,
                self.field.decimals,
                self.field.digits,
                repr(self.value),
            )


class NumDigitsExceededError(AssignmentFieldError):
    """Tentativa de atribuicao de valor mais longo que o campo suportaia"""


class TypeError(AssignmentFieldError):
    """Tentativa de atribuicao de tipo nao suportado pelo campo"""


class NumDecimalsError(AssignmentFieldError):
    """Numero de casasa decimais em desacordo com especificacao"""


class MissingArgsError(fwfileError):
    """Faltando argumentos na chamada do metodo"""

    def __init__(self, args_missing):
        self.args_missing = args_missing
        super(MissingArgsError, self).__init__()

    def __str__(self):
        return ('The following kwargs are required and were not found: {0}').format(', '.join(self.args_missing))


class EmptyFileError(fwfileError):
    """Tentativa de escrita de arquivo vazio."""


class NoneEventError(fwfileError):
    """Tentativa de escrita de lote sem eventos. """


class RequiredFieldError(fwfileError):
    """Campo obrigatorio nao preenchido."""
