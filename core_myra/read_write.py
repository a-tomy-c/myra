import json
import toml
import yaml


class _Base:
    """clase base para leer y escribir archivos"""
    def __init__(self, filename:str):
        """filename: ruta del archivo (str)"""
        self.filename = filename

    def read(self) -> dict:
        ...
    
    def get(self, key:str) -> str|int:
        """retorna el valor en `key`"""
        if not hasattr(self, 'data'): self.read()
        return self.data.get(key, None)
    

class MyJson(_Base):
    def __init__(self, filename:str):
        super().__init__(filename)

    def write(self, data:dict):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=2)
    
    def read(self) -> dict:
        with open(self.filename, 'r') as file:
            self.data = json.load(file)
            return self.data
        

class MyToml(_Base):
    def __init__(self, filename:str):
        super().__init__(filename)

    def write(self, data:dict):
        with open(self.filename, 'w') as file:
            toml.dump(data, file)
    
    def read(self) -> dict:
        with open(self.filename, 'r') as file:
            self.data = toml.load(file)
            return self.data
        

class MyYaml(_Base):
    def __init__(self, filename:str):
        super().__init__(filename)

    def write(self, data:dict):
        with open(self.filename, 'w', encoding='utf-8') as file:
            yaml.dump(data, file, sort_keys=False, default_flow_style=False)
    
    def read(self) -> dict:
        with open(self.filename, 'r', encoding='utf-8') as file:
            self.data = yaml.safe_load(file)
            return self.data


class ReadWrite:
    def __init__(self, file_path:str, type:int=0):
        "type = 0:yaml, 1:toml, 2:json, x:json"
        match type:
            case 0:self.file = MyYaml(file_path)
            case 1:self.file = MyToml(file_path)
            case 2:self.file = MyJson(file_path)
            case _:self.file = MyJson(file_path)
        

if __name__ == "__main__":
    nuevo_server_config = {
        "aplicacion": "MiApp",
        "version": "1.2.0",
        "parametros": {
            "log_level": "DEBUG",
            "max_conn": 100
        },
        "usuarios_activos": ["user1", "user2"]
    }

    # mj = MyJson(filename='adicional/mi_archivo.json')
    # mj.write(nuevo_server_config)

    # mt = MyToml(filename='adicional/mi_archivo.toml')
    # mt.write(nuevo_server_config)
    # mt.read()
    # print(mt.get('version'))

    # my = MyYaml(filename='adicional/mi_archivo.yml')
    # my.write(nuevo_server_config)
    # print(my.get('parametros'))

    file = 'adicional/mi_archivo.yml'
    # mf = MyFile(file_name=file)
    # print(mf.yaml.get('version'))

    rw = ReadWrite(file)
    res = rw.file.get('version')
    print(res)
