class power():
    def __init__(self,n=0,m=0):
        self.m=m
        self.n=n

    def __iter__(self):
        self.s=0
        return self
    def __next__(self):
      
        if self.s<=self.m:
            num=self.n**self.s
        else:
            raise StopIteration
        self.s+=1

        return num
        



       
            

        

