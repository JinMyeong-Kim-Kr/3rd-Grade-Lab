import datetime
from decimal import Decimal
import sys, csv, json
from xml.etree.ElementTree import Element, ElementTree, SubElement
import pymysql
from PyQt5.QtWidgets import *

class MainWindow(QWidget):          
    def __init__(self):
        super().__init__()
        self.query = DB_Queries()
        self.setupUI()
        self.initComboBoxItem()
        self.initTable()
        self.lastChoose = "customer"
        
    def setupUI(self):
        # 윈도우 설정
        self.setWindowTitle("주문 검색")
        self.setGeometry(0, 0, 600, 400)

        # 주문 검색 label
        self.titleLabel = QLabel("주문 검색")
        
        # 고객 Label
        self.customerLabel = QLabel("고객")
        # 고객 RadioButton
        self.customerQBox = QComboBox(self)
        self.customerQBox.activated.connect(lambda: self.customerCBoxAct())
        # 국가 Label
        self.countryLabel = QLabel("국가")
        # 국가 RadioButton
        self.countryQBox = QComboBox(self)

        self.countryQBox.activated.connect(lambda: self.countryCBoxAct())
        # 도시 Label
        self.cityLabel = QLabel("도시")
        # 도시 RadioButton
        self.cityQBox = QComboBox(self)
        self.cityQBox.activated.connect(lambda: self.cityCBoxAct())
        # 주문 결과 label
        self.numOfResultLabel = QLabel("검색된 주문의 개수:")
        # 주문 결과 출력 label
        self.resultLabel = QLabel("0") 
        # 검색 button
        self.searchButton = QPushButton("검색")
        self.searchButton.clicked.connect(lambda: self.searchBtnClicked())
        
        # 초기화 button
        self.initButton = QPushButton("초기화")
        self.initButton.clicked.connect(lambda: self.initBtnClicked())
        # 결과 출력 tablewidget
        self.resultTableWidget = QTableWidget(self)
        # 테이블의 항목을 더블 클릭시 주문 상세 화면으로 이동
        self.resultTableWidget.doubleClicked.connect(lambda: self.tableDoubleClicked())
                
        # 고객, 국가, 도시 입력 위젯을 포함하는 레이아웃
        searchLayout = QHBoxLayout()
        searchLayout.addWidget(self.customerLabel)
        searchLayout.addWidget(self.customerQBox)
        searchLayout.addWidget(self.countryLabel)
        searchLayout.addWidget(self.countryQBox)
        searchLayout.addWidget(self.cityLabel)
        searchLayout.addWidget(self.cityQBox)
        
        # 주문 결과 label과 버튼 widget을 포함하는 레이아웃 
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.numOfResultLabel)
        buttonLayout.addWidget(self.resultLabel)
        buttonLayout.addWidget(self.initButton)
        buttonLayout.addWidget(self.searchButton)
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.titleLabel)
        mainLayout.addLayout(searchLayout)
        mainLayout.addLayout(buttonLayout)
        mainLayout.addWidget(self.resultTableWidget)
        self.setLayout(mainLayout)
        
    def initComboBoxItem(self):
        self.customerItem = self.query.searchCustomer()
        self.countryItem = self.query.searchCountry()
        self.cityItem = self.query.searchCity()
        self.customerQBox.addItem("ALL")
        for item in self.customerItem:
            for _, name in item.items():
                self.customerQBox.addItem(name)
        self.countryQBox.addItem("ALL")
        for item in self.countryItem:
            for _, name in item.items():
                self.countryQBox.addItem(name)
        self.cityQBox.addItem("ALL")
        for item in self.cityItem:
            for _, name in item.items():
                self.cityQBox.addItem(name)
    
    def initTable(self):
        self.data = self.query.searchALL()
        self.displayContent(self.data)
    
    def initBtnClicked(self):
        self.clearTable()
        self.customerQBox.clear()
        self.countryQBox.clear()
        self.cityQBox.clear()
        self.initComboBoxItem()
        self.lastChoose = "customer"
        
    def clearTable(self):
        self.resultTableWidget.clearContents()
        self.resultLabel.setText("0")
        self.resultTableWidget.setRowCount(0)
        self.resultTableWidget.setColumnCount(0)
        
    def customerCBoxAct(self):
        self.lastChoose = "customer"
    def countryCBoxAct(self):
        self.lastChoose = "country"
        # City의 QComboBox 항목 수정
        self.cityQBox.clear()
        self.cityQBox.addItem("ALL")
        country = self.countryQBox.currentText()
        if country == "ALL":
            self.data = self.query.searchCity()
            for item in self.data:
                for _, name in item.items():
                    self.cityQBox.addItem(name)
        else:
            self.cityItem = self.query.selectCityInCountry(country)
            for item in self.cityItem:
                for _, name in item.items():
                    self.cityQBox.addItem(name)
        
    def cityCBoxAct(self):
        self.lastChoose = "city"
        
    def searchBtnClicked(self):
        if self.lastChoose == "customer":
            keyword = self.customerQBox.currentText()
            if keyword == "ALL":
                self.data = self.query.searchALL()
                self.displayContent(self.data)
                return
            else:
                self.data = self.query.selectCustomer(keyword)
                if len(self.data) == 0 : return self.clearTable()
                self.displayContent(self.data)
        elif self.lastChoose == "country":
            keyword = self.countryQBox.currentText()
            if keyword == "ALL":
                self.data = self.query.searchALL()
                self.displayContent(self.data)
            else:
                self.data = self.query.selectCountry(keyword)
                if len(self.data) == 0 : return self.clearTable()
                self.displayContent(self.data)
        elif self.lastChoose == "city":
            keyword = self.cityQBox.currentText()
            if keyword == "ALL":
                self.data = self.query.searchALL()
                self.displayContent(self.data)
            else:
                self.data = self.query.selectCity(keyword)
                if len(self.data) == 0 : return self.clearTable()
                self.displayContent(self.data)
        
    def displayContent(self, data):
        self.resultTableWidget.clearContents()
        self.resultTableWidget.setRowCount(len(data))
        self.resultTableWidget.setColumnCount(len(data[0]))
        self.resultLabel.setText(str(len(data)))
        
        columnNames = list(data[0].keys())                     
        self.resultTableWidget.setHorizontalHeaderLabels(columnNames)
        self.resultTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        for rowIDX, item in enumerate(data):
            for columnIDX, (k, v) in enumerate(item.items()):
                if v == None:     
                    continue 
                elif isinstance(v, datetime.date):
                    item = QTableWidgetItem(v.strftime('%Y-%m-%d')) 
                else:
                    item = QTableWidgetItem(str(v)) 
                self.resultTableWidget.setItem(rowIDX, columnIDX, item)

        self.resultTableWidget.resizeColumnsToContents()
        self.resultTableWidget.resizeRowsToContents() 
    
    def tableDoubleClicked(self):
        row = self.resultTableWidget.currentIndex().row()
        orderId = self.data[row]["orderNo"]
        self.detailWindow = DetailWindow(orderId)
        self.detailWindow.show()
        
    
