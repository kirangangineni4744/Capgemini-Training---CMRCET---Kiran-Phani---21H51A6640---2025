# Mail --> Interface
#      --> send() Abstract
# Email
# SMS 
# WhatsApp


from abc import ABC,abstractmethod

class Mail(ABC):
    @abstractmethod
    def display(self):
        pass

class Email(Mail):
    def display(self,email):
        self.email=email
        print("Enter your mail ID:",self.email)

class SMS(Mail):
    def display(self,sms):
        self.sms=sms
        print("Your SMS Message:",self.sms)

class WhatsApp(Mail):
    def display(self,wa_message):
        self.wa_message=wa_message
        print("Your WA message:",self.wa_message)
        
m=Email()
s=SMS()
w=WhatsApp()
m.display("abcd@gmail.com")
s.display("Hello!")
w.display("Hi")