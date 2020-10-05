guests =['Adela','Emily','Jackson','Kate','River','Bob']
person ='Kate'

guests2= ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
person2='Owen'

guests3=['Paul', 'John', 'Ringo', 'George']
person3='Ringo'

def fashionably_late(arrivals, name):
    partiers=[arrivals]
    print('Person: ' + name)
    # get index for person
    a = partiers[0].index(name)
    #subtracts one from length of partiers
    b = len(partiers[0])-1
    c=len(partiers[0])
    # divides the length of partiers in half
    d = c/2
    print('Index of person: ')
    print(a)

    if a < b  and a >= d:
        print('Is '+ name + ' fashionably late?' + ' Yes')
    else:
        print('Is '+ name + ' fashionably late?'+' No')

fashionably_late(guests,person)   
fashionably_late(guests2,person2) 
fashionably_late(guests3,person3) 
