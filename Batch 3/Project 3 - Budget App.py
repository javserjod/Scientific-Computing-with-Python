''' INFORMATION

Complete the Category class. It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment. When objects are created, they are passed in the name of the category. The class should have an instance variable called ledger that is a list. The class should also contain the following methods:

A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {'amount': amount, 'description': description}.
A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.
A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
A transfer method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description 'Transfer to [Destination Budget Category]'. The method should then add a deposit to the other budget category with the amount and the description 'Transfer from [Source Budget Category]'. If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.
When the budget object is printed it should display:

A title line of 30 characters where the name of the category is centered in a line of * characters.
A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
A line displaying the category total.


Besides the Category class, create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. It should return a string that is a bar chart.

The chart should show the percentage spent in each category passed in to the function. The percentage spent should be calculated only with withdrawals and not with deposits, and it should be the percentage of the amount spent for each category to the total spent for all categories. Down the left side of the chart should be labels 0 - 100. The 'bars' in the bar chart should be made out of the 'o' character. The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar. Each category name should be written vertically below the bar. There should be a title at the top that says 'Percentage spent by category'.



'''

# Solution by Javier Serrano Jodral

class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        LINE_SIZE = 30
        DESCRIPTION_SIZE = 23
        AMOUNT_SIZE = 7
        category_name_size = len(self.category)
        # Title
        formatted = '*' * (LINE_SIZE//2 - category_name_size//2) + self.category
        formatted += '*' * (LINE_SIZE- len(formatted)) + '\n'

        # items in ledger
        for item in self.ledger:
            if (description_size:= len(item['description'])) <= DESCRIPTION_SIZE:
                formatted += item['description'] + (DESCRIPTION_SIZE-description_size)*' '
            else:
                formatted += item['description'][:DESCRIPTION_SIZE]


            if (amount_size:= len(str(format(item['amount'], '.2f')))) <= AMOUNT_SIZE:
                formatted += (AMOUNT_SIZE-amount_size)*' ' + str(format(item['amount'], '.2f'))
            else:
                formatted += str(format(item['amount'], '.2f'))[:AMOUNT_SIZE]

            formatted += '\n'

        # Total
        formatted += 'Total: ' + str(format(self.get_balance(), '.2f'))

        return formatted
        
    def deposit(self, amount, description=''):
        self.ledger.append({'amount':amount, 'description':description})
        
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):   # if there's enough money to withdraw
            self.ledger.append({'amount':-amount, 'description':description})
            return True
        return False

    def get_balance(self):
        return sum([element['amount'] for element in self.ledger])

    def transfer(self, amount, category):   # to another budget category (instance)
        if self.withdraw(amount, f'Transfer to {category.category}'):
            category.deposit(amount, f'Transfer from {self.category}')
            return True
        return False

    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        else:
            return False




def create_spend_chart(categories):
    total_per_category = []   # only withdrawals
    for category in categories:
        withdrawals = [item['amount'] for item in category.ledger if item['amount'] < 0]
        total_per_category.append(sum(withdrawals))

    total = sum(total_per_category)

    percentage_per_category = list(map(lambda x: round((abs(x/total))*100), total_per_category))

    print(percentage_per_category)
    # Title
    output = 'Percentage spent by category' +'\n'
    
    # Bars
    for i in range(100, -10, -10):
        line = (3-len(str(i)))*' ' + str(i) + '| '
        for n_category in range(len(categories)):
            if percentage_per_category[n_category] >= i:
                line += 'o  '
            else:
                line += '   '

        output = output + line + '\n'
    
    # Dashed line
    output += 4*' '+ '-'*(1+len(categories)*3) + '\n'

    # Category names vertically
    names = [category.category for category in categories]
    max_length_name = max(list(map(len, names)))
    
    for letter_index in range(max_length_name):
        output += ' '*5
        for name in names:
            try:
                output += name[letter_index] + '  '
            except:
                output += '   '
        
        if letter_index < max_length_name-1:
            output += '\n'

    return output



food = Category('Food')
clothing = Category('Clothing')
auto = Category('Auto')

food.deposit(1000, "deposit")
food.transfer(200, clothing)
food.transfer(300, auto)
food.withdraw(50, "Lidl")
clothing.withdraw(98, 'Nike')
auto.withdraw(130, "Audi")

print(food)
print('\n')
print(clothing)
print('\n')
print(auto)
print('\n')
print(create_spend_chart([food, clothing, auto]))