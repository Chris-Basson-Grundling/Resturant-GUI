from tkinter import *
import random
import time
from tkinter import messagebox
from tkinter import ttk

root = Tk()

root.geometry("1600x800+0+0")       #Size Of Window

root.title("Make Orders")      #Title Of Window

root.configure(background='blue') #Background of Window
#============================================Size of sections in window=================================================
Tops = Frame(root, width=1250, height=90, bd=1, relief="sunken")
Tops.pack(side=TOP)

f1 = Frame(root, width=750, height=750, bd=1, relief="sunken")
f1.pack(side=LEFT)

f2 = Frame(root, width=400, height=950, bd=1, relief="sunken")
f2.pack(side=RIGHT)

f1a = Frame(f1, width=900, height=330, bd=1, relief="sunken")
f1a.pack(side=TOP)

f2a = Frame(f1, width=850, height=520, bd=1, relief="sunken")
f2a.pack(fill=BOTH, side=BOTTOM)

ft2 = Frame(f2, width=440, height=450, bd=1, relief="sunken")
ft2.pack(side=TOP)

fb2 = Frame(f2, width=440, height=750, bd=1, relief="sunken")
fb2.pack(side=BOTTOM)

f1aa = Frame(f1a, width=400, height=330, bd=1, relief="sunken")
f1aa.pack(side=LEFT)

f1ab = Frame(f1a, width=400, height=330, bd=1, relief="sunken")
f1ab.pack(side=RIGHT)

f2aa = Frame(f2a, width=450, height=330, bd=1, relief="sunken")
f2aa.pack(side=LEFT)

f2ab = Frame(f2a, width=450, height=330, bd=1, relief="sunken")
f2ab.pack(side=RIGHT)

# ============================ Background color ==================================================

Tops.configure(background='powder blue')
f1.configure(background='powder blue')
f2.configure(background='powder blue')

# ================================Main Lable=================================

lblInfo = Label(Tops, font=('sans', 64, 'bold'), text="Make Orders:", bd=9)
lblInfo.grid(row=0, column=0)


# ================================== Cost Method ====================================

def CostofItems():
    flag = False
    while flag == False:
        try:
            Item1 = float(E_Fries.get())
            Item2 = float(E_Lunch.get())
            Item3 = float(E_Burger.get())
            Item4 = float(E_Pizza.get())
            Item5 = float(E_CheeseBurger.get())
            Item6 = float(E_MacNuggets.get())
            Item7 = float(E_MacPuff.get())
            Item8 = float(E_ChickenWings.get())

            Item9 = float(E_Coffee_Cake.get())
            Item10 = float(E_Red_Velvet_Cake.get())
            Item11 = float(E_Black_Forest.get())
            Item12 = float(E_Boston_Cream_Cake.get())
            Item13 = float(E_Latta.get())
            Item14 = float(E_Coke.get())
            Item15 = float(E_Pepsi.get())
            Item16 = float(E_Cappuccino.get())

            PriceofFood = (Item2 * 90) + (Item3 * 50) + (Item4 *100) + (Item5 * 50) + (Item6 * 80) +\
                           (Item7 * 50) + (Item8 * 120)

            PriceofCakesandDrinks =(Item9 * 100) + (Item10 * 110) + (Item11 * 100) + (Item12 *110) + (Item13 * 70) + \
                          (Item14 * 70) + (Item15 * 80) + (Item16 * 100)

            FoodPrice = "Rs "+ str('%.2f' % PriceofFood)
            DrinksandCakesPrice = "Rs "+ str("%.2f" % PriceofCakesandDrinks)
            CostofFood.set(FoodPrice)
            CostofCakesandDrinks.set(DrinksandCakesPrice)
            SC =  ((PriceofFood + PriceofCakesandDrinks)*0.15)
            print("Rs " + str("%.2f" % SC))
            ServiceCharge.set("Rs "+ str("%.2f" % SC))

            SubTotalofITEMS = "Rs "+ str(round(PriceofFood + PriceofCakesandDrinks + SC))
            SubTotal.set(SubTotalofITEMS)

            Tax = "Rs "+ str(round((PriceofFood + PriceofCakesandDrinks + SC)*0.15))
            Tax_Flo = float(round(PriceofCakesandDrinks + PriceofFood + SC)*0.15)
            PaidTax.set(Tax)
            TT = (PriceofFood + PriceofCakesandDrinks + SC)
            TC = "Rs "+ str(round((PriceofFood + PriceofCakesandDrinks + SC) + Tax_Flo))
            print((TC))
            TotalCost.set(TC)
            flag = True
        except :
                print("Please enter numbers only !")
                Reset()


