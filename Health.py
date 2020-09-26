from tkinter import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import webbrowser
from sklearn.naive_bayes import GaussianNB
import pandas as pd
import link
def Details():

    window2 = Toplevel(window)
    window2.title("Disease Checkup")
    age = Label(window2, text="AGE")
    age.pack()
    global entryAge
    entryAge= Entry(window2)
    entryAge.pack()
    sex = Label(window2, text="GENDER")
    sex.pack()
    global v1
    v1 = IntVar()
    R3 = Radiobutton(window2, text="Male", variable=v1, value=1.0)
    R3.pack()
    R4 = Radiobutton(window2, text="Female", variable=v1, value=0.0)
    R4.pack()

    smoking = Label(window2, text="Smoking ")
    smoking.pack()
    global v2
    v2 = IntVar()
    R5 = Radiobutton(window2, text="No", variable=v2, value=0.0)
    R5.pack()
    R6 = Radiobutton(window2, text="Yes", variable=v2, value=1.0)
    R6.pack()

    cigDay = Label(window2, text="Cigrate Per Day")
    cigDay.pack()
    global entryperday
    entryperday = Entry(window2)
    entryperday.pack()
    BPMed = Label(window2, text="Taking BP medicine ")
    BPMed.pack()
    global v3
    v3 = IntVar()
    R7= Radiobutton(window2, text="No", variable=v3, value=0.0)
    R7.pack()
    R8 = Radiobutton(window2, text="Yes", variable=v3, value=1.0)
    R8.pack()
    Diab = Label(window2, text=" Having Diabetese")
    Diab.pack()
    global v4
    v4 = IntVar()
    R9 = Radiobutton(window2, text="No", variable=v4, value=0.0)
    R9.pack()
    R10 = Radiobutton(window2, text="Yes", variable=v4, value=1.0)
    R10.pack()

    chol = Label(window2, text="Enter Cholestrol (in mg/dL):")
    chol.pack()
    global entryChol
    entryChol= Entry(window2)
    entryChol.pack()

    sysBP = Label(window2, text="Enter Systolic BP (in mg/dl):")
    sysBP.pack()
    global entrysysBp
    entrysysBp= Entry(window2)
    entrysysBp.pack()

    DiaBp = Label(window2, text=" Enter  Diastolic BP (in mg/dl):")
    DiaBp.pack()
    global entryDiabp
    entryDiabp= Entry(window2)
    entryDiabp.pack()

    Heart = Label(window2, text="Enter Heart Rate (Beats/Min)")
    Heart.pack()
    global entryHR
    entryHR = Entry(window2)
    entryHR.pack()

    glucose = Label(window2, text="Enter Glucose (mg/dL)")
    glucose.pack()
    global entryGlu
    entryGlu = Entry(window2)
    entryGlu.pack()

    btnCheck = Button(window2, text="Submit", command=fun2)
    btnCheck.pack()

