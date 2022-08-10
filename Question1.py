import decimal 

def give_remainder_dict(divident,divisor,shortitupto):
    floor = divident//divisor       #calculating floor value of divident and divisor
    digits = len(str(floor))        #calculate floor count by converting int into string so that we get it count
    
    decimal.getcontext().prec = shortitupto+digits    #calculating precision upto how much decimal places we want after . 
    division = decimal.Decimal(divident) / decimal.Decimal(divisor);   #get our required result with 10 decimal places after .
    
    list  = []           #created one list
    for s in str(division).split(".")[1]:
        list.append(s)                #appended all the numbers comes after .
    for i in range(0, len(list)):
        list[i] = int(list[i])       #converting that string list into int list
   
    
  
    
    dict = {}           #created a dictionary for storing keys and values

    for each in range(0,10):
        dict.update({each:list.count(each)})        #counting each key upto 0 to 9

    print(dict)      #printing the results 



give_remainder_dict(22,7,10);        #calling the function
#result   {0: 0, 1: 2, 2: 2, 3: 0, 4: 2, 5: 1, 6: 0, 7: 1, 8: 1, 9: 1}

#testcases implementation

give_remainder_dict(22,7,100)
#result {0: 0, 1: 17, 2: 17, 3: 0, 4: 17, 5: 16, 6: 0, 7: 16, 8: 16, 9: 1}

give_remainder_dict(1,3,33)

#result {0: 0, 1: 0, 2: 0, 3: 34, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}


















        
   














            
    
    