###########################################

class DetailWindow(QWidget):
    def __init__(self, orderNo):
        super().__init__()
        self.setupUI()
        self.orderNo = orderNo
        self.query = DB_Queries()
        self.displayDetail(self.orderNo)
        
    def setupUI(self):
        # 윈도우 설정
        self.setWindowTitle("주문 상세 내역")
        self.setGeometry(0, 0, 600, 400)
        # 주문 상세 내역 label
        self.titleLabel = QLabel("주문 상세 내역")
        # 주문 번호 label
        self.orderNumLabel = QLabel("주문 번호")
        # 주문 번호 출력 label
        self.printOrderNumLabel = QLabel("0")
        # 상품 개수 label
        self.numOfProductLabel = QLabel("상품 개수")
        # 상품 개수 출력 label
        self.printNumOfProductLabel = QLabel("0")
        # 주문 금액 label
        self.priceOfOrderLabel = QLabel("주문 금액")
        # 주문 금액 출력 label
        self.printPriceOfOrderLabel = QLabel("0")
        # 상품 리스트 출력 table widget
        self.productListTable = QTableWidget()
        # 파일 출력 label
        self.printFileLabel = QLabel("파일 출력")
        # CSV radio button
        self.CSVradioButton = QRadioButton("CSV")
        self.CSVradioButton.setChecked(True) # default
        # JSON radio button
        self.JSONradioButton = QRadioButton("JSON")
        # XML radio button
        self.XMLradioButton = QRadioButton("XML")
        # 저장 button
        self.saveButton = QPushButton("저장")
        self.saveButton.clicked.connect(self.saveBtnClicked)
        
        # 주문 번호, 상품 개수, 주문 금액을 포함하는 layout
        self.resultLayout = QHBoxLayout()
        self.resultLayout.addWidget(self.orderNumLabel)
        self.resultLayout.addWidget(self.printOrderNumLabel)
        self.resultLayout.addWidget(self.numOfProductLabel)
        self.resultLayout.addWidget(self.printNumOfProductLabel)
        self.resultLayout.addWidget(self.priceOfOrderLabel)
        self.resultLayout.addWidget(self.printPriceOfOrderLabel)
        # radio, 저장 button을 포함하는 layout
        self.radioLayout = QHBoxLayout()
        self.radioLayout.addWidget(self.CSVradioButton)
        self.radioLayout.addWidget(self.JSONradioButton)
        self.radioLayout.addWidget(self.XMLradioButton)
        self.radioLayout.addWidget(self.saveButton)
        # main layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.titleLabel)
        mainLayout.addLayout(self.resultLayout)
        mainLayout.addWidget(self.productListTable)
        mainLayout.addWidget(self.printFileLabel)
        mainLayout.addLayout(self.radioLayout)
        
        self.setLayout(mainLayout)

    # displayDetail @self.productListTable을 구성하는 함수
    def displayDetail(self, orderNo):
        self.printOrderNumLabel.setText(str(orderNo))
        self.data = self.query.showDetail(orderNo)
        self.productListTable.setRowCount(len(self.data))
        self.productListTable.setColumnCount(len(self.data[0]) + 1)
        self.printNumOfProductLabel.setText(str(len(self.data)))
        totalOrderPrice = 0
        
        columnNames = list(self.data[0].keys())                     
        columnNames.append("상품주문액")
        self.productListTable.setHorizontalHeaderLabels(columnNames)
        self.productListTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for rowIDX, item in enumerate(self.data):
            quantity = item.get("quantity")
            priceEach = item.get("priceEach")
            for columnIDX, (_, v) in enumerate(item.items()):
                if v == None:   
                    continue
                else:
                    item = QTableWidgetItem(str(v)) 
                    self.productListTable.setItem(rowIDX, columnIDX, item)
            totalOrderPrice += quantity * priceEach
            orderAmount = QTableWidgetItem(str(quantity * priceEach))
            self.productListTable.setItem(rowIDX, 5, orderAmount)
            
        self.printPriceOfOrderLabel.setText(str(totalOrderPrice))
        self.productListTable.resizeColumnsToContents()
        self.productListTable.resizeRowsToContents() 
    
    def saveBtnClicked(self):
        if self.CSVradioButton.isChecked():   self.CSVFileSave()
        elif self.JSONradioButton.isChecked():   self.JSONFileSave()
        elif self.XMLradioButton.isChecked():   self.XMLFileSave()
    
    def CSVFileSave(self):
        columns = range(self.productListTable.columnCount())
        header = [self.productListTable.horizontalHeaderItem(column).text()
                    for column in columns]
        with open(f'{self.orderNo}.csv', 'w') as csvfile:
            writer = csv.writer(
                csvfile, dialect='excel', lineterminator='\n')
            writer.writerow(header)
            for row in range(self.productListTable.rowCount()):
                writer.writerow(
                    self.productListTable.item(row, column).text()
                    for column in columns)
    
    def XMLFileSave(self):
        root = Element('TABLE')
        with open(f'{self.orderNo}.xml', 'w') as xmlfile:
            for item in self.data:
                row = SubElement(root, 'ROW')
                for key, val in item.items():
                    row.attrib[key] = str(val)
        indent(root)
        tree = ElementTree(root)
        tree.write(f'./{self.orderNo}.xml')
        
    def JSONFileSave(self):
        filename = str(self.orderNo)
        with open(filename + '.json', 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4, cls=JSONEncoder)
        
