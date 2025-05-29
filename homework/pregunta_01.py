# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import os
import zipfile
import pandas as pd

def pregunta_01():
    """
    Descomprime 'files/input.zip' si existe y no se ha extraido.
    Luego recorre los directorios 'train' y 'test' y sus subcarpetas
    de sentimiento ('negative','positive','neutral'), lee todos los
    archivos .txt, y genera dos CSV: 'train_dataset.csv' y 'test_dataset.csv'
    en 'files/output', con columnas 'phrase' y 'target'.
    """
    # Descomprimir input.zip si es necesario
    zip_path = os.path.join('files', 'input.zip')
    extract_folder = os.path.join('files', 'input')
    if os.path.exists(zip_path) and not os.path.isdir(extract_folder):
        with zipfile.ZipFile(zip_path, 'r') as z:
            z.extractall('files')

    carpetas = ['train', 'test']
    sentimientos = ['negative', 'positive', 'neutral']
    base_dir = os.path.join('files', 'input')
    all_data = []

    for carpeta in carpetas:
        for sentimiento in sentimientos:
            folder_path = os.path.join(base_dir, carpeta, sentimiento)
            if not os.path.isdir(folder_path):
                continue
            for filename in os.listdir(folder_path):
                if filename.lower().endswith('.txt'):
                    file_path = os.path.join(folder_path, filename)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        phrase = f.read().strip()
                    all_data.append({
                        'phrase': phrase,
                        'target': sentimiento,
                        'subset': carpeta
                    })

    df = pd.DataFrame(all_data)

    # Separar y eliminar columna 'subset'
    train_df = df[df['subset'] == 'train']
    test_df = df[df['subset'] == 'test']

    # Crear carpeta output
    output_folder = os.path.join('files', 'output')
    os.makedirs(output_folder, exist_ok=True)

    # Guardar CSVs
    train_df.to_csv(os.path.join(output_folder, 'train_dataset.csv'), index=False)
    test_df.to_csv(os.path.join(output_folder, 'test_dataset.csv'), index=False)

    return df

    

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
