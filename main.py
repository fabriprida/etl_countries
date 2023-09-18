from api_data import fetch_country_data
from db_creation import create_database, store_data
from excel_generation import generate_excel
from mail_send import send_email

if __name__ == "__main__":
    # Obtener datos
    data = fetch_country_data()

    # Crear y almacenar en la base de datos
    engine = create_database()
    store_data(engine, data)

    # Generar archivo Excel
    generate_excel(engine)

    #Enviar email 
    sender_email = input("Enter sender email: ")
    password = 'dpbsjtooyjbkicng'
    receiver_email = input("Enter receiver email: ")
    
    send_email(sender_email, password, receiver_email)