import configparser

config = configparser.ConfigParser(allow_no_value=True)
config.read('config.ini')

def data_inicial():
    
    station = config.get("DATA","station")
    stations = eval(station)
    return stations
    
def files():
    
    file = config.get("FILES","origin")
    files = eval(file)
    return files
    
def log():
    
    folder = config.get("LOG","folder")
    return folder
