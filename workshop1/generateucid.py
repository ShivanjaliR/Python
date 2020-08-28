def generateucid(firstname, lastname):
    lastnamelength = len(lastname)
    finalresult = "";
    if lastnamelength > 6 :
        finalresult = lastname[0:6]
    else:
        finalresult = lastname
        remlength = 6-lastnamelength
        finalresult = finalresult + firstname[0:remlength]
    finalresult = finalresult + firstname[0] + firstname[len(firstname)-1]
    print(f'Final Result is {finalresult}')


if __name__ == '__main__':
    firstname = input('Enter first name')
    lastname = input('Enter last name')
    generateucid(firstname, lastname)
