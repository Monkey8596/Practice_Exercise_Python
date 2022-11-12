import csv

def read_csv(path):
    with open(path,'r') as csvfile:
        reader =  csv.reader(csvfile, delimiter=',')

        header = next(reader)
        data = []


        for row in reader:

            iterable = zip(header,row)
            country_dict = {key: value for key,value in iterable }
            data.append(country_dict)

        return data 



if __name__ == '__main__':
    data = read_csv('./Data.csv')
    
    Co = [element for element in data if element["Country/Territory"] == 'Colombia']
    print(Co)

    # dato2 = list(filter(lambda item: item['Country/Territory'] == 'Colombia', data))
    # print(dato2)

    # for element in data:
    #     if element["Country/Territory"] == 'Colombia':
    #         print(element)

    
