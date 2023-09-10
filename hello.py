from hellopackage.helloworld import helloboy
from hellopackage.printStatus import print_status
from readCSV.readData import readTitanicData


if __name__ == "__main__":
    helloboy()
    print_status()
    data_path = 'readCSV/titanic.csv'
    readTitanicData(data_path)