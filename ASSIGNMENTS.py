customers=[("sana",1000,5,2),("arez",1200,6,3),("kaif",1500,7,4)]
for customer in customers:
    name,principle,rate,time=customer 
    
    simple_interest=principle*rate*time/100
    final_interest=principle+simple_interest

    compound_interest=principle*(1+rate/100)*time-principle
    final_com_interest=principle+compound_interest

    print("Customer Name: ",name)
    print("Principle Amount: ",principle)
    print("Simple Interest:  ",simple_interest)
    print("Final Simple Interest: ",final_interest)
    print("Compound Interest: ",compound_interest)
    print("Final Compound Interest: ",final_com_interest)
    print("--------------------------------------------")   