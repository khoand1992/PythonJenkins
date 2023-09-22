from hellopackage.helloworld import helloboy
from hellopackage.printStatus import print_status
from readCSV.readData import readTitanicData
from APIEndpoint.JsonPlaceHolder import getResponseJSON
# from SendEmail.RealPython import sendEmail


if __name__ == "__main__":
    helloboy()
    print_status()
    data_path = 'readCSV/titanic.csv'
    readTitanicData(data_path)
    df = getResponseJSON('https://jsonplaceholder.typicode.com/posts/1')
    print(df)
    # sendEmail()