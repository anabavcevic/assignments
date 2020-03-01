class Account:
    __accountID=101
    __type = "Loan Account"
    __balance = 50.00
 
    def PrintBalance (self):
        print("Account " + str(self.__accountID) + " has a current balance of : "+ str(self.__balance))
        
v=Account()

v.PrintBalance( )