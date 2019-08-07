import calculator

class Main():

    input_total_cost = 0;
    input_amount = 0;


    def __init__( self):
        pass

    def user_input(self):

        while True:
            try:
                self.input_total_cost = int(input("Enter Total cost of device ? "))
                self.input_amount = int(input("Enter total amount ? "))
                break;
            except:
                print('please enter integer values')
                continue;


print(__name__)

if (__name__ == '__main__'):
    main = Main();
    # main.user_input();

    # change_calculator = calculator.Change_Calculator(main.input_total_cost, main.input_amount);
    change_calculator = calculator.Change_Calculator(300, 337);
    change_calculator.get_change();
