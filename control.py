from pyexpat import model
from xmlrpc.client import boolean
from PyQt5 import uic,QtWidgets
import psycopg2
from PyQt5.QtGui import QStandardItemModel, QStandardItem

try:
    banco = psycopg2.connect(
        host="localhost",
        database="DIDMANAGER",
        user="postgres",  
        password="DADOS"
    )
    print("Conexão com o banco de dados estabelecida com sucesso!")
except psycopg2.Error as e:
    print(f"Erro ao conectar ao banco de dados: {e}")

def MainFunction():
    line1 = form.lineEdit.text()
    line2 = form.lineEdit_2.text()
    line3 = form.lineEdit_3.text()
    line4 = form.lineEdit_4.text()
    box = form.comboBox.currentText()
  

    status1 = ""
    if form.radioButton.isChecked():
       print("End of Stock")
       status1 = "End of Stock" 

    elif form.radioButton_2.isChecked():
       print("Promotion") 
       status1 = "Promotion" 
  
    print("Code:", line1)
    print("Name:", line2)
    print("Price:", line3)
    print("Stock:",line4)
    print("Type:",box)

    try:
        cursor = banco.cursor()

        comando_sql = "INSERT INTO product (product_code, product_name, product_price, product_stock, product_type, product_status) VALUES (%s, %s, %s, %s, %s, %s)"

        dados = (line1, str(line2), line3, line4, box, str(status1))

        cursor.execute(comando_sql, dados)
        banco.commit()
        cursor.close()

        print("Dados inseridos com sucesso!")

    except psycopg2.Error as e:
        print(f"Erro ao inserir os dados: {e}")
         
    treeview_update() 
     
def treeview_update():    
    treev = form.treeView  


    model = QStandardItemModel()
    model.setHorizontalHeaderLabels(['Code', 'Name', 'Price', 'Stock', 'Type', 'Status'])

    cursor = banco.cursor()
    cursor.execute("SELECT product_code, product_name, product_price, product_stock, product_type, product_status FROM product")
    rows = cursor.fetchall()
    cursor.close()    

    print(f"Registros encontrados: {rows}")  # Depuração
           
    if not rows:
        print("Nenhum dado encontrado no banco.")
    else:
        for row in rows:
            items = [QStandardItem(str(field)) for field in row]  # Criando itens para cada campo
            model.appendRow(items)  # Adicionando linha ao modelo

    treev.setModel(model)  # Definindo o modelo atualizado na TreeView
    print("TreeView atualizada!")

app=QtWidgets.QApplication([])
form=uic.loadUi("form.ui")
form.pushButton.clicked.connect(MainFunction)

treeview_update() 
form.show()
app.exec()