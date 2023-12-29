# creating a vending
print("""      __       __          __               __              __ 
\  / |_  |\ | |  \ | |\ | / _    |\/|  /\  /   |__| | |\ | |_  
 \/  |__ | \| |__/ | | \| \__)   |  | /--\ \__ |  | | | \| |__ 
                                                               """)

print("GREETINGS!")
print("______________________________")
print("STEP INTO THE AMAZING VEND-O-WORLD")
print("......................................................................................")
print("[Simulation of a Vending Machine]")
print("-------------------------------")



#Codes representing Items in the Store
items={
   'A1' : 'CKERS BSNIAR' , 
   'B2' : 'CHOLATE CHIP' , 
   'C3' : 'BLUEBERRY CRISP' , 
   'D4' : 'POP-TARTS' , 
   'E5' : 'SUN CHIPS' , 
   'F6' : 'DORITOS' , 
   'G7' : 'PRETZELS' , 
   'H8' : 'WATER BOTTLE' , 
   'I9' : 'ENERGY DRINK' ,
   'J10' : 'COLD COFFE' , 
   'K11' : 'VITAMIN WATER' , 
   'L12' : 'SODA' , 
   'M13' : 'MOUNTAIN DEW' ,
   'N14' : 'COKE' ,
   'O15' : 'ICED TEA' , 


}

print("SnackShop MENU")
print("...........................................................................")
print("1. SNICKERS BAR                   AED 330 ,      Code: A1 ,         Stock:150")
print("2. CHOLATE CHIP                   AED 270 ,      Code: B2 ,         Stock:200")
print("3. BLUEBERRY CRISP                AED 215 ,      Code: C3 ,         Stock:30 ")
print("4. POP-TARTS                      AED 100 ,      Code: D4 ,         Stock:100")
print("5. SUN CHIPS                      AED 150 ,      Code: E5 ,         Stock:250")
print("6. DORITOS                        AED 160 ,      Code: F6 ,         Stock:90")
print("7. PRETZELS                       AED 120 ,      Code: G7 ,         Stock:220")
print("         ...THE DRINKS MENU...    ")
print("8. WATER BOTTLE                 AED 100 ,      Code: H8 ,          Stock:220")
print("9. ENERGY DRINK                 AED 220 ,      Code: I9 ,          Stock:150")
print("10. COLD COFFE                  AED 350 ,      Code: J10 ,         Stock:90")
print("11. VITAMIN WATER               AED 110 ,      Code: K11 ,         Stock:240")
print("12. SODA                        AED 235 ,      Code: L12 ,         Stock:360")
print("13. MOUNTAIN DEW                AED 160 ,      Code: M13 ,         Stock:95")
print("14. COKE                        AED 145 ,      Code: N14 ,         Stock:125")
print("15. ICED TEA                    AED 340 ,      Code: O15 ,         Stock:160")   
print("............................................................................")

#The cost of things in the Store
SNICKERSBAR=330
CHOLATECHIP=270
BLUEBERRYCRISP=215
POPTARTS=100
SUNCHIPS=150
DORITOS=160
PRETZELS=120
WATERBOTTLE=100
ENERGYDRINK=220
COLDCOFFE=350
VITAMINWATER=110
SODA=235
MOUNTAINDEW=160
COKE=145
ICEDTEA=340

# Check the Inventory Status
inventory_quantity = 3000
if inventory_quantity > 0:
    print("________________________")
    print("Thank you for visiting our Vending Emporium.!")
    print("Discover a wide range of tasty snacks and pleasant beverages.")
    print("_______________________")



# Flavour Gateway Unlock      
chosen_code = input('Enter the Product Code of your selected delight to begin your flavour adventure:')

# Start a Delicious Transaction
inserted_amount = int(input("Congratulations on your decision! Please deposit the necessary cash"))



# Request Information on a Different Item and Make Suggestions
additional_choice = {
   '1': 'yes, please.' ,
   '2': 'no, thankyou.'
}
# Inquiry About a Different Item with Suggestions
suggestion_response = input('Do you want to try something new? (Sure/no thank you):')
if suggestion_response == 'sure':
   chosen_code = input("Enter the iteam code you wish to buy: ")

   inserted_amount = float(input("Enter the total amount of money you wish to deposit: $"))
   print("Thank you very much for your payment. Have a good time with your buy!")

