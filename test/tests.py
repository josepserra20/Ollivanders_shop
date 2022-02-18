

def gettests(itemName):

    items = []
    with open ("C:/Users/josep/Escritorio/python/Ollivanders_shop/test/test.txt","r") as tests:
        for line in tests:
            if line.find(itemName) != -1:
                items.append(line.rstrip('\n'))

        return items

def settest():
    items = gettests('itemName')
    
    for brie in items:

        


            
          
                

    

