from typing import Iterator


class File:
    def __init__(self, file_name:str):
        self.file_name = file_name

    def readlines(self) -> Iterator[str]:
        def clean(line:str) -> str:
            return line.replace('\n', '').strip()
        with open(self.file_name, 'r') as f:
            return (clean(line) for line in f.readlines())
        

class FileM3u(File):
    """Lectura y Escritura de archivos .m3u [Playlist]"""
    def __init__(self, file_name:str):
        super().__init__(file_name)

    def read(self) -> list[dict]:
        """lectura del archivo .m3u, retorna [{seconds, title, url, *image}, {...}]"""
        def get_info(line:str, pre:str='#EXTINF:') -> dict:
            if line.startswith(pre):
                seconds, title = line.strip(pre).split(',')
                return int(seconds), title.strip()
            
        def get_image(line:str, pre:str='#EXTIMG:') -> dict:
            if line.startswith(pre):
                return line.strip(pre)
            
        def get_items(lines:Iterator[str]) -> list[dict]:
            items = list()
            data = dict()
            for line in lines:
                if line.startswith('#EXT'):
                    tag, _ = line.split(':', 1)
                    match tag:
                        case '#EXTINF':
                            seconds, title = get_info(line)
                            data.update(seconds=seconds, title=title)
                        case '#EXTIMG':
                            data.update(image=get_image(line))
                else:
                    data.update(url=line)
                    items.append(data)
                    data = dict()
            return items

        lines = self.readlines()
        header = next(lines)
        playlist = []
        if header == '#EXTM3U':
            playlist:list = get_items(lines)
        return playlist

    def write(self, items:list[dict]):
        "escribir archivo .m3u items=[{seconds, title, url, *image}, {...}]"
        text = '#EXTM3U\n'
        for item in items:
            template = [
                f'#EXTINF:{item.get("seconds", 0)},{item.get("title")}',
                f'#EXTIMG:{item.get("image", '')}',
                f'{item.get("url")}\n'
            ]
            text += '\n'.join(template)
        with open(self.file_name, 'w') as f:
            f.write(text)


if __name__ == "__main__":
    from pprint import pprint
    # pruebas m3u
    # path_m3u = 'ejemplo.m3u'
    # m3u = FileM3u(file_name=path_m3u)

    # # LECTURA
    # pprint(m3u.read())

    # ESCRITURA
    # data = [
    #     dict(seconds=0, title='mi titulo', url='www.goggle.com', image='ruta de image'),
    #     dict(seconds=0, title='mi titulo 1', url='www.uno.com', image='ruta de image 1')
    # ]
    # m3u.write(data)