elif suggestion_response == 'no thank you':
   print("Thank you for making this selection. Enjoy your chosen delicacies!")

   # Receiving and Returning SNICKERSBAR Change
if chosen_code == 'A1':
    if inserted_amount >= SNICKERSBAR:
        change = inserted_amount - SNICKERSBAR
        print("*******************************************")
        print("              SNICKERS DELICIOUS              ")
        print("-------------------------------------------")
        print("Amount Paid:           AED", inserted_amount)
        print("Item Cost (SNICKERS):  AED", SNICKERSBAR)
        print("-------------------------------------------")
        print("Change Returned:        AED", change)
        print("-------------------------------------------")
        print("      Thank you for deciding on SNICKERS!     ")
        print("  Your SNICKERS have been delivered. Enjoy!")
        print("         Have a wonderful day!")
        print("*******************************************")
        print("       Please come back! Goodbye!")
    else:
        print("*******************************************")
        print("   Insufficient Balance! Refund of funds    ")
        print("     Please accept our apologies for the inconvenience.")
        print("   Feel free to experiment with other delectable delicacies!")
        print("*******************************************")
        print("       Please Visit Again! Goodbye!")



         # Processing and Returning Change for CHOCOLATE CHIP
if chosen_code == 'B2':
    if inserted_amount >= CHOLATECHIP:
        change = inserted_amount - CHOLATECHIP
        print("*******************************************")
        print("           CHOCOLATE CHIP DELICIOUS           ")
        print("-------------------------------------------")
        print("Amount Paid:            AED", inserted_amount)
        print("Item Cost (CHOCOLATE CHIP):  AED", CHOLATECHIP)
        print("-------------------------------------------")
        print("Change Returned:         AED", change)
        print("-------------------------------------------")
        print("    Thank you for deciding on CHOCOLATE CHIP!  ")
        print(" Your CHOCOLATE CHIP have been delivered. Enjoy!")
        print("          Have a chocolaty day ahead!")
        print("*******************************************")
        print("       Please Visit Again! Goodbye!")
    else:
        print("*******************************************")
        print("   Insufficient Balance! Refund of funds    ")
        print("      Please accept our apologies for the inconvenience.")
        print("    Feel free to try other delicious treats!")
        print("*******************************************")
        print("       Please Visit Again! Goodbye!")




        # Processing and Returning Change for BLUEBERRY CRISP
if chosen_code == 'C3':
    if inserted_amount >= BLUEBERRYCRISP:
        change = inserted_amount - BLUEBERRYCRISP
        print("*******************************************")
        print("           BLUEBERRY CRISP DELICIOUS          ")
        print("-------------------------------------------")
        print("Amount Paid:           AED", inserted_amount)
        print("Item Cost (BLUEBERRY CRISP):  AED", BLUEBERRYCRISP)
        print("-------------------------------------------")
        print("Change Returned:        AED", change)
        print("-------------------------------------------")
        print("  Thank you for choosing BLUEBERRY CRISP!  ")
        print(" Your BLUEBERRY CRISP has been dispensed. Enjoy!")
        print("         Have a fruity day ahead!")
        print("*******************************************")
        print("       Please Visit Again! Goodbye!")
    else:
        print("*******************************************")
        print("   Insufficient Balance! Money Refunded    ")
        print("      Apologies for the inconvenience.")
        print("    Feel free to try other delicious treats!")
        print("*******************************************")
        print("       Please Visit Again! Goodbye!")


        # Calculating and Returning the Correct Change Of POPTARTS