# ===================================== Exit Window ===============================================


def qExit():

    qExit = messagebox.askyesno("Quit System", "Do you want to quit?")
    if qExit > 0:
        root.destroy()
        import Login_window
        return

# ============================ Save Files  =========================================
def Save():
    file = open("myfile.txt", "x") 
    file = open("myfile.txt", "w")
    file.write('Receipt Ref:\t\t\t'+ Receipt_Ref.get() + '\t\t' + DateofOrder.get()+"\n") 
    file.write('Items\t\t\t\t' + "Cost of Items \n\n") 
    file.write('Table Number:\t\t\t\t\t' + E_Fries.get() + "\n") 
    file.write('Lunch Meal: \t\t\t\t\t' + E_Lunch.get() + "\n")
    file.write('Burger: \t\t\t\t\t' + E_Burger.get() + "\n") 
    file.write('Pizza: \t\t\t\t\t' + E_Pizza.get() + "\n") 
    file.write('Cheese Burger: \t\t\t\t\t' + E_CheeseBurger.get() + "\n") 
    file.write('Mac Nuggets: \t\t\t\t\t' + E_MacNuggets.get() + "\n") 
    file.write('Mac Puff: \t\t\t\t\t' + E_MacPuff.get() + "\n") 
    file.write('Chicken Wings: \t\t\t\t\t' + E_ChickenWings.get() + "\n") 
    file.write('Coffee Cake: \t\t\t\t\t' + E_Coffee_Cake.get() + "\n") 
    file.write('Red Valet Cake: \t\t\t\t\t' + E_Red_Velvet_Cake.get() + "\n") 
    file.write('Black Forest Cake: \t\t\t\t\t' + E_Black_Forest.get() + "\n")
    file.write('Boston Cream Cake: \t\t\t\t\t' + E_Boston_Cream_Cake.get() + "\n") 
    file.write('Latte: \t\t\t\t\t' + E_Latta.get() + "\n") 
    file.write('Coke: \t\t\t\t\t' + E_Coke.get() + "\n") 
    file.write('Pepsi: \t\t\t\t\t' + E_Pepsi.get() + "\n") 
    file.write('Cappuccino: \t\t\t\t\t' + E_Cappuccino.get() + "\n") 
    file.write('Cost of Food: \t\t\t\t\t' + CostofFood.get() + "\t\t\tTax Paid:\t\t\t\t\t" + PaidTax.get() + "\n") 
    file.write('Cost of Cakes and Drinks: \t\t\t\t\t' + CostofCakesandDrinks.get() + "\t\t\tSub Total:\t\t\t\t\t" +
                      SubTotal.get() + "\n")
    file.write('Service Charge: \t\t\t\t\t' + ServiceCharge.get() + "\t\t\tTotal Cost:\t\t\t\t\t" + TotalCost.get() + "\n")
    file.close()

# ====================================== Reset Method =========================================
def Reset():

    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofFood.set("")
    CostofCakesandDrinks.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0", END)

    E_Fries.set("1")
    E_Lunch.set("0")
    E_Burger.set("0")
    E_Pizza.set("0")
    E_CheeseBurger.set("0")
    E_MacNuggets.set("0")
    E_MacPuff.set("0")
    E_ChickenWings.set("0")

    E_Coffee_Cake.set("0")
    E_Red_Velvet_Cake.set("0")
    E_Black_Forest.set("0")
    E_Boston_Cream_Cake.set("0")
    E_Latta.set("0")
    E_Coke.set("0")
    E_Pepsi.set("0")
    E_Cappuccino.set("0")

    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("0")
    var8.set("0")
    var9.set("0")
    var10.set("0")
    var11.set("0")
    var12.set("0")
    var13.set("0")
    var14.set("0")
    var15.set("0")
    var16.set("0")


