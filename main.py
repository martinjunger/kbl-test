import csv

print("Hello world from python")

csvlt = '\n'
csvdel = ','
csvquo = '"'
with open('in/tables/bitcoin-price.csv', mode='rt', encoding='utf-8') as in_file, \
        open('out/tables/odd.csv', mode='wt', encoding='utf-8') as odd_file, \
        open('out/tables/even.csv', mode='wt', encoding='utf-8') as even_file:
    lazy_lines = (line.replace('\0', '') for line in in_file)
    reader = csv.DictReader(lazy_lines, lineterminator=csvlt, delimiter=csvdel,
                            quotechar=csvquo)

    even_writer = csv.DictWriter(odd_file, fieldnames=reader.fieldnames,
                                 lineterminator=csvlt, delimiter=csvdel,
                                 quotechar=csvquo)
    even_writer.writeheader()

    odd_writer = csv.DictWriter(even_file, fieldnames=reader.fieldnames,
                                lineterminator=csvlt, delimiter=csvdel,
                                quotechar=csvquo)
    odd_writer.writeheader()
    i = 0
    for row in reader:
        if i % 2 == 0:
            even_writer.writerow(row)
        else:
            odd_writer.writerow(row)
        i = i + 1