if chosen_code == 'D4':
    if inserted_amount >= POPTARTS:
        change = inserted_amount - POPTARTS
        print("*******************************************")
        print("           WARM AND TOASTY POPTARTS          ")
        print("-------------------------------------------")
        print("Amount Paid:           AED", inserted_amount)
        print("Item Cost (POPTARTS):  AED", POPTARTS)
        print("-------------------------------------------")
        print("Change Returned:        AED", change)
        print("-------------------------------------------")
        print("  Thank you for choosing POPTARTS!  ")
        print(" Your POPTARTS has been dispensed. Enjoy!")
        print("         Have a delightful day ahead!")
        print("*******************************************")
        print("       Please Visit Again! Goodbye!")
    else:
        print("*******************************************")
        print("   Insufficient Balance! Money Refunded    ")
        print("      Apologies for the inconvenience.")
        print("    Feel free to try other delicious treats!")
        print("*******************************************")
        print("       Please Visit Again! Goodbye!")



        # Calculating and reporting the correct SUNCHIP change
if chosen_code == 'E5':
    if inserted_amount >= SUNCHIPS:
        change = inserted_amount - SUNCHIPS
        print("*******************************************")
        print("        CRUNCHY GOODNESS UNLEASHED!        ")
        print("-------------------------------------------")
        print("Amount Paid:           AED", inserted_amount)
        print("Item Cost (SUNCHIPS):   AED", SUNCHIPS)
        print("-------------------------------------------")
        print("Change Returned:        AED", change)
        print("-------------------------------------------")
        print("  Thank you for choosing SUNCHIPS!  ")
        print(" Your SUNCHIPS has been dispensed. Enjoy!")
        print("         Have a delightful day ahead!")
        print("*******************************************")
        print("       Please Visit Again! Goodbye!")
    else:
        print("*******************************************")
        print("   Insufficient Balance! Money Refunded    ")
        print("      Apologies for the inconvenience.")
        print("    Feel free to try other delicious treats!")
        print("*******************************************")
        print("       Please Visit Again! Goodbye!")



         # DORITOS Change Calculation and Return
if chosen_code == 'F6':
    if inserted_amount >= DORITOS:
        change = inserted_amount - DORITOS
        print("*******************************************")
        print("         UNLEASH THE DORITOS DELIGHT!       ")
        print("-------------------------------------------")
        print("Amount Paid:           AED", inserted_amount)
        print("Item Cost (DORITOS):   AED", DORITOS)
        print("-------------------------------------------")
        print("Change Returned:        AED", change)
        print("-------------------------------------------")
        print("  Thank you for choosing DORITOS!  ")
        print("  Your DORITOS has been dispensed. Enjoy!")
        print("         Have a flavorful day ahead!")
        print("*******************************************")
        print("       Please Visit Again! Goodbye!")
    else:
        print("*******************************************")
        print("   Insufficient Balance! Money Refunded    ")
        print("      Apologies for the inconvenience.")
        print("    Feel free to try other delicious treats!")
        print("*******************************************")
        print("       Please Visit Again! Goodbye!")




        # Calculating and Returning the Correct PRETZEL Change
if chosen_code == 'G7':
    if inserted_amount >= PRETZELS:
        change = inserted_amount - PRETZELS
        print("*******************************************")
        print("           INDULGE IN CRISPY PRETZELS       ")
        print("-------------------------------------------")
        print("Amount Paid:            AED", inserted_amount)
        print("Item Cost (PRETZELS):   AED", PRETZELS)
        print("-------------------------------------------")
        print("Change Returned:         AED", change)
        print("-------------------------------------------")
        print("  Thank you for choosing PRETZELS!")
        print("  Your PRETZELS has been dispensed. Enjoy!")
        print("         Have a crunchy day ahead!")
        print("*******************************************")
        print("       Please Visit Again! Goodbye!")
    else:
        print("*******************************************")
        print("   Insufficient Balance! Money Refunded    ")
        print("      Apologies for the inconvenience.")
        print("    Feel free to try other delicious treats!")
        print("*******************************************")
        print("       Please Visit Again! Goodbye!")



        # Calculating and reporting the correct water bottle change
