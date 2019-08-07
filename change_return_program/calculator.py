
denominations = [25, 10, 5, 1]
currentCount = [];

class Change_Calculator():

    # self.quarters = 0;
    # self.dime = 0;
    # self.nickels = 0;
    # self.pennies = 0;

    def __init__(self, total_cost, total_amount):
        self.total_cost = total_cost;
        self.total_amount = total_amount;
        self.return_amount = total_amount - total_cost;

    def get_change(self):

        for (index, item) in enumerate(denominations):
            count = 0;

            while (self.return_amount >= item):
                self.return_amount -= item;
                count += 1;

            if (count != 0):
                currentCount.append({'count':count, 'value': item});

        print(currentCount)
