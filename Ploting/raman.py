import os
import sys

# Definimos la Clase base "RamanSpectra" que debera contener información relacionada con la medicion
# TODO: Podemos añadir un mapeo de intensidades para caracterizar la superficie de medicion
# TODO: Añadir otros parametros de informacion para la muestra o espectro

class RamanSpectra(object):
    """
    RamanSpectra es un objeto que contiene los puntos de una medicion, es decir, 
    el objeto tiene un atributo correspondiente al eje x & otro para el eje y asi 
    como dos atributos mas para la información de la medición
    """

    def __init__(self, pathFile, upLevels = 0):
        _readFromLocation(pathFile,upLevels)
        return;
    
    def __str__(self):
        return 'raman_s at +++ ' + self.r_id;

    def __repr__(self):
        return 'raman_s at ... ' + self.r_id;
    
    def _readFromLocation(self, pathFile, upLevels):
        count = 0
        initialPath = os.getcwd().split('/')[1:]
        # TODO: Raise error when upLevels > treeDepth
        while count  < upLevels:
            initialPath.pop()
        docLoc = '/'+ '/'.join(initialPath)+pathFile
        with open(docLoc, 'r', encoding = 'unicode_escape') as tempfile:
                self.content = tempfile.read()
                self.info    = content.split('#Acquired')[1].split('\n')[0].replace("=\t",'')
                self.values  = content.split('#Acquired')[1].split('\n')[1:-1]
                self.spx=[]
                self.spy=[]
                for string_values in values:
                    try:
                        x = float(string_values.split('\t')[0])
                        y = float(string_values.split('\t')[1])
                    except:
                        print('Ocurrio un error al hacer la lectura de los archivos')
                    self.spx.append(x)
                    self.spy.append(y)
        return;
    
    
    def plot(self):
        fig, ax = plt.subplots()
        ax.plot(self.x, self.y)
        ax.set_title(self.info)



class RamanSpectraGroup(object):

    def __init__(self):
        # Un Grupo de espectros Raman será una lista de Objectos RamanSpectra
        # con los atributos de información (info) y datos de la medicion (data), inicialmente el atributo 
        # spectra es una lista vacía

        # TODO: Es posible añadir una opcion que distinga cuando un espectro ya ha sido añadido al grupo de
        # espectros Raman
        self.saved_memo = 0
        self.files = []
        self.ramanSpectra = []
        return;

    def getFilesFromFolder(self, folder):
        # NOTE: Este método no verifica si los archivos en el folder seleccionado ya se encuentran en self.spectra
        # el método construye una lista de archivos en el directorio seleccionado y llama al método
        # getDetailedSpectra con una lista que pasa a su argumento (self.files)
        folder = '/' + folder
        path   = os.getcwd()
        # TODO: Verificar si es posible discriminar con - if file in files - para evitar la duplicacion de archivos
        self.files  = [path + folder + '/' + f for f in os.listdir(path + folder)]
        self.getFiles(self.files)
        return;
    
    def getFilesFromPath(self, path):
        cwd = os.getcwd().split('/')[:-1]
        cwd = '/'.join(cwd)
        self.files  = [ cwd + path + '/' + f for f in os.listdir(cwd + path)]
        self.getFiles(self.files)
        return;

    def getFiles(self, targets):
        assert(type(targets)==list)
        for file in targets:
            with open(file, 'r', encoding = 'unicode_escape') as tempfile:
                content = tempfile.read()
                info    = content.split('#Acquired')[1].split('\n')[0].replace("=\t",'')
                values  = content.split('#Acquired')[1].split('\n')[1:-1]
                spx=[]
                spy=[]
                for string_values in values:
                    try:
                        x = float(string_values.split('\t')[0])
                        y = float(string_values.split('\t')[1])
                    except:
                        print('Ocurrio un error al hacer la lectura de los archivos')
                    spx.append(x)
                    spy.append(y)
                self.ramanSpectra.append(RamanSpectra((spx,spy), info ,file))
        return;