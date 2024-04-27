def convertor(number):
    finalNumber=''
    myNumbers={
    1:'ერთი',
    2:'ორი',
    3:'სამი',
    4:'ოთხი',
    5:'ხუთი',
    6:'ქვსი',
    7:'შვიდი',
    8:'რვა',
    9:'ცხრა',
    10:'ათი',
    11:'თერთმეტი',
    12:'თორმეტი',
    13:'ცამეტი',
    14:'თოთხმეტი',
    15:'თხუთმეტი',
    16:'თექვსმეტი',
    17:'ჩვიდმეტი',
    18:'თვრამეტი',
    19:'ცხრამეტი',
    20:'ოცი',
    40:'ორმოცი',
    60:'სამოცი',
    80:'ოთხმოცი',
    100:'ასი',
    1000000:'მილიონი',
    1000000000:'მილიარდი'
    }

    if number in myNumbers.keys():
        finalNumber=myNumbers[number]
    else:
        if number > 20 and number <100:
            finalNumber=convertor(number-number%20)[:-1]+'და'+convertor(number%20)
        elif number>100 and number<1000:
            if number//100==1:
                prefix=''
            else:
                prefix=convertor(number//100)
            if len(prefix)>0 and prefix[-1]=='ი':
                prefix=prefix[:-1]
            if number%100==0:
                finalNumber=prefix+convertor(100)
            else:
                finalNumber=prefix+convertor(100)[:-1]+' '+convertor(number%100)
        elif number>=1000 and number<1000000:
            if number//1000==1:
                if number%1000==0:
                    finalNumber=convertor(10)[:-1]+convertor(100)
                else:
                    finalNumber=convertor(10)[:-1]+convertor(100)[:-1]+' '+convertor(number%1000)
                    
            else:
                if number%1000==0:
                    finalNumber=convertor(number//1000)+' '+convertor(10)[:-1]+convertor(100)
                else:
                    finalNumber=convertor(number//1000)+' '+convertor(10)[:-1]+convertor(100)[:-1]+' '+convertor(number%1000)
        elif number>1000000 and number<1000000000:
            
            prefix=convertor(number//1000000)
            
            if number%1000000==0:
                finalNumber=prefix+convertor(1000000)
            else:
                finalNumber=prefix+' '+convertor(1000000)[:-1]+' '+convertor(number%1000000)
        elif number>1000000000:
            
            prefix=convertor(number//1000000000)
            
            if number%1000000000==0:
                finalNumber=prefix+convertor(1000000000)
            else:
                finalNumber=prefix+' '+convertor(1000000000)[:-1]+' '+convertor(number%1000000000)


    return finalNumber

print(convertor(2345235))


    
    
