# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    csvreader.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/19 12:38:56 by mli               #+#    #+#              #
#    Updated: 2020/01/19 15:51:05 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#Not finished at all

class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        try:
            self.filename = str(filename)
            self.sep = str(sep)
            self.header = header
            self.skip_top = int(skip_top)
            self.skip_bottom = int(skip_bottom)
            self.fd = None
            self.data = None
        except ValueError:
            exit(print("Given arguments not good"))

    def __enter__(self):
        try:
            self.fd = open(self.filename, 'r')
        except:
            return (None)

        self.data = self.fd.readline().split(self.sep)
        for i in range(len(self.data)):
            self.data[i] = self.data[i].strip()
        return (self)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if (self != None):
            self.fd.close()

    def getdata(self):
        return (self.data)

    def getheader(self):
        return (self.header)

with CsvReader("good.csv") as test:
    pass

for data in test.getdata():
    print("|%s|" %data)

