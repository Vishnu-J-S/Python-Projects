print("Hello there! Had a meal  in a fancy restraunt, did you?")
bill = float ( input ( "What was the total bill? $" ) )
tip = int ( input ("How generous do you wish to be to the poor waiter(in percentage),10 12 or 15? " ) )
people = int ( input ( "How many fine people dined with you? " ) )
tip_1 = float ( tip/100 + 1 )
pay = ( bill * tip_1 ) / people
r_pay = "{:.2f}".format( pay )
print ( f"Make sure everyone pays: ${r_pay}")