if chosen_code == 'H8':
    if inserted_amount >= WATERBOTTLE:
        change = inserted_amount - WATERBOTTLE
        print("*******************************************")
        print("      STAY HYDRATED WITH WATER BOTTLE      ")
        print("-------------------------------------------")
        print("Amount Paid:            AED", inserted_amount)
        print("Item Cost (WATER BOTTLE): AED", WATERBOTTLE)
        print("-------------------------------------------")
        print("Change Returned:         AED", change)
        print("-------------------------------------------")
        print("  Thank you for choosing WATER BOTTLE!")
        print(" Your WATER BOTTLE has been dispensed. Enjoy!")
        print("         Stay refreshed and have a great day!")
        print("*******************************************")
        print("       Please Visit Again! Goodbye!")
    else:
        print("*******************************************")
        print("   Insufficient Balance! Money Refunded    ")
        print("      Apologies for the inconvenience.")
        print("    Feel free to explore other delightful options!")
        print("*******************************************")
        print("       Please Visit Again! Goodbye!")



        # Calculating and reporting the correct ENERGY DRINK change
if chosen_code == 'I9':
    if inserted_amount >= ENERGYDRINK:
        change = inserted_amount - ENERGYDRINK
        print("*******************************************")
        print("      BOOST YOUR ENERGY WITH ENERGY DRINK  ")
        print("-------------------------------------------")
        print("Amount Paid:              AED", inserted_amount)
        print("Item Cost (ENERGY DRINK): AED", ENERGYDRINK)
        print("-------------------------------------------")
        print("Change Returned:           AED", change)
        print("-------------------------------------------")
        print("  Thank you for choosing ENERGY DRINK!")
        print(" Your ENERGY DRINK has been dispensed. Enjoy!")
        print("   Stay energized and have a productive day!")
        print("*******************************************")
        print("       Please Visit Again! Goodbye!")
    else:
        print("*******************************************")
        print("   Insufficient Balance! Money Refunded    ")
        print("      Apologies for the inconvenience.")
        print("    Feel free to explore other delightful options!")
        print("*******************************************")
        print("       Please Visit Again! Goodbye!")


         # Calculating and Returning the Correct Cold Coffee Change
if chosen_code == 'J10':
    if inserted_amount >= COLDCOFFE:
        change = inserted_amount - COLDCOFFE
        print("*******************************************")
        print("         CHILL OUT WITH COLD COFFEE        ")
        print("-------------------------------------------")
        print("Amount Paid:            AED", inserted_amount)
        print("Item Cost (COLD COFFEE): AED", COLDCOFFE)
        print("-------------------------------------------")
        print("Change Returned:         AED", change)
        print("-------------------------------------------")
        print("    Thank you for choosing COLD COFFEE!")
        print("Your COLD COFFEE has been dispensed. Enjoy!")
        print("  Sip, relax, and have a refreshing time!")
        print("*******************************************")
        print("      Please Visit Again! Goodbye!")
    else:
        print("*******************************************")
        print("  Insufficient Balance! Money Refunded    ")
        print("     Apologies for the inconvenience.")
        print("   Feel free to explore other delightful options!")
        print("*******************************************")
        print("      Please Visit Again! Goodbye!")




       # Calculating and reporting the correct VITAMIN WATER change
if chosen_code == 'K11':
    if inserted_amount >= VITAMINWATER:
        change = inserted_amount - VITAMINWATER
        print("*******************************************")
        print("         RECHARGE WITH VITAMIN WATER        ")
        print("-------------------------------------------")
        print("Amount Paid:               AED", inserted_amount)
        print("Item Cost (VITAMIN WATER): AED", VITAMINWATER)
        print("-------------------------------------------")
        print("Change Returned:            AED", change)
        print("-------------------------------------------")
        print("    Thank you for choosing VITAMIN WATER!")
        print("Your VITAMIN WATER has been dispensed. Enjoy!")
        print("  Stay hydrated and refreshed!")
        print("*******************************************")
        print("      Please Visit Again! Goodbye!")
    else:
        print("*******************************************")
        print("  Insufficient Balance! Money Refunded    ")
        print("     Apologies for the inconvenience.")
        print("   Feel free to explore other delightful options!")
        print("*******************************************")
        print("      Please Visit Again! Goodbye!")



       # Calculating and reporting the correct SODA change
