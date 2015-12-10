# encode UTF-8
import os

caminho = "E:/zipextraido/data/meta-data"
caminhoInst ="E:/zipextraido/data/meta-data"+"/Instituicao.txt"

def extract_name(name):   
    return name.split(".")[0]

def read_lines(filename):
    _file = open(os.path.join(caminho, filename), "rt")
    data = _file.read().split("\n")
    _file.close()
    return data

def read_metadata(filename):
    metadata = []
    for column in read_lines(filename):
        if column:
            values = column.split('\t')
            nome = values[0]
            tipo = values[1]
            desc = values[2]
            metadata.append((nome, tipo, desc))
            
    return metadata

def main():
    meta = {}
    for meta_data_file in os.listdir(caminho):
        table_name = extract_name(meta_data_file)
        meta[table_name] = read_metadata(meta_data_file)
    
    for key, val in meta.items():
        print("Entidade {}".format(key))    
        print("Attributes: ")
        for col in val:
            print(" {}: {}".format(col[1], col[0]))

if __name__ == "__main__":
    main()