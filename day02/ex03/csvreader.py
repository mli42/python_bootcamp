# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    csvreader.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/19 12:38:56 by mli               #+#    #+#              #
#    Updated: 2020/11/21 21:11:15 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import csv

class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        try:
            if not isinstance(filename, str) or not isinstance(sep, str) \
            or not isinstance(header, bool) or not isinstance(skip_top, int) \
            or not isinstance(skip_bottom, int):
                raise ValueError
            self.filename = filename
            self.sep = sep
            self.header_b = header
            self.skip_top = skip_top
            self.skip_bottom = skip_bottom
            self.fd = None
            self.data = []
            self.header = None
        except ValueError:
            exit(print("Given arguments not good"))

    def __enter__(self):
        try:
            self.fd = open(self.filename, 'r')
            csv_reader = csv.reader(self.fd, delimiter=self.sep)
        except:
            return (None)

        for i, row in enumerate(csv_reader):
            #row = [word.strip().strip("\"") for word in row]
            for element in row:
                if len(element) == 0:
                    return None
            if i == 0 and self.header_b is True:
                self.header = row
            elif i >= self.skip_top and (self.skip_bottom == 0 or i < self.skip_bottom):
                self.data.append(row)
        return (self)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.fd is not None:
            self.fd.close()

    def getdata(self):
        return (self.data)

    def getheader(self):
        return (self.header)

if __name__ == "__main__":
    with CsvReader("good.csv", header=True, skip_top=15) as file:
        if file is None:
            print("File not found or is corrupted")
            exit()
        print("Header:")
        print("|%s|" %file.getheader())
        print("Data:")
        for data in file.getdata():
            print("|%s|" %data)