#########################################

class DB_Utils:
    def queryExecutorNoParams(self, sql):
        conn = pymysql.connect(host='localhost', user='guest', password='bemyguest', db='classicmodels', charset='utf8')
        try:
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:     
                cursor.execute(sql)                            
                rows = cursor.fetchall()
                return rows
        except Exception as e:
            print(e)
            print(type(e))
        finally:
            cursor.close()
            conn.close()    
            
    def queryExecutor(self, sql, params):
        conn = pymysql.connect(host='localhost', user='guest', password='bemyguest', db='classicmodels', charset='utf8')
        try:
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:     
                cursor.execute(sql, params)                             
                rows = cursor.fetchall()
                return rows
        except Exception as e:
            print(e)
            print(type(e))
        finally:
            cursor.close()
            conn.close()        

class DB_Queries:
    def searchCustomer(self):
        sql = "SELECT DISTINCT name FROM customers ORDER BY name;"
        util = DB_Utils()
        rows = util.queryExecutorNoParams(sql)
        return rows
    
    def searchCountry(self):
        sql = "SELECT DISTINCT country FROM customers ORDER BY country"
        util = DB_Utils()
        rows = util.queryExecutorNoParams(sql)
        return rows

    def searchCity(self):
        sql = "SELECT DISTINCT city FROM customers ORDER BY city"
        util = DB_Utils()
        rows = util.queryExecutorNoParams(sql)
        return rows

    def searchALL(self):
        sql = "SELECT orderNo, orderDate, requiredDate, shippedDate, status, customers.name, comments FROM customers INNER JOIN orders ON customers.customerId = orders.customerId ORDER BY orderNo"
        util = DB_Utils()
        rows = util.queryExecutorNoParams(sql)
        return rows
    
    def selectCustomer(self, customer):
        sql = "SELECT orderNo, orderDate, requiredDate, shippedDate, status, customers.name, comments FROM customers INNER JOIN orders ON customers.customerId = orders.customerId WHERE name = %s ORDER BY orderNo"
        params = (customer)
        util = DB_Utils()
        rows = util.queryExecutor(sql, params)
        return rows
    
    def selectCountry(self, country):
        sql = "SELECT orderNo, orderDate, requiredDate, shippedDate, status, customers.name, comments FROM customers INNER JOIN orders ON customers.customerId = orders.customerId WHERE country = %s ORDER BY orderNo"
        params = (country)
        util = DB_Utils()
        rows = util.queryExecutor(sql, params)
        return rows

    def selectCity(self, city):
        sql = "SELECT orderNo, orderDate, requiredDate, shippedDate, status, customers.name, comments FROM customers INNER JOIN orders ON customers.customerId = orders.customerId WHERE city = %s ORDER BY orderNo"
        params = (city)
        util = DB_Utils()
        rows = util.queryExecutor(sql, params)
        return rows
    
    def selectCityInCountry(self, country):
        sql = "SELECT DISTINCT city FROM customers WHERE country = %s ORDER BY city"
        params = (country)
        util = DB_Utils()
        rows = util.queryExecutor(sql, params)
        return rows
    
    def showDetail(self, orderNo):
        sql = "SELECT orderLineNo, orderDetails.productCode, products.name, quantity, priceEach FROM orders INNER JOIN orderDetails ON orders.orderNo = orderDetails.orderNo INNER JOIN products ON orderDetails.productCode = products.productCode WHERE orders.orderNo = %s ORDER BY orderLineNo;"
        params = (orderNo)
        util = DB_Utils()
        rows = util.queryExecutor(sql, params)
        return rows
    
# JSON 파일의 Decimal을 float형으로 바꿔주는 함수
class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)  
    
# xml 파일에 들여쓰기를 추가하여 가독성을 높여주는 함수
def indent(elem, level=0): 
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()