# =================================== Receipt Method ======================

def Receipt():
    txtReceipt.delete("1.0", END)
    x = random.randint(1000, 500890)
    randomRef = str(x)
    Receipt_Ref.set("BILL" + randomRef)
    txtReceipt.insert(END, 'Receipt Ref:\t\t\t'+ Receipt_Ref.get() + '\t\t' + DateofOrder.get()+"\n")
    txtReceipt.insert(END, 'Items\t\t\t\t' + "Cost of Items \n\n")
    txtReceipt.insert(END, 'Table Number:\t\t\t\t\t' + E_Fries.get() + "\n")
    txtReceipt.insert(END, 'Burger: \t\t\t\t\t' + E_Lunch.get() + "\n")
    txtReceipt.insert(END, 'Hot Dog: \t\t\t\t\t' + E_Burger.get() + "\n")
    txtReceipt.insert(END, 'Pizza: \t\t\t\t\t' + E_Pizza.get() + "\n")
    txtReceipt.insert(END, 'Burrito: \t\t\t\t\t' + E_CheeseBurger.get() + "\n")
    txtReceipt.insert(END, 'Steak: \t\t\t\t\t' + E_MacNuggets.get() + "\n")
    txtReceipt.insert(END, 'Fries: \t\t\t\t\t' + E_MacPuff.get() + "\n")
    txtReceipt.insert(END, 'Sandwich: \t\t\t\t\t' + E_ChickenWings.get() + "\n")
    txtReceipt.insert(END, 'Coke: \t\t\t\t\t' + E_Coffee_Cake.get() + "\n")
    txtReceipt.insert(END, 'Monster: \t\t\t\t\t' + E_Red_Velvet_Cake.get() + "\n")
    txtReceipt.insert(END, 'Fanta Orange: \t\t\t\t\t' + E_Black_Forest.get() + "\n")
    txtReceipt.insert(END, 'Coffee: \t\t\t\t\t' + E_Boston_Cream_Cake.get() + "\n")
    txtReceipt.insert(END, 'Milk: \t\t\t\t\t' + E_Latta.get() + "\n")
    txtReceipt.insert(END, 'Sprie: \t\t\t\t\t' + E_Coke.get() + "\n")
    txtReceipt.insert(END, 'Water: \t\t\t\t\t' + E_Pepsi.get() + "\n")
    txtReceipt.insert(END, 'Milkshake: \t\t\t\t\t' + E_Cappuccino.get() + "\n")
    txtReceipt.insert(END, 'Cost of Food: \t\t\t\t\t' + CostofFood.get() + "\t\t\tTax Paid:\t\t\t\t\t" + PaidTax.get() + "\n")
    txtReceipt.insert(END, 'Cost of Cakes and Drinks: \t\t\t\t\t' + CostofCakesandDrinks.get() + "\t\t\tSub Total:\t\t\t\t\t" +
                      SubTotal.get() + "\n")
    txtReceipt.insert(END, 'Service Charge: \t\t\t\t\t' + ServiceCharge.get() + "\t\t\tTotal Cost:\t\t\t\t\t" + TotalCost.get() + "\n")



# ============================== Inisiolizing Variables ===============================================


var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofCakesandDrinks = StringVar()
CostofFood = StringVar()
ServiceCharge = StringVar()

E_Table_Num = StringVar()
E_Fries = StringVar()
E_Lunch = StringVar()
E_Burger = StringVar()
E_Pizza = StringVar()
E_CheeseBurger = StringVar()
E_MacNuggets = StringVar()
E_MacPuff = StringVar()
E_ChickenWings = StringVar()

E_Coffee_Cake = StringVar()
E_Red_Velvet_Cake = StringVar()
E_Black_Forest = StringVar()
E_Boston_Cream_Cake = StringVar()
E_Latta = StringVar()
E_Coke = StringVar()
E_Pepsi = StringVar()
E_Cappuccino = StringVar()


