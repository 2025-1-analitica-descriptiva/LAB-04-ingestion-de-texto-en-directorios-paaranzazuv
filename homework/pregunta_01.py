# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import zipfile
import os

def pregunta_01():

    import os
import pandas as pd

carpetas     = ['train', 'test']
sentimientos = ['negative', 'positive', 'neutral']
base_dir     = os.path.join('files', 'input')

all_data = []

# Recorremos carpetas y sentimientos
for carpeta in carpetas:
    for sentimiento in sentimientos:
        path = os.path.join(base_dir, carpeta, sentimiento)
        if not os.path.isdir(path):
            continue

        for nombre in os.listdir(path):
            if nombre.lower().endswith('.txt'):
                file_path = os.path.join(path, nombre)
                with open(file_path, 'r', encoding='utf-8') as f:
                    phrase = f.read().strip()
                all_data.append({
                    'phrase':    phrase,
                    'target': sentimiento,
                    'subset':    carpeta
                                })

    # Creamos un único DataFrame
    df = pd.DataFrame(all_data)

    # Separamos en train y test
    train_df = df[df['subset'] == 'train'].reset_index(drop=True)
    test_df  = df[df['subset'] == 'test'].reset_index(drop=True)
    train_df.drop(columns='subset', inplace=True)
    test_df.drop(columns='subset', inplace=True)
    # Guardamos cada uno en su CSV
    os.makedirs('files/output', exist_ok=True)
    train_df.to_csv('files/output/train_dataset.csv', index=False)
    test_df.to_csv('files/output/test_dataset.csv',  index=False)

    print("Guardados: train_dataset.csv  y  test_dataset.csv")

    

print(pregunta_01())

"""
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
