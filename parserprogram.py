from argparse import ArgumentParser
from convert_to_cfg import file_to_cfg
from convert_to_cnf import cfg_to_cnf
from cyk import cyk
from lexer import tokenToStr
from colorama import Fore

def red() :
    print("\033[31m", end='')

def green() :
    print("\033[32m", end='')

def reset() :
    print("\033[0m", end='')

if __name__ == "__main__":
    # command parser
    argParser = ArgumentParser()
    argParser.add_argument("filename", type=str)
    args = argParser.parse_args()
    
    #print(args.filename)
    #print(tokenToStr(args.filename))
    # cek
    if (cyk(cfg_to_cnf(file_to_cfg("grammar.txt")),tokenToStr(args.filename))):
        green()
        print("Accepted")
        reset()
    else:
        red()
        print("Syntax Error")
        reset()
    