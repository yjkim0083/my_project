from data.stock import *
from db import *
from utils.Logger import *


class Runner:

    def __init__(self, **kwargs):
        self._type = kwargs['type']

    def run(self):
        """
        :rtype: obejct

        """
        df = download_stock_codes('kospi')
        print(type(df))
        print(df.head())
