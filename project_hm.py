import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#P_dir={"Patient_ID","Name","Father's name","Disease","Date of admission","Gender","Age","Address","Phone no.","Date of birth","Current medical history","Blood group","Email","Tests done","Consultant doctor","Reference doctor","Pateint type","Room no.","Payment method"}

#D_dir={"Doctor_ID","Doctor's name","Father's /husband's name","Gender","Department","Martial status","Consultation day","Consultation time from","Consultation time to","Address","Contact no.","Emergency no.","Age","Total pateints","Date of joining","Assistant doctor","Education","O.T days","Fees"}

#S_dir={"Staff_ID","Name of staff member","Father's Name","Gender","Phone no.","Doctor","Address","Education","Age","Fee"}

df=pd.read_csv("F:\\Book1 (1).csv")
print("WELCOME TO HOSPITAL MANAGEMENT SYSTEM IN PYTHON")
PID=input("Enter the id of Patient/Doctor/Staff :").upper()
if (df['Patient_ID'].isin([PID]).any()):
	df.set_index("Patient_ID", inplace=True)
	if (PID[0]=='D'):
		df=df.rename(columns =df.loc['Doctor_ID'])
		print(df.loc[PID])
	elif (PID[0]=='S'):
		df=df.rename(columns =df.loc['Staff_ID'])
		print(df.loc[PID,"Name of staff member":"Fee"])
	else:
		
		print(df.loc[PID])

	
else:
	print("Invalid ID")
	
print("TO GENERATE BILLS USE THIS MODULE :" )
def Biling():
        print("\t\t\t\tFINAL INVOICE")
a=print("BED CHARGES:-")
b=int(input("multibed/simplebed:"))
c=print("diagnostics and investigations:-")
d=int(input("liver function test:"))
e=int(input("complete hemogram:"))
f=int(input("glucose random:"))
print("-"*65)
g=print("DOCTOR CHARGES:-")
h=int(input("doctor visit charges(1st visit):"))
i=int(input("doctor visit charges(2nd visit):"))
j=int(input("doctor visit charges(3rd visit):"))
print("-"*65)
k=print("DRUGS:-")
l=int(input("water for injection:"))
m=int(input("pantodac injection:"))
n=int(input("emeset injection:"))
o=int(input("DNS infusion:"))
p=int(input("pantodac infection:"))
import datetime
now=datetime.datetime.now()
dtm=str(now)
item=("item no.: 16")
price=b+d+e+f+h+i+j+l+m+n+o+p
print("-"*65)

print("-"*65)
print()
print("date:{0:>55s}".format(dtm))
print("-"*65)
print("item\t\t\tunit price\t")
print("-"*65)
print("{0:<25s}".format(item),end="")
print("{0:>7.2f}".format(price),end="")
print()
print("-"*65)
print("total:{0:>46.2f} Rs".format(price))

print("TO GENERATE RECEIPTS USE THIS MODULE:")
def receipt():
        a=input("patient name:")
b=input("gender:")
c=int(input("age:"))
d=int(input("receipt no.:"))
e=input("receipt date:")
import datetime
now=datetime.datetime.now()
dtm=str(now)
paytype=input("pay type:")
cheque=int(input("cheque/card no.:"))
bankname=input("bank name:")
amount=int(input("amount:"))
tax=amount*0.5
net=amount+tax
print("-"*65)
print("\t\t\t\t RECEIPT")
print("-"*65)
print()
print("date:{0:>55s}".format(dtm))
print("-"*65)
print("paytype\t\t\tcheque\tbankname\tamount")
print("-"*65)
print("{0:<25s}".format(paytype),end="")
print("{0:>7.2f}".format(cheque),end="")
print("{0:10s}".format(bankname),end="")
print("{0:14.2f}".format(amount))
print()
print()
print("tax:{0:>57.2f}".format(tax))
print("-"*65)
print("amount payable:{0:>46.2f}".format(net))

print("GRAPH OF DISEASE AND OUR SPECIALIZATION IN ITS TREATMENT: ")
def Matplotlib():
        import numpy as np
import matplotlib.pyplot as plt
objects=('cancer','heart disease','typhoid','jaundice','malaria','dengue')
y_pos=np.arange(len(objects))
performance=[3,2,2,1,1,1]
plt.barh(y_pos,performance,align='center',color='b')
plt.yticks(y_pos,objects)
plt.xlabel('number of patients')
plt.title('disease frequency chart')
plt.show()

        


df.to_csv("F:\\Book1 (1).csv")
