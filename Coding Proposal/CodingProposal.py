from tkinter import *
win=Tk()
win.geometry('500x200')
win.title("Welcome Tungii")

def yes():
    ro=Tk()
    ro.title("Pehla")
    ro.geometry('500x300')
    def clicked():
        par=Tk()
        par.title("Pehla")
        par.geometry('500x300')
        def otta():
            ok=Tk()
            ok.title("Coding")
            ok.geometry('500x300')
            def search():
                se=Tk()
                se.title("Proposal")
                se.geometry('500x300')
                def checku():
                    if(en.get()=="k8aangnnaudta"):
                        ke=Tk()
                        ke.title("Hain")
                        ke.geometry('420x90')
                        def yess():
                            ye=Tk()
                            ye.title(":)")
                            ye.geometry('500x300')
                            l1=Label(ye, text="OH! THANK-YOU FOR ACCEPTING MY PROPOSAL", font='Monospace', fg="orange")
                            l1.grid(row=0, column=0)
                            l1=Label(ye, text="WE WILL BE ROCKINGG", font='Monospace', fg="orange")
                            l1.grid(row=1, column=0)
                            ye.mainloop()
                        def noo():
                            nu=Tk()
                            nu.title(":(")
                            nu.geometry('500x200')
                            l1=Label(nu, text="Fine! I wont deserve You:(", font='Monospace', fg="Red")
                            l1.grid(row=0, column=0)
                            nu.mainloop()
                        
                        l1=Label(ke, text="Finally You reached DeadPoint!", font='Monospace', fg="Blue")
                        l1.grid(row=0, column=0)
                        l1=Label(ke, text="Now listen! I would like to tell you about U")
                        l1.grid(row=1, column=0)
                        l1=Label(ke, text="In study matter, I feel we both are equal right? You are the perfect match for me!")
                        l1.grid(row=2, column=0)
                        l1=Label(ke, text="I feel, we can be the best team if we work each other! So... Directly I'll Ask")
                        l1.grid(row=3, column=0)
                        l1=Label(ke, text="WILL YOU BE MY PROJECT PARTNER?", font='Monospace', fg="Blue")
                        l1.grid(row=4, column=0)
                        b1=Button(ke, text="   Yes   ", fg="white", bg="green",command=yess)
                        b1.grid(row=4, column=1)
                        b2=Button(ke, text="   No   ", fg="white", bg="red", command=noo)
                        b2.grid(row=4, column=2)
                        ke.mainloop()
                        
                    else:
                        l1=Label(se, text="Key is wrong>>Serach Carefully", fg="blue")
                        l1.grid(row=3, column=0)
                l1=Label(se, text="Enter your key", font='Monospace', fg="green")
                l1.grid(row=0, column=0)
                en=Entry(se, bd=4)
                en.grid(row=0, column=1)
                b1=Button(se, text="  Sign-in   ", fg="red", bg="yellow", command=checku)
                b1.grid(row=1, column=0)
                
                se.mainloop()
            
            l1=Label(ok, text="I have a task for you", font='Monospace', fg="Red")
            l1.grid(row=0, column=0)
            l1=Label(ok, text="Your duty is to seracha key and login to the most important page", fg="blue")
            l1.grid(row=1, column=0)
            l1=Label(ok, text="Paap anta heli, I will give some hints to you.", fg="blue")
            l1.grid(row=2, column=0)
            l1=Label(ok, text="Hint: Search for a key in a folder called tpp which is present on desktop", fg="blue")
            l1.grid(row=3, column=0)
            l1=Label(ok, text="Will u serach for a key?", font='Monospace', fg="orange")
            l1.grid(row=4, column=0)
            b1=Button(ok, text="   Okay:)   ", fg="white", bg="black", command=search)
            b1.grid(row=4, column=1)

            ok.mainloop()
        
        l1=Label(par, text="I want to know you technically!", font='Monospace', fg="Green")
        l1.grid(row=0, column=0)
        l1=Label(par, text="Tell me which Programming language", font='Monospace', fg="Green")
        l1.grid(row=1, column=0)
        l1=Label(par, text="Do you like most?", font='Monospace', fg="Green")
        l1.grid(row=2, column=0)
        e=Entry(par, bd=4)
        e.grid(row=3, column=0)
        l1=Label(par, text="Okay, then shall we move furthur?", font='Monospace', fg="Green")
        l1.grid(row=4, column=0)
        b1=Button(par, text="   Otttuuu   ", fg="white", bg="red", command=otta)
        b1.grid(row=4, column=1)
        par.mainloop()
    
    l1=Label(ro, text="Okay! Now listen. I have planned something", font='Monospace', fg="Orange")
    l1.grid(row=0, column=0)
    l1=Label(ro, text="for you. I will accept all your answers.", font='Monospace', fg="Orange")
    l1.grid(row=1, column=0)
    l1=Label(ro, text="Note:Thatt anta Helbeku Ok?", font='Monospace', fg="Orange")
    l1.grid(row=2, column=0)
    l1=Label(ro, text="Ok, Click here Jaldi", font='Monospace', fg="Orange")
    l1.grid(row=3, column=0)
    b1=Button(ro, text="   Click Bhaii   ", fg="White", bg="Blue", command=clicked)
    b1.grid(row=4, column=0)
    ro.mainloop()

def no():
    ot=Tk()
    ot.title("Bad Luck")
    ot.geometry('200x100')
    l1=Label(ot, text="No means fine:(", font='Monospace', fg="Red")
    l1.grid(row=0, column=0)
    ot.mainloop()

l1=Label(win, text="Hey Tungi, Nan ning eno helbeku ok? ", font='Monospace', fg="Blue")
l1.grid(row=0, column=0)

l2=Label(win, text="Have patience till the end......", font='Monospace', fg="Blue")
l2.grid(row=1, column=0)

l3=Label(win, text="Soch samaj ke decision le looo!!", font='Monospace', fg="Blue")
l3.grid(row=2, column=0)

l4=Label(win, text="Are you ready?", font='Monospace', fg="Red")
l4.grid(row=4, column=0)



b1=Button(win, text="   Yes   ", fg="white", bg="green", command=yes)
b1.grid(row=4, column=1)

b2=Button(win, text="   No   ", fg="white", bg="red", command=no)
b2.grid(row=4, column=2)

win.mainloop()
