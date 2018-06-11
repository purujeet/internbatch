class odd():
    def __init__(self,m=0):
        self.m=m

    def __iter__(self):
        self.n =1
        return self
    def __next__(self):
        self.n+=2
        return self.n


       
            

        

