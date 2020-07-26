import csv

from table import table


with open('camion.csv', 'rt') as f:
    cont = csv.reader(f)
    headers = next(cont)
    data = []
    for line in cont:
         tupla = (line[0], int(line[1]), float(line[2]))
         data.append(tupla)


tabla = table(len(headers))
tabla.setMaxWidth(20)
tabla.setHeaders(headers)
tabla.setBody(data)
tabla.print_table()


