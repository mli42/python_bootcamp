# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    csvreader.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/19 12:38:56 by mli               #+#    #+#              #
#    Updated: 2021/12/25 22:09:26 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import csv

class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        if not (isinstance(filename, str) and isinstance(sep, str)
        and isinstance(header, bool) and isinstance(skip_top, int)
        and isinstance(skip_bottom, int)):
            exit("Given arguments not good")
        self.filename = filename
        self.sep = sep
        self.has_header = header
        self.skip_top = skip_top + header
        self.skip_bottom = skip_bottom
        self.fd = None
        self.data = []
        self.header = None

    def __enter__(self):
        try:
            self.fd = open(self.filename, 'r')
            csv_reader = csv.reader(self.fd, delimiter=self.sep)
        except:
            return (None)

        expected_len = None
        for i, row in enumerate(csv_reader):
            #row = [word.strip().strip("\"") for word in row]
            if expected_len is None:
                expected_len = len(row)
            elif expected_len != len(row):
                return None

            if any([(len(element) == 0) for element in row]):
                return None

            if i == 0 and self.has_header is True:
                self.header = row
            elif i >= self.skip_top and (self.skip_bottom == 0 or i < self.skip_bottom):
                self.data.append(row)
        return (self)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if hasattr(self, 'fd') and self.fd is not None:
            self.fd.close()

    def getdata(self):
        return (self.data)

    def getheader(self):
        return (self.header)

if __name__ == "__main__":
    def testReader(filename, sep, header, skip_top, skip_bottom):
        with CsvReader(filename, sep, header, skip_top, skip_bottom) as reader:
            if reader == None:
                print("File is corrupted or missing")
            else:
                print('Header:', reader.getheader(), end = "\n")
                print('Data  :', reader.getdata(), end = "\n\n")
    testReader('good.csv', ',', False, 18, 0)
    testReader('good.csv', ',', True, 17, 0)
    testReader('bad.csv', ',', False, 18, 0)
    testReader('bad.csv', ',', True, 17, 0)
    testReader('mdr.csv', ',', False, 18, 0)
    testReader('mdr.csv', ',', True, 17, 0)
