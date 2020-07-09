#-*- coding:utf-8 -*-

import argparse
from utils.Logger import *
from Runner import *

def run(args):
    _type = args.type.upper()
    runner = Runner(type=_type)
    runner.run()


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description='')
    argparser.add_argument('--type', required=True, help='select type()')
    args = argparser.parse_args()
    logger = get_logger("app")
    run(args)