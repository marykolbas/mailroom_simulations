

class Package:
    def __init__(self,id,letter,bin,size = "small"):
        self.id = id
        self.size = size
        self.letter = letter
        self.bin = bin
    
    def getID(self):
        return self.id
    

    def getSize(self):
        return self.size
    
    def getLetter(self):
        return self.letter
    
    def getBin(self):
        return self.bin
    
    def __str__(self):
        return f"ID: {self.id} | {self.size}"

    

class Bin:
    packages = []
    def __init__(self,label):
        self.label = label
    
    def addPackage(self,package):
        self.packages.add(package)
    
    def removePackage(self,package):
        self.packages.remove(package)
    
    def getPackages(self):
        return self.packages
    



