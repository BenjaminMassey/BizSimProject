## BizSim Project
## By Benjamin Massey
## Written in Python 3.3.0

# Inform the Player of Rules and Theoretical Last Quarter
print("You have inherited a business and now must run it. You will decide how much money to put into each category, changing the outcome of how your company will perform. You will determine the price, Production, Total Quality Management and Advertisement of your company. Total Quality Management will determine how much your Product will cost to make per unit, the more money you put in the less it will cost to make that Product. The more you add into Advertising, the more units you will sell. Think it through well.\nLast Quarter, you sold a total of 15,000 units at $35. You spent 100,000 in both Total Quality Management and in Advertisement. You currently have 100,000 in cash and the cost of your Product will be 70% of what you're selling it for. Good Luck\n")

# Set up variables
def set_vars():
    data = dict()
    MaxProd = 20
    data["MaxProd"] = MaxProd
    Cash = 100
    data["Cash"] = Cash
    Quarter = 1
    data["Quarter"] = Quarter
    TotalTQM = 0
    data["TotalTQM"] = TotalTQM
    TotalAds = 0
    data["TotalAds"] = TotalAds
    return data

data = set_vars()

def get_inputs():

    choices = dict()
    print("It is currently Quarter " + str(data["Quarter"]) + "\n")
    Price = int(input("How much will you charge for your Product? Choose a number between 30 and 40 dollars: "))
    if Price < 30 or Price > 40:
        print("You cannot have that price, try again.")
        Price = int(input("Price: "))
        if Price < 30:
            print("We will set your price to 30 dollars since you are having difficulty making correct decisions.")
            Price = 30
        if Price > 40:
            print("We will set your price to 40 dollars since you are having difficulty making correct decisions.")
            Price = 40
    choices["Price"] = Price
    
    print("How many units would you like to Produce? Your current max capacity is at", str(data["MaxProd"]) + ",000 units.")
    Prod = int(input("Units (In Thousands): "))
    if Prod < 0 or Prod > data["MaxProd"]:
        print("You cannot have make that amount, try again.")
        Prod = int(input("Units: "))
        if Prod > 20:
            print("We will set your Production to 20 since you are having difficulty making correct decisions.")
            Prod = 20
        if Prod < 0:
            print("We will set your Production to 0 since you are having difficulty making correct decisions.")
            Prod = 0
    choices["Prod"] = Prod
    
    AddProd = int(input("Would you like to increase your maximum Production? It will cost $1 per extra unit added. Increase amount(thousands): "))
    choices["AddProd"] = AddProd
    data["MaxProd"] = data["MaxProd"] + AddProd
    TQM = int(input("How much will you put into Total Quality Management (TQM)? This will be in thousands, and cannot exceed 200: "))
    if TQM < 0 or TQM > 200:
        print("You cannot have spend that amount, try again.")
        TQM = int(input("TQM: "))
        if TQM > 200:
            print("We will set your TQM to 200 since you are having difficulty making correct decisions.")
            TQM = 200
        if TQM < 0:
            print("We will set your TQM to 0 since you are having difficulty making correct decisions.")
            TQM = 0
    choices["TQM"] = TQM  
    Ads = int(input("How much will you put into Advertising? This will be in thousands, and cannot exceed 200: "))
    if Ads < 0 or Ads > 200:
        print("You cannot have spend that amount, try again.")
        Ads = int(input("Advertising: "))
        if Ads > 200:
            print("We will set your Advertising to 200 since you are having difficulty making correct decisions.")
            Ads = 200
        if Ads < 0:
            print("We will set your Advertising to 0 since you are having difficulty making correct decisions.")
            Ads = 0
    choices["Ads"] = Ads
    return choices

# Calculate the outcome for Quarter
def get_calc(choices):

    calcs = dict()

    data["TotalAds"] = data["TotalAds"] + choices["Ads"]
    AdsBonus = data["TotalAds"] * 0.005
    calcs["AdsBonus"] = AdsBonus
    SoldUnitsTheory = 15 + AdsBonus
    calcs["SoldUnitsTheory"] = SoldUnitsTheory
    if SoldUnitsTheory <= choices["Prod"]:
        SoldUnits = SoldUnitsTheory
    if SoldUnitsTheory > choices["Prod"]:
        SoldUnits = choices["Prod"]
    calcs["SoldUnits"] = SoldUnits
    MissSell = choices["Prod"] - SoldUnitsTheory
    calcs["MissSell"] = MissSell
    costPU = choices["Price"] * 0.7
    calcs["costPU"] = costPU
    profitPU = choices["Price"] - costPU
    calcs["costPU"] = costPU
    profits = (profitPU * SoldUnits) - choices["Ads"] - choices["TQM"] - choices["AddProd"]
    calcs["profits"] = profits
    data["Cash"] = data["Cash"]+ profits
    data["TotalTQM"] = data["TotalTQM"] + choices["TQM"]
    TQMHelp = data["TotalTQM"] * 0.005
    calcs["TQMHelp"] = TQMHelp
    costPU = costPU - TQMHelp
    calcs["costPU"] = costPU
    if MissSell > 0:
        print("\n\nYou sold", str(calcs["SoldUnits"]) + " thousand units with", str(calcs["MissSell"]) + " thousand too many units Produced. Your profits were", str(calcs["profits"]) + " thousand with", str(data["Cash"]) + " thousand in cash now. Cost per unit is now", str(calcs["costPU"]), "per unit. Good luck!\n")
    if MissSell <= 0:
        print("\n\nYou sold", str(calcs["SoldUnits"]) + " thousand units with", str((-1) * calcs["MissSell"]) + " thousand missed selling oppurtunities. Your profits were", str(calcs["profits"]) + " thousand with", str(data["Cash"]) + " thousand in cash now. Cost per unit is now", str(calcs["costPU"]), "per unit. Good luck!\n")
    data["Quarter"] = data["Quarter"] + 1
    if data["Quarter"] == 13:
        print("Your three year game is now over! You ended with", str(data["Cash"]), "thousand dollars in cash, got your cost per unit down to", str(calcs["costPU"]), "and sold", str(calcs["SoldUnits"]), "thousand units your last quarter. Good job! Try again something new, and see if you do better or worse. Thanks for playing.") 
    return calcs


for _ in range(12):
    choices = get_inputs()
    calcs = get_calc(choices)
