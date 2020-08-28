def generate_bill(cost, tax, tip):
 taxvalue = (cost * 7.85)/100
 print(f'Tax Amount on {cost} is {taxvalue}')
 tipvalue = (cost*tip)/100
 print(f'Tip Amount on {cost} is {tipvalue}')
 finalvalue = cost + taxvalue + tipvalue
 print(f'Final Value {finalvalue}')


if __name__ == '__main__':
    generate_bill(54.76, 7.85, 15)
