class Inbalance(Exception):
    def __init__(self,msg):
        print("inside constructor")
        self.msg = msg
        
      
def withdrawl(amount):
    bal = 500
    if bal>amount:
        print("take it")
    else:
        # print("not enough balance")
        try:
            raise Inbalance("balance is low ")
        except Inbalance as err:
            print("Inside exception")
            print(err)
    
withdrawl(5000)


