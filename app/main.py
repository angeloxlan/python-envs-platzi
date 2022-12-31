import csv
import matplotlib.pyplot as plt
import re

def read_csv(path):
    with open(path) as filecsv:
        reader = csv.reader(filecsv, delimiter=',')
        header = next(reader)

        data = []
        for row in reader:
            country = dict(zip(header, row))
            data.append(country)

        return data


def generate_bar_chart(labels, values, name):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    # plt.show()
    plt.savefig(f'./imgs/{name}.png')
    plt.close()


def get_data_by_country(country, data):
    data = filter(lambda c: c['Country/Territory'] == country, data)
    return list(data)


def get_population(country):
    data = dict()
    for key, value in country.items():
        # if 'Population' in key and key != 'World Population Percentage':
        if re.match(r'[0-9]+ Population', key):
            year, _ = key.split(' ')
            data[year] = int(value)

    return data


def run():
    data = read_csv('world_population.csv')
    country = input('Type a Country => ')

    result = get_data_by_country(country, data)
    if len(result) > 0:
        country = result[0]
        population = get_population(country)

        labels = population.keys()
        values = population.values()
        generate_bar_chart(labels, values, country['Country/Territory'])
    else:
        print('No se encontró el país que indicaste.')


if __name__ == '__main__':
    run()
