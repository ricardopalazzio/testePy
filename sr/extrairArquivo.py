# coding: utf-8
'''
Created on 8 de dez de 2015

@author: ricar
'''

import sys
import zipfile
import os

def main(path):
    if not os.path.exists(path):
        print("Arquivo {} não existe".format(path))
        sys.exit(-1)
    else:
        zfile = zipfile.ZipFile(path)
        zfile.extractall(path="E:/zipextraido")
        print("Arquivos extraídos")
        
if __name__ == '__main__':
    main(sys.argv[1])