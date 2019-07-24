##print('--------------------------------WELCOME----------------------------------')
spotName="";
helpLineNo=0;
facilities="";

class PicnicSpot:
    def __init__(self,spotName, helpLineNo, facilities):
        self.spotName=spotName
        self.helpLineNo=helpLineNo
        self.facilities=facilities
        
#    '''def set(self,spotName, helpLineNo, facilities):
#        self.spotName=spotName
#        self.helpLineNo=helpLineNo
#        self.facilities=facilities
#    '''
    
    def show(self):
        print(self.spotName);
        print(self.helpLineNo);
        print(self.facilities);
        
    def __del__(self):
        print('DESTROYED')
        
        
personName="";
class Person(PicnicSpot):
        def __init__(self,personName):
            PicnicSpot.__init__(self,"YAHSWANT DAMS",12345,"YAHA BHI BOHOT HAI");
            #PicnitSpot.set(self,"YAHSWANT DAMS",12345,"YAHA BHI BOHOT HAI");
            self.personName=personName;
            
        def show(self):
            PicnicSpot.show(self);
            print(self.personName);
        
        def __del__(self):
            print('DESTROYED')
            
ref=Person("ANMOL PAL")
ref.show();
del ref;
print('-------------------------------------------------------------------------')







