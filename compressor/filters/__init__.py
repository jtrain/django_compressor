from compressor.exceptions import FilterError
from compressor.utils import get_class, get_mod_func

class FilterBase(object):
    def __init__(self, content, filter_type=None, verbose=0):
        self.type = filter_type
        self.content = content
        self.verbose = verbose

    def input(self, **kwargs):
        raise NotImplementedError
    def output(self, **kwargs):
        raise NotImplementedError
