from curses import *
from twilio.rest import Client 
import random
from tkinter import *
from tkinter import messagebox 

class otp_verifier(Tk):
    def __int__(self):
        super().__int__()
        self.geometry("600*550")
        self.resizable(False, False)
        self.n= random.randint(1000, 9999)
        self.client = Client("AC9bff51b1dde5a6505ba30f93323211a0","c87a725fe5be6d98209395308ab77399")
        self.client.massages.create(to = ["+917870899818"],
                                    from_ ="+18643872629",
                                    body=self.n)
    
    
    def Labels(self):
        self.c= Canvas(self, bg= "white", width=400, height=280)    
        self.c.place(x=100, y=60)
        
        self.Login_Title= Label(self,text="OTP verification", font= "bold, 20", bg= "white") 
        self.Login_Title.place(x=210, y=90)
        
        
    def Entry(self):
        self.User_Name=Text(self, borderwidth=2, wrap="word", width=29, height=2)
        self.User_Name.place(x=190, y=160)
        
    def Button(self):
        self.submitButtonImage= PhotoImage(file="submit.png")
        self.submitButton= Button(self,image=self.submitButtonImage, command=self.checkOTP,border=0)
        self.submitButton.place(x=208,y=240)
        
        self.resendOTPImage=PhotoImage(file="resendOTP.png")
        self.resendOTP=Button(self, image= self.resendOTPImage, command=self.resendOTP, border=0)
        self.resendOTP.place(x=208,y=400)
        
        
        
    def checkOTP(self):
        try:
            self.userInput= int(self.User_Name.get(1.0, "end-1c"))
            if self.userInput==self.n:
                messagebox.showinfo("showinfo", "Login Success")
                self.n= "done"
            
            elif self.n=="done":
                messagebox.showinfo("showinfo", "Already Enterd the OTP")
            else:
                messagebox.showinfo("showinfo", "Wrong OTP")
        except:
            messagebox.showinfo("showinfo", "Invalid OTP")
                  
        
    def resendOTP(self):
        self.n= random.randint(1000, 9999)
        self.client = Client("AC9bff51b1dde5a6505ba30f93323211a0","c87a725fe5be6d98209395308ab77399")
        self.client.messages.create(to = ["+917870899818"],
                                    from_ ="+18643872629",
                                    body=self.n)       
        
        
if __name__ =="__main__":
    window = otp_verifier()
    window.Labels()
    window.Entry()
    window.Button()
    window.mainloop()
    
        
    