E_Fries.set("0")
E_Lunch.set("0")
E_Burger.set("0")
E_Pizza.set("0")
E_CheeseBurger.set("0")
E_MacNuggets.set("0")
E_MacPuff.set("0")
E_ChickenWings.set("0")


E_Coffee_Cake.set("0")
E_Red_Velvet_Cake.set("0")
E_Black_Forest.set("0")
E_Boston_Cream_Cake.set("0")
E_Latta.set("0")
E_Coke.set("0")
E_Pepsi.set("0")
E_Cappuccino.set("0")

# ===========================Declaring Date=============================================

DateofOrder.set(time.strftime("%d/%m/%y"))

# ============== Food  buttons =======================================================

Fries = Label(f1aa, bg="powder blue", font=('sans',18, 'bold'), text="Table number: \t").grid(row=0, sticky=W)

Lunch = Label(f1aa, bg="powder blue", font=('sans', 18, 'bold'), text="Buger              \t").grid(row=1, sticky=W)

Burger = Label(f1aa, bg="powder blue", font=('sans', 18, 'bold'), text="Hot Dog                \t").grid(row=2, sticky=W)

Pizza = Label(f1aa, bg="powder blue", font=('sans', 18, 'bold'), text="Pizza            \t").grid(row=3, sticky=W)

CheeseBurger = Label(f1aa, bg="powder blue", font=('sans', 18, 'bold'), text="Burrito              \t").grid(row=4, sticky=W)

MacNuggets = Label(f1aa, bg="powder blue", font=('sans', 18, 'bold'), text="Steak            \t").grid(row=5, sticky=W)

MacPuff = Label(f1aa, bg="powder blue", font=('sans', 18, 'bold'), text="Fries              \t").grid(row=6, sticky=W)

ChickenWings = Label(f1aa, bg="powder blue", font=('sans', 18, 'bold'), text="Sandwich \t").grid(row=7, sticky=W)

# ========================== Drinks  Buttons ================================================

CoffeeCake = Label(f1ab, bg="powder blue", font=('sans', 18, 'bold'), text="Coke          \t").grid(row=0, sticky=W)

Red_Velvet_Cake = Label(f1ab, bg="powder blue", font=('sans', 18, 'bold'), text="Monster       \t").grid(row=1, sticky=W)

Black_Forest_Cake = Label(f1ab, bg="powder blue", font=('sans', 18, 'bold'), text="Fanta Orange \t").grid(row=2, sticky=W)

Boston_Cream_Cake = Label(f1ab, bg="powder blue", font=('sans', 18, 'bold'), text="Coffee       \t").grid(row=3, sticky=W)

Latta = Label(f1ab, bg="powder blue", font=('sans', 18, 'bold'), text="Milk        \t").grid(row=4, sticky=W)

Coke = Label(f1ab, bg="powder blue", font=('sans', 18, 'bold'), text="Sprite       \t").grid(row=5, sticky=W)

Pepsi = Label(f1ab, bg="powder blue", font=('sans', 18, 'bold'), text="Water          \t").grid(row=6, sticky=W)

Cappuccino = Label(f1ab, bg="powder blue", font=('sans', 18, 'bold'), text="Milkshake \t").grid(row=7, sticky=W)

# ======================================  Table Number assignment ===================================================

# Create a Tkinter variable
tkvar = StringVar(root)
# Dictionary with options
choices = { '1','2','3'}
txtFries = OptionMenu( f1aa, tkvar, *choices)
txtFries.grid(row=0, column=1)
tkvar.set('1') # set the default option
#from Login_window.register import username_entery

#if username_entry == Chris:
#    choices = { '1','2','3'}
 #   txtFries = OptionMenu( f1aa, tkvar, *choices)
 #   txtFries.grid(row=0, column=1)
#elif username_entry == Joana:
#    choices = {'4','5', '6'}
 #   txtFries = OptionMenu( f1aa, tkvar, *choices)
 #   txtFries.grid(row=0, column=1)
#else:
 #   choices = {'7','8', '9'}
 #   txtFries = OptionMenu( f1aa, tkvar, *choices)