if chosen_code == 'L12':
    if inserted_amount >= SODA:
        change = inserted_amount - SODA
        print("*******************************************")
        print("              SAVOR THE SODA                ")
        print("-------------------------------------------")
        print("Amount Paid:               AED", inserted_amount)
        print("Item Cost (SODA):           AED", SODA)
        print("-------------------------------------------")
        print("Change Returned:            AED", change)
        print("-------------------------------------------")
        print("       Thank you for choosing SODA!")
        print("Your SODA has been dispensed. Enjoy the fizz!")
        print("  Refresh yourself with the coolness!")
        print("*******************************************")
        print("      Please Visit Again! Goodbye!")
    else:
        print("*******************************************")
        print("  Insufficient Balance! Money Refunded    ")
        print("     Apologies for the inconvenience.")
        print("   Feel free to explore other delightful options!")
        print("*******************************************")
        print("      Please Visit Again! Goodbye!")


       # Calculating and reporting the correct MOUNTAINDEW change
if chosen_code == 'M13':
    if inserted_amount >= MOUNTAINDEW:
        change = inserted_amount - MOUNTAINDEW
        print("*******************************************")
        print("           ENJOY THE MOUNTAIN DEW          ")
        print("-------------------------------------------")
        print("Amount Paid:               AED", inserted_amount)
        print("Item Cost (MOUNTAIN DEW):   AED", MOUNTAINDEW)
        print("-------------------------------------------")
        print("Change Returned:            AED", change)
        print("-------------------------------------------")
        print("      Thank you for choosing MOUNTAIN DEW!")
        print("Your MOUNTAIN DEW has been dispensed. Stay refreshed!")
        print("    Awaken your senses with the citrus burst!")
        print("*******************************************")
        print("      Please Visit Again! Goodbye!")
    else:
        print("*******************************************")
        print("  Insufficient Balance! Money Refunded    ")
        print("     Apologies for the inconvenience.")
        print("   Feel free to explore other delightful options!")
        print("*******************************************")
        print("      Please Visit Again! Goodbye!")

         



       # Calculating and reporting the correct COKE change
if chosen_code == 'N14':
    if inserted_amount >= COKE:
        change = inserted_amount - COKE
        print("*******************************************")
        print("          REFRESHING COCA-COLA             ")
        print("-------------------------------------------")
        print("Amount Paid:               AED", inserted_amount)
        print("Item Cost (COCA-COLA):      AED", COKE)
        print("-------------------------------------------")
        print("Change Returned:            AED", change)
        print("-------------------------------------------")
        print("     Thank you for choosing COCA-COLA!")
        print("Your COCA-COLA has been dispensed. Enjoy the fizz!")
        print("  Open happiness and share the joy of COKE!")
        print("*******************************************")
        print("      Please Visit Again! Goodbye!")
    else:
        print("*******************************************")
        print("  Insufficient Balance! Money Refunded    ")
        print("     Apologies for the inconvenience.")
        print("   Feel free to explore other delightful options!")
        print("*******************************************")
        print("      Please Visit Again! Goodbye!")



 # Calculating and reporting the correct ICEDTEA change
if chosen_code == 'O15':
    if inserted_amount >= ICEDTEA:
        change = inserted_amount - ICEDTEA
        print("*******************************************")
        print("       ICED DELIGHT - PEACH ICED TEA        ")
        print("-------------------------------------------")
        print("Amount Paid:               AED", inserted_amount)
        print("Item Cost (PEACH ICED TEA): AED", ICEDTEA)
        print("-------------------------------------------")
        print("Change Returned:            AED", change)
        print("-------------------------------------------")
        print("    Thank you for choosing PEACH ICED TEA!")
        print("Your PEACH ICED TEA has been dispensed. Enjoy the coolness!")
        print("     Sip, relax, and savor the refreshing taste!")
        print("*******************************************")
        print("      Please Visit Again! Goodbye!")
    else:
        print("*******************************************")
        print("  Insufficient Balance! Money Refunded    ")
        print("     Apologies for the inconvenience.")
        print("   Feel free to explore other delightful options!")
        print("*******************************************")
        print("      Please Visit Again! Goodbye!")


