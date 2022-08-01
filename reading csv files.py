import csv
with open(r'C:\Users\Nitin\Downloads\airtravel.csv','r') as f:
      reader = csv.reader(f)
      print(reader)
      next(reader)
      year_1958 = dict()
      for row in reader:
          #print(row[1])
          year_1958[row[0]] = row[1]
      #print(year_1958)

      max_1958 = max(year_1958.values())
      #print(max_1958)

      for k , v in year_1958.items():
          if max_1958 == v:
              print(f'Busiest month in 1958:{k}, Flights:{v.strip()}')

     # sometimes we have white spaces in csv files
      # in order to remove the whitespaces we can use the strip function
     # strip is a string function and k and v are strings








      def getList1(year_1958):
          return list(year_1958.keys())
      #Typecasting to list

      ## Python program to get  dictionary keys as list
      def getList(year_1958):
        keys_list = []
        for key in year_1958.keys():
           keys_list.append(key)
        return keys_list

      def getList2(year_1958):
          return [*year_1958]

      #Unpacking with *works with any object
      # that is iterable and, since dictionaries return their keys when iterated through,
      # you can easily create a list by using it within a list literal.

      #Approach  # 1 : Using dict.keys() [For Python 2.x]


      def getList3(year_1958):
          return year_1958.keys()


      #a = year_1958.keys()
      print(getList3(year_1958))

      b = year_1958.keys()
      print(b)
      #a = int(year_1958[key[0]])
      #for key in year_1958:
      #    if year_1958[key] > a:
      #        a = year_1958[key]
      #print(a)


# each row is a list of strings

