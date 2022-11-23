from argparse import ArgumentParser

if __name__ == "__main__":
    # command parser
    argParser = ArgumentParser()
    argParser.add_argument("filename", type=str)
    args = argParser.parse_args()
    
    # cek
    '''
    if ():
        print("Accepted")
    else:
        print("Syntax Error")
    '''