def fun2():

    window3=Toplevel(window)
    window3.title("Result")
    window3.minsize(1000,200)

    class DiseasData():

        def __init__(self,sex=0.0,age=0.0, smoking=0.0, cigDay=0.0, BPMed=0.0, Diab=0.0, chol=0.0,sysBp=0.0,DiaBp=0.0,BMI=0.0,HRate=0.0,glucose=0.0):

            self.sex = sex
            self.age = age
            self.smoking = smoking
            self.cigDay = cigDay
            self.BPMed = BPMed
            self.Diab = Diab
            self.chol = chol
            self.sysBp = sysBp
            self.DiaBp = DiaBp
            self.BMI = BMI
            self.HRate = HRate
            self.glucose= glucose


    R = DiseasData(None,None, None, None, None, None, None, None)
    R.NAME=entryName.get()
    R.No=entryMobile.get()
    R.sex = float(v1.get())
    R.age = float(entryAge.get())
    R.smoking = float(v2.get())
    R.cigDay = float(entryperday.get())
    R.BPMed = float(v3.get())
    R.Diab = float(v4.get())
    R.chol = float(entryChol.get())
    R.sysBp = float(entrysysBp.get())
    R.DiaBp = float(entryDiabp.get())
    R.BMI = float(round(BMI,2))
    R.HRate = float(entryHR.get())
    R.glucose = float(entryGlu.get())

    db = firestore.client()
    D = R.__dict__
    db.collection("DiseaseData").document().set(D)

    Input = [R.sex, R.age, R.smoking, R.cigDay, R.BPMed, R.Diab, R.chol,R.sysBp,R.DiaBp,R.BMI,R.HRate,R.glucose]

    data = pd.read_csv("heart2data.csv")

    features = []
    for i in range(0, len(data)):
        features.append(
            [data.male[i], data.age[i], data.currentSmoker[i], data.cigsPerDay[i], data.BPMeds[i], data.diabetes[i],data.totChol[i],data.sysBP[i],data.diaBP[i],data.BMI[i],data.heartRate[i],data.glucose[i]])

    Labels = []
    for i in range(0, len(data)):
        Labels.append(data.TenYearCHD[i])

    Disease = ["No You don't have chances of Heart Disease", "Yes You have chances of heart disease"]
    model = GaussianNB()
    model.fit(features, Labels)

    predicLabels = model.predict([Input])
    result = Label(window3,text=Disease[predicLabels[0]], font=('AR BLANCA',36),fg = "#D60300")
    result.pack()

    frame = Frame(window3, width=300, height=100)
    frame.pack()

    text = Text(frame)

    text.pack()

    hyperlink = link.HyperlinkManager(text)

    def click1():
        webbrowser.open("https://www.practo.com/{}/cardiologist".format(entryCity.get()))

    text.insert(INSERT,"click this link for Doctor ")
    text.insert(INSERT, " Help", hyperlink.add(click1))
    window3.mainloop()


