import csv
import requests
import xml.etree.ElementTree as ET

def parseXML(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
  
    orderitems = []
  
    for item in root.findall('./AddOrder'):
        orders = {}
  
        for child in item:
            orders[child.tag] = child.text.encode('utf8')
        orderitems.append(orders)

    for item in root.findall('./AddOrder'):
        orders = {}
  
        for child in item:
            orders[child.tag] = child.text.encode('utf8')

        orderitems.append(orders)
      
    return orderitems
  
  
def savetoCSV(newsitems, filename):
    fields = ['book', 'operation', 'price', 'volume', 'orderId']
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(newsitems)
  
      
def main():
    orderitems = parseXML('orders.xml')
  
    savetoCSV(orderitems, 'orders.csv')
      
      
if __name__ == "__main__":
  
    # calling main function
    main()