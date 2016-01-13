import csv
import mysql.connector


host = "localhost"
port = "3307"
username = "root"
password = " "
db = "northwind"

class Employee():


    def __init__(self, row):
        self.employeeid=row['EmployeeID']
        self.lastname=row['LastName']
        self.firstname=row['FirstName']
        self.title=row['Title']
        self.titleofcourtesy=row['TitleOfCourtesy']
        self.birthdate=row['BirthDate']
        self.hiredate=row['HireDate']
        self.address=row['Address']
        self.city=row['City']
        self.region=row['Region']
        self.postalcode=row['PostalCode']
        self.country=row['Country']
        self.homephone=row['HomePhone']
        self.extension=row['Extension']
        self.photo=row['Photo']
        self.notes=row['Notes']
        self.reportsto=row['ReportsTo']
        self.photopath=row['PhotoPath']
        self.salary=row['Salary']

    @staticmethod
    def parse(rownumber):
        count = 1
        with open('employees.csv', 'r') as f:
            reader = csv.DictReader(f,delimiter = ";")
            for row in reader:
                count += 1
                if count == rownumber:
                    return Employee(row)

    @staticmethod
    def persist():
        pass


class Customers():


    def __init__(self, row):
        self.cutomerid=row['CustomerID']
        self.companyname=row['CompanyName']
        self.contactname=row['ContactName']
        self.contacttitle=row['ContactTitle']
        self.address=row['Address']
        self.city=row['City']
        self.region=row['Region']
        self.postalcode=row['PostalCode']
        self.country=row['Country']
        self.phone=row['Phone']
        self.fax=['Fax']

    @staticmethod
    def parse(rownumber):
        count = 1
        with open('customers.csv', 'r') as f:
            reader = csv.DictReader(f,delimiter = ";")
            for row in reader:
                count += 1
                if count == rownumber:
                    return Customers(row)



class Order_details():


    def __init__(self,row):
        self.orderid=row['OrderID']
        self.product=row['Product']
        self.unitprice=row['UnitPrice']
        self.quantity=row['Quantity']
        self.discount=row['Discount']

    @staticmethod
    def parse(rownumber):
        count = 1
        with open('order_datails.csv', 'r') as f:
            reader = csv.DictReader(f,delimiter = ";")
            for row in reader:
                count += 1
                if count == rownumber:
                    return Order_details(row)


class Orders():

    def __init__(self,row):
        self.orderid=row['OrderID']
        self.customerid=row['CustomeriD']
        self.employeeid=row['EmployeeID']
        self.contacttitle=row['ContactTitle']
        self.orderdate=row['OrderDate']
        self.requireddate=row['RequiredDate']
        self.shippeddate=row['ShippedDate']
        self.shipvia=row['ShipVia']
        self.freight=row['Freight']
        self.shipname=row['ShipName']
        self.shipaddress=row['ShipAddress']
        self.shipcity=row['ShipCity']
        self.shipregion=row['ShipRegion']
        self.shippostalcode=row['ShipPostalCode']
        self.shipcountry=row['ShipCountry']


    @staticmethod
    def parse(rownumber):
        count = 1
        with open('orders.csv', 'r') as f:
            reader = csv.DictReader(f,delimiter = ";")
            for row in reader:
                count += 1
                if count == rownumber:
                    return Orders(row)