#    txtFries.grid(row=0, column=1)

# ====================================== Food Widgets ===================================================

txtLunch = Entry(f1aa, font=('sans', 16, 'bold'), bd=1, bg="steel blue", width=6, justify='left', textvariable=E_Lunch,
                    state=NORMAL)
txtLunch.grid(row=1, column=1)
txtBurger = Entry(f1aa, font=('sans', 16, 'bold'), bd=1, bg="steel blue", width=6, justify='left', textvariable=E_Burger,
                      state=NORMAL)
txtBurger.grid(row=2, column=1)
txtPizza = Entry(f1aa, font=('sans', 16, 'bold'), bd=1, bg="steel blue", width=6, justify='left', textvariable=E_Pizza,
                       state=NORMAL)
txtPizza.grid(row=3, column=1)
txtCheeseBurger = Entry(f1aa, font=('sans', 16, 'bold'), bd=1, bg="steel blue", width=6, justify='left', textvariable=E_CheeseBurger,
                      state=NORMAL)
txtCheeseBurger.grid(row=4, column=1)
txtMacNuggets = Entry(f1aa, font=('sans', 16, 'bold'), bd=1, bg="steel blue", width=6, justify='left', textvariable=E_MacNuggets
                          , state=NORMAL)
txtMacNuggets.grid(row=5, column=1)
txtMacPuff = Entry(f1aa, font=('sans', 16, 'bold'), bd=1, bg="steel blue", width=6, justify='left',
                           textvariable=E_MacPuff, state=NORMAL)
txtMacPuff.grid(row=6, column=1)
txtChickenWings = Entry(f1aa, font=('sans', 16, 'bold'), bd=1, bg="steel blue", width=6, justify='left',
                           textvariable=E_ChickenWings, state=NORMAL)
txtChickenWings.grid(row=7, column=1)

# ====================================== Drink Widgets ===================================================

txtCoffee_Cake = Entry(f1ab, font=('sans', 16, 'bold'), bd=1, bg="steel blue", width=6, justify='left',
                       textvariable=E_Coffee_Cake, state=NORMAL)
txtCoffee_Cake.grid(row=0, column=1)
txtRed_Valet_Cake = Entry(f1ab, font=('sans', 16, 'bold'), bd=1, bg="steel blue", width=6, justify='left',
                          textvariable=E_Red_Velvet_Cake, state=NORMAL)
txtRed_Valet_Cake.grid(row=1, column=1)
txtBlack_Forest_Cake = Entry(f1ab, font=('sans', 16, 'bold'), bd=1, bg="steel blue", width=6, justify='left',
                             textvariable=E_Black_Forest, state=NORMAL)
txtBlack_Forest_Cake.grid(row=2, column=1)
txtBoston_Cream_Cake = Entry(f1ab, font=('sans', 16, 'bold'), bd=1, bg="steel blue", width=6, justify='left',
                             textvariable=E_Boston_Cream_Cake, state=NORMAL)
txtBoston_Cream_Cake.grid(row=3, column=1)
txtLatta = Entry(f1ab, font=('sans', 16, 'bold'), bd=1, bg="steel blue", width=6, justify='left',
                                textvariable=E_Latta, state=NORMAL)
txtLatta.grid(row=4, column=1)
txtCoke = Entry(f1ab, font=('sans', 16, 'bold'), bd=1, bg="steel blue", width=6, justify='left',
                                 textvariable=E_Coke, state=NORMAL)
txtCoke.grid(row=5, column=1)
txtPepsi = Entry(f1ab, font=('sans', 16, 'bold'), bd=1, bg="steel blue", width=6, justify='left',
                             textvariable=E_Pepsi, state=NORMAL)
txtPepsi.grid(row=6, column=1)
txtCappuccino = Entry(f1ab, font=('sans', 16, 'bold'), bd=1, bg="steel blue", width=6, justify='left',
                           textvariable=E_Cappuccino, state=NORMAL)
txtCappuccino.grid(row=7, column=1)

# =========================== Receipt Box ====================================================

