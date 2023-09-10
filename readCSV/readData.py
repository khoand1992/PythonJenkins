import pandas as pd


def readTitanicData(csv_path):
    if csv_path is None or csv_path == '':
        print("Titanic path is empty")
    else:
        df = pd.read_csv(csv_path)
        print(df)
        print("Read titanic data successful")
