import datetime
import random 
from pandas import *
import smtplib
from constants import *

my_email=EMAIL
password=PASSWORD
message="subject:Hello followers\n\nexample using constans"


# #creamos un objeto de este modulo que recibe 2 parametros, mail-server y puerto
# with  smtplib.SMTP("smtp.gmail.com", 587) as connection:


#     #  TLS (Transport Layer Security), usamos esta funcion para encriptar nuestro msj y para una conexion segura
#     connection.starttls()


#     #ingresamos nuestro correo y contrasena a la funcion login
#     connection.login(user=my_email, password=password)


#     # enviamos nuestro correo
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="bardack134@gmail.com", 
#                         msg=message)



# # NOTE:logre enviar el correo, intentar enviar el correo pero creando constantes

#TODO: COMPROVAMOS SI LA FECHA DE HOY COINCIDE CON ALUGO DE NUESTROS CUMPLEA;OS DEL ARCHIVO birthday.csv

birthdays_dataframe=read_csv('birthdays.csv')


#creamos una lista de  diccionarios del dataframe, ‘records’ : list like [{column -> value}, … , {column -> value}]
birthday_dict=birthdays_dataframe.to_dict('records')


#calculamos la fecha de hoy con datetime
today_date=datetime.datetime.today()


#mes y dia de hoy
today_month=today_date.month
today_day=today_date.day


#recorro mi lista de diccionarios
for dict in birthday_dict:
    
    #compruebo si la fecha de hoy coincide con algun cumplea;os
    if today_month == dict['month']:
        
        friend_name=dict['name']
        
        friend_email=dict['email']
  
        
#lista de cartas, aca pondremos todas nuestras cartas
letter_list=[]

#TODO: ESCOGEMOS UN MENSAJE ALEATORIO DE NUESTROS MENSAJES    
with open("letter_templates/letter_1.txt", "r")  as letter1:
    
    #creamos una lista de lineas del archivo
    letter_1=letter1.readlines()
    
    
    #agregamos nuestra carta a la lista de cartas
    letter_list.append(letter_1)


#hacemos  el mismo procedimiento con las demas cartas
with open("letter_templates/letter_2.txt", "r")  as letter2:
    
    
    letter_2=letter2.readlines()
        
    
    letter_list.append(letter_2)
    
    
with open("letter_templates/letter_3.txt", "r")  as letter3:
    
    
    letter_3=letter3.readlines()
        
    
    letter_list.append(letter_3)
    

#escogemos aleatoriamente una de nuetras letter de la lista de letters
random_letter=random.choice(letter_list)
print(random_letter)


#obtenemos el lugar donde esta escrito [NAME]
initial_msg=random_letter[0]
print(initial_msg)


#incrustamos el　nombre de nuestro amigo en [NAME]    
new_initial_msg=initial_msg.replace("[NAME]", friend_name)
print(new_initial_msg)


#remplazamos el inicio del mensaje con el nuevo mensaje en random_letter
random_letter[0]=new_initial_msg
print(random_letter)

#NOTE: TENEMOS EN FORMATO LISTA, LA CARTA PERSONALIZADA CON EL NOMBRE DE NUESTRO AMIGO, ...APARTIR DE AHORA CREAR LA CARTA EN FORMATO .TXT

# 4. Send the letter generated in step 3 to that person's email address.





