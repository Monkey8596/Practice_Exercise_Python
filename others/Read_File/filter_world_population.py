import csv
import ej_charts

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

    new_data = list(filter(lambda x:x['Continent']== 'South America', data ))
    South_america = list(map(lambda x:x['Country/Territory'], new_data ))
    

    countries = list(map(lambda x:x['Country/Territory'], new_data )) # All Countries 

    percentages = list(map(lambda x:x['World Population Percentage'], new_data )) # Population Percentage

    ej_charts.generate_pie_chart(countries,percentages)


