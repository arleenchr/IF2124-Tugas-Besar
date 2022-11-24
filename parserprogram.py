from argparse import ArgumentParser
from convert_to_cfg import file_to_cfg
from convert_to_cnf import cfg_to_cnf
from cyk import cyk
from lexer import tokenToStr

if __name__ == "__main__":
    # command parser
    argParser = ArgumentParser()
    argParser.add_argument("filename", type=str)
    args = argParser.parse_args()
    
    # cek
    if (cyk(cfg_to_cnf(file_to_cfg("grammar.txt")),tokenToStr(args.filename))):
        print("Accepted")
    else:
        print("Syntax Error")
    