class Hello():
    
    def __init__(self,m=0):
        self.m=m
    def __iter__(self):
        self.n=0
        return self
    def __next__(self):
        self.n+=1
        if self.n<=self.m:
            return self.n
        else:
            raise StopIteration


       
            

        

