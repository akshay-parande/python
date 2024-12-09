

import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage


listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source,1000)
            print("Recognising......")
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        print("Try Again")
        return get_info()
    


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login("akshayparande3522@gmail.com", "")
    email = EmailMessage()
    email['From'] = 'Sender_Email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'rishika': 'rishikamarottikal05@gmail.com',
    'rupali' : 'gandotrarupali11@gmail.com',
    'sahil' : 'deshmukhsahil384@gmail.com'
}



def get_email_info():
    talk('To whom do you want to send the email?')
    print("Adding Recipient")
    name = get_info()
    receiver = email_list.get(name)
    if receiver:
        talk('What is the subject of your email?')
        print("Adding Subject")
        subject = get_info()
        talk('Tell me the text of your email')
        print("Adding text of the email")
        message = get_info()
        send_email(receiver, subject, message)
        talk('Hey, your email has been sent successfully!')
        print("Email sent Successfully")
        
    else:
        talk('Sorry, I could not find the recipient in the list. Please try again.')

get_email_info()