def fun():

    class signIn():
        def __init__(self, name, city, weight=0, height=0, Mobile=0):
            self.name = name
            self.city = city
            self.weight = weight
            self.height = height
            self.mobile = Mobile
    r = signIn(None, None,None,None,None )
    r.name =entryName.get()
    r.city =entryCity.get()
    r.weight =entryWeight.get()
    r.height =entryHeight.get()
    r.mobile = entryMobile.get()

    credent = credentials.Certificate('raj.json')
    firebase_admin.initialize_app(credent)
    db = firestore.client()
    s = r.__dict__
    docs = db.collection("DiseaseData").stream()
    db.collection("Data").document().set(s)
    global BMI
    BMI = (float(r.weight) / (float(r.height) * float(r.height))) * 10000

    if BMI < 16:
        newwin = Toplevel(window)
        # newwin.geometry("500x100")
        display = Label(newwin, font=('AR BLANCA', 36), fg="#D60300", text="SEVERE THICKNESS")
        display.pack()
        choice = Label(newwin, text="Do you want further check-ups", font=('AR BLANCA', 18))
        choice.pack()

        v = IntVar()

        R1 = Radiobutton(newwin, text="Yes", variable=v, value=1, command=Details)
        R1.pack()
        R2 = Radiobutton(newwin, text="No", variable=v, value=0, command=exit)
        R2.pack()
        newwin.mainloop()

    elif 16 < BMI < 17:
        newwin = Toplevel(window)
        display = Label(newwin, font=('AR BLANCA', 36), fg="#D60300", text="MODERATE THICKNESS")
        display.pack()
        choice = Label(newwin, text="Do you want further check-ups", font=('AR BLANCA', 18))
        choice.pack()
        v = IntVar()
        R1 = Radiobutton(newwin, text="Yes", variable=v, value=1, command=Details)
        R1.pack()
        R2 = Radiobutton(newwin, text="No", variable=v, value=0, command=exit)
        R2.pack()
        newwin.mainloop()

    elif 17 <= BMI < 18.5:
        newwin = Toplevel(window)

        display = Label(newwin, font=('AR BLANCA', 36), fg="#D60300", text="MILD THICKNESS")
        display.pack()
        choice = Label(newwin, text="Do you want further check-ups", font=('AR BLANCA', 18))
        choice.pack()
        v = IntVar()
        R1 = Radiobutton(newwin, text="Yes", variable=v, value=1, command=Details)
        R1.pack()
        R2 = Radiobutton(newwin, text="No", variable=v, value=0, command=exit)
        R2.pack()
        newwin.mainloop()

    elif 18.5 <= BMI < 25:
        newwin = Toplevel(window)

        display = Label(newwin, font=('AR BLANCA', 36), fg="#D60300", text="NORMAL ")
        display.pack()
        choice = Label(newwin, text="Do you want further check-ups", font=('AR BLANCA', 18))
        choice.pack()
        v = IntVar()
        R1 = Radiobutton(newwin, text="Yes", variable=v, value=1, command=Details)
        R1.pack()
        R2 = Radiobutton(newwin, text="No", variable=v, value=0, command=exit)
        R2.pack()
        newwin.mainloop()

    elif 25 <= BMI < 30:
        newwin = Toplevel(window)
        display = Label(newwin, font=('AR BLANCA', 36), fg="#D60300", text="OVERWEIGHT ")
        display.pack()
        choice = Label(newwin, text="Do you want further check-ups", font=('AR BLANCA', 18))
        choice.pack()
        v = IntVar()
        R1 = Radiobutton(newwin, text="Yes", variable=v, value=1, command=Details)
        R1.pack()
        R2 = Radiobutton(newwin, text="No", variable=v, value=0, command=exit)
        R2.pack()
        newwin.mainloop()

    elif 30 <= BMI < 35:
        newwin = Toplevel(window)
        display = Label(newwin, font=('AR BLANCA', 36), fg="#D60300", text="OBESE CLASS I")
        display.pack()
        choice = Label(newwin, text="Do you want further check-ups", font=('AR BLANCA', 18))
        choice.pack()
        v = IntVar()
        R1 = Radiobutton(newwin, text="Yes", variable=v, value=1, command=Details)
        R1.pack()
        R2 = Radiobutton(newwin, text="No", variable=v, value=0, command=exit)
        R2.pack()
        newwin.mainloop()

    elif 35 <= BMI < 40:
        newwin = Toplevel(window)
        display = Label(newwin, font=('AR BLANCA', 36), fg="#D60300", text="OBESE CLASS II ")
        display.pack()
        choice = Label(newwin, text="Do you want further check-ups", font=('AR BLANCA', 18))
        choice.pack()
        v = IntVar()
        R1 = Radiobutton(newwin, text="Yes", variable=v, value=1, command=Details)
        R1.pack()
        R2 = Radiobutton(newwin, text="No", variable=v, value=0, command=exit)
        R2.pack()
        newwin.mainloop()

    else:
        newwin = Toplevel(window)
        display = Label(newwin, font=('AR BLANCA', 36), fg="#D60300", text="OBESE CLASS ")
        display.pack()
        choice = Label(newwin, text="Do you want further check-ups", font=('AR BLANCA', 18))
        choice.pack()
        v = IntVar()
        R1 = Radiobutton(newwin, text="Yes", variable=v, value=1, command=Details)
        R1.pack()
        R2 = Radiobutton(newwin, text="No", variable=v, value=0, command=exit)
        R2.pack()
        newwin.mainloop()





window = Tk()
window.title("FitBit.exe")
photo = PhotoImage(file = "heart.gif")
w = Label(window, image=photo)
w.pack()
name = Label(window,text="NAME")
name.pack()
entryName = Entry(window)
entryName.pack()
Mobile = Label(window, text="Mobile No.")
Mobile.pack()
entryMobile = Entry(window)
entryMobile.pack()
city = Label(window,text="CITY")
city.pack()
global entryCity
entryCity = Entry(window)
entryCity.pack()
weight = Label(window,text="WEIGHT(in Kg)")
weight.pack()
entryWeight = Entry(window)
entryWeight.pack()
height = Label(window,text="HEIGHT(in Cm)")
height.pack()

entryHeight = Entry(window)
entryHeight.pack()
btnSubmit = Button(window,text="CHECK-BMI",command=fun)
btnSubmit.pack()
window.mainloop()