lblReceipt = Label(ft2, font=('sans', 12, 'bold'), text="Receipt                                                                                                                  ", bd=1, bg="steel blue", anchor='w')
lblReceipt.grid(row=0, column=0, sticky=W)
txtReceipt = Text(ft2, width=59, height=22, bg="grey", bd=1, font=('sans', 11, 'bold'))
txtReceipt.grid(row=1, column=0, sticky=W+E)

# ======================= left side outputs ==================================================

lblCostofFood = Label(f2aa, font=('sans', 16, 'bold'), fg="red", text="Cost of Food", bd=1)
lblCostofFood.grid(row=2, column=0, sticky=W)
txtCostofFood = Entry(f2aa, font=('sans', 16, 'bold'), bd=1, justify="left", textvariable=CostofFood)
txtCostofFood.grid(row=2, column=1)

lblCostofCakesandDrinks = Label(f2aa, font=('sans', 16, 'bold'), fg="red", text="Drinks", bd=1)
lblCostofCakesandDrinks.grid(row=3, column=0, sticky=W)
txtCostofCakesandDrinks = Entry(f2aa, font=('sans', 16, 'bold'), bd=1, justify="left", textvariable=CostofCakesandDrinks)
txtCostofCakesandDrinks.grid(row=3, column=1, sticky=W)

lblServiceCharge = Label(f2aa, font=('sans', 16, 'bold'), fg="red", text="Service Charge", bd=1)
lblServiceCharge.grid(row=4, column=0, sticky=W)
txtServiceCharge = Entry(f2aa, font=('sans', 16, 'bold'), bd=1, justify="left", textvariable=ServiceCharge)
txtServiceCharge.grid(row=4, column=1, sticky=W)

# ===================Right side outputs===================================================

lblPaidTax = Label(f2ab, font=('sans', 16, 'bold'),fg="red", text="Tax", bd=1)
lblPaidTax.grid(row=2, column=0, sticky=W)
txtPaidTax = Entry(f2ab, font=('sans', 16, 'bold'),  bd=1, justify="left", textvariable=PaidTax)
txtPaidTax.grid(row=2, column=1, sticky=W)

lblSubTotal = Label(f2ab, font=('sans', 16, 'bold'), fg="red", text="Sub Total", bd=1)
lblSubTotal.grid(row=3, column=0, sticky=W)
txtSubTotal = Entry(f2ab, font=('sans', 16, 'bold'), bd=1, justify="left", textvariable=SubTotal)
txtSubTotal.grid(row=3, column=1, sticky=W)

lblTotalCost = Label(f2ab, font=('sans', 16, 'bold'), fg="red", text="Total", bd=1)
lblTotalCost.grid(row=4, column=0, sticky=W)
txtTotalCost = Entry(f2ab, font=('sans', 16, 'bold'), bd=1, justify="left", textvariable=TotalCost)
txtTotalCost.grid(row=4, column=1, sticky=W)


# ==========Buttons===================================================

btnTotal = Button(fb2, padx=16, pady=1, bd=4, fg="red", font=('sans', 16, 'bold'), width=5,
                  text="Total", command=CostofItems).grid(row=0, column=0, sticky=W+E+N+S)
btnReceipt = Button(fb2, padx=16, pady=1, bd=4, fg="red", font=('sans', 16, 'bold'), width=5,
                    text="Receipt", command=Receipt).grid(row=0, column=1, sticky=W+E+N+S)
btnReset = Button(fb2, padx=16, pady=1, bd=4, fg="red", font=('sans', 16, 'bold'), width=5,
                  text="Reset", command=Reset).grid(row=0, column=2, sticky=W+E+N+S)
btnSave = Button(fb2, padx=16, pady=1, bd=4, fg="red", font=('sans', 16, 'bold'), width=5,
                  text="Save", command=Save).grid(row=0, column=3, sticky=W+E+N+S)
btnExit = Button(fb2, padx=16, pady=1, bd=4, fg="red", font=('sans', 16, 'bold'), width=5,
                 text="Exit", command=qExit).grid(row=0, column=4, sticky=W+E+N+S)




root.mainloop()