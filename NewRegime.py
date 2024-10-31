## Script to calculate the total tax according to the new Regime

# Below are the tax slabs
# Amount (Rs)                                         Tax rate (%)
# From 0 to 3,00,000                                 0
# From 3,00,001 to 6,00,000                 5
# From 6,00,001 to 9,00,000               10
# From 9,00,001 to 12,00,000             15
# From 12,00,001 to 15,00,000          20
# From 15,00,001 and above              30

TS1 = 300000
TS2 = 600000
TS3 = 900000
TS4 = 1200000
TS5 = 1500000
Standard_Deduction = 50000

Annual_Income = float(input("Enter your annual income: "))

Taxable_Income = Annual_Income - Standard_Deduction

Tax = 0
if Taxable_Income <= TS1:
    print("Hurrah! No income tax applicable to you")
    exit()
elif Taxable_Income <= TS2:
    Taxable_Income = Taxable_Income - TS1
    Tax = Taxable_Income * 0.05
elif Taxable_Income <= TS3:
    Taxable_Income = Taxable_Income - TS2
    Tax = 15000
    Tax = Tax + Taxable_Income * 0.10
elif Taxable_Income <= TS4:
    Taxable_Income = Taxable_Income - TS3
    Tax = 45000
    Tax = Tax + Taxable_Income * 0.15
elif Taxable_Income <= TS5:
    Taxable_Income = Taxable_Income - TS4
    Tax = 90000
    Tax = Tax + Taxable_Income * 0.20
else:
    Taxable_Income = Taxable_Income - TS5
    Tax = 150000
    Tax = Tax + Taxable_Income * 0.30

# 4% of the total tax is added as Education cess by the Govt.
Tax = Tax + Tax * 0.04

print ("Your total tax applicable is - " + str(Tax) + " INR")
