
def convert_to_binary(number):
    st = '';

    while (number > 0):
        s = number%2;
        number = number/2;
        st += str(s);

    st = st[::-1]
    print(' binary number is {}'.format(st));

def convert_to_decimal(number):
    value = 0;
    multiply_factor = 1;
    while (number > 0):
        s = number%10;
        number = number/10;
        value += s * multiply_factor;
        multiply_factor = multiply_factor*2;

    print(' decimal number is {}'.format(value));


def user_input():
    user_conversion = raw_input('What do you want to do ? for decimal press d otherwise press b ?')
    print (user_conversion)

    if (user_conversion == 'd'):
        input_number = int(input('Enter binary number you want to convert to decimal ?'))
        convert_to_decimal(input_number);
    else:
        input_number = int(input('Enter decimal number you want to convert to binary ?'))
        convert_to_binary(input_number);

user_input();
