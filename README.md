# Copy-files

##### Código Python para cópia de arquivos

##### Para o funcionamento deste código, o Dev precisa instalar pysimplegui

```terminal

pip install pysimplegui
//or
//pip3 install pysimplegui
//verificar versão de seu pip
```

##### O comando shutil.copy2 reduziu parte do código

```python
shutil.copy2(file, station)
```

#### É necessário editar o arquivo config.ini e inserir informações nas variáveis station, folder e origin
###### station = esta lista deve conter o caminho em que o arquivo deverá ser salvo(destino)
###### folder = deve conter o caminho que os logs de execução ficará salvo
###### origin = esta lista deve conter o caminho do arquivo que você deseja gerar cópia(poderá ter mais de uma origem)

1. O arquivo principal é o main.py, para o programa ser executado sem a presença do terminal, salvar este arquivo como main.pyw

###### Links relacionados:
[PYSIMPLEGUI](https://pysimplegui.readthedocs.io/en/latest/#pysimplegui-users-manual)
