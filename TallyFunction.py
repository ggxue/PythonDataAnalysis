import pandas

def Tally(Transaction_No): #Pass a sepecific Transaction_No which want to check as argument

    csv_file=pandas.read_csv('strLineItems.csv',delimiter=',')
    Item_price=csv_file['Item Unit Price'].groupby(csv_file['Transaction No.']) #extract Item Unit Price list and group by Transaction No. from strLineItems.csv using pandas module
    Item_price_sum=dict(list(Item_price))[Transaction_No].dropna().sum() #get the sum of all the Items price in the sepecific Transaction No. group
    print('price_list_sum is : ',Item_price_sum) #print the sum of all the Items price in the sepecific Transaction No. group

    csv_file2=pandas.read_csv('strTransactions.csv',delimiter=',')
    Line_Net_price=csv_file2['Line Net PMount'].groupby(csv_file2['Transaction No.']) #extract Line Net PMount and group by Transaction No. from strTransactions.csv using pandas module
    Line_Net_price_sum=dict(list(Line_Net_price))[Transaction_No].dropna().sum() #get the sum of Line Net PMount in the sepecific Transaction No. group
    print('price_transaction_sum is : ',Line_Net_price_sum) #print the sum of Line Net PMount in the sepecific Transaction No. group

    if(Item_price_sum==Line_Net_price_sum): print('Line Items Total and sum of each Item Price in Transaction No: ',Transaction_No,' is Equal ')
    else: print('Line Items Total and sum of each Item Price in Transaction No ',Transaction_No,' is Not equal')

Tally(61901557)