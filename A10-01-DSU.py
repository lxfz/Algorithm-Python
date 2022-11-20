class DSU:
    
    def __init__(self, n) -> None:
        self.father = [i for i in range(n+1)]
        self.ans = 0;

    def find(self, x):
        if(self.father[x] != x):
            self.father[x] = self.find(self.father[x])
            
        return self.father[x]
    
    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y) 
        if(fx == fy):
            self.ans+=1
        else:
            self.father[fx] = fy

