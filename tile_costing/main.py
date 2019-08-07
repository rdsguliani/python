

class Tile_Costing():

    input_width = 0;
    input_length = 0;
    cost_per_foot = 0;


    def __init__( self):
        pass

    def total_cost (self):
        return self.input_width * self.input_length * self.cost_per_foot;

    def user_input(self):

        while True:
            try:
                self.cost_per_foot = int(input("Enter price per foot ? "))
                self.input_width = int(input("Enter width of the hall ? "))
                self.input_length = int(input("Enter length of hall ? "))
                break;
            except:
                print('please enter integer values')
                continue;



tile_costing = Tile_Costing();
tile_costing.user_input();
print(tile_costing.total_cost());
