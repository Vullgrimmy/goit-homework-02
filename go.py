


def format_ingredients(items):
        if len(items) == 0:
                return('')
        if len(items) == 1:
                return(items[0])
        # items.insert(-1, ' and ')
        stroka = ', '.join(items[:-1]) #+' and '+items[-1]
        a= items[:-1]
        # lenght = len(items)-1
        # recept_2 = items[1:lenght:]
        # stroka = items[0]
        
        # for a in recept_2:
        #          stroka = stroka + ", " + a 
        # stroka = stroka +" and " + items[-1]         
        return(stroka)
recept = ["2 eggs", "1 liter sugar"]

format_ingredients(recept)