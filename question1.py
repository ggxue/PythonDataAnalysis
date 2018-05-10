import csv

with open('strInput.csv', 'r') as csv_file:
    csv_reader=csv.DictReader(csv_file) #read from the strInput csv file

    with open('strTransactions.csv', 'w', newline='') as new_file:
        fieldnames = ['Date', 'Time', 'Transaction No.', 'Status', 'Store No.', 'Location Code', 'POS Terminal No.',
                      'Receipt No.', 'Cashier Staff ID', 'Sales Staff ID','Line Net PMount',
                      'Line Discount PMount','Line GST PMount']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames) #DictWriter function allows to manipulate content using Dictionary datas tructure
        csv_writer.writeheader()    #write coloumn entry to strTransactions.csv

        for line in csv_reader:
                csv_writer.writerow({'Date': line['Date'], 'Time': line['Time'], 'Transaction No.': line['Transaction No.'],
                                     'Status': line['Status'], 'Store No.': line['Store No.'],
                                     'Location Code': line['Location Code'],
                                     'POS Terminal No.': line['POS Terminal No.'], 'Receipt No.': line['Receipt No.'],
                                     'Line Net PMount':line['Line Net PMount'],'Line Discount PMount':line['Line Discount PMount'],
                                     'Line GST PMount':line['Line GST PMount'],'Cashier Staff ID': line['Cashier Staff ID'],
                                     'Sales Staff ID': line['Sales Staff ID']}) #write content from strInput to according entry in strTransactions.csv use Dictionary data structure

with open('strInput.csv', 'r') as csv_file:   #read from the strInput csv file
    csv_reader = csv.DictReader(csv_file)

    with open('strLineItems.csv', 'w',newline='') as newfile:
        fieldnames=['Transaction No.','Item ID','Item Description','Item Quantity','Item Unit Price']
        csv_writer=csv.DictWriter(newfile,fieldnames=fieldnames) #DictWriter function allows to manipulate content using Dictionary datas tructure
        csv_writer.writeheader()    #write coloumn entry to strLineItems.csv

        for line in csv_reader:
                csv_writer.writerow({'Transaction No.': line['Transaction No.'],'Item ID':line['Item ID'],
                                     'Item Description':line['Item Description'],
                                     'Item Quantity':line['Item Quantity'],
                                     'Item Unit Price':line['Item Unit Price']})   #write content from strInput to according entry in strLineItems.csv use Dictionary data structure