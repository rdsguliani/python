

input = 'My name is raman and i am 24 years of age.'


dict = {};
vowel_dict = {};

def count_chars():

    f = open("demo.txt", "r")
    content = f.read();
    #print(f.read())

    for item in content:
        if(item.isalpha()):
            if item in dict:
                dict[item] = dict[item] + 1;
            else:
                dict[item] = 1;

    print(dict);
    # print (dict.keys())

def count_words():

    f = open("demo.txt", "r")
    # content = f.read();
    # print(f.readline());
    # print(f.readline());
    # print(f.readline());

    #file_it = iter(f.readline())
    #print(f.read())
    line = f.readline();

    word_dict = {};
    # lines = list(line for line in (l.strip() for l in f) if line)
    while line:
        line = line.strip('\n').strip();
        if line:
    #line_list = list(line for line in lines if line)
            for item in line.split(' '):
                #if(item.isalpha()):
                if item in word_dict:
                    word_dict[item] = word_dict[item] + 1;
                else:
                    word_dict[item] = 1;
        line = f.readline()
    f.close()
    print(word_dict);
    # print (word_dict.keys())

def count_vowels():
    vowel = 'aeiou'
    for item in input.lower():
        if(item in vowel):
            if item in vowel_dict:
                vowel_dict[item] = vowel_dict[item] + 1;
            else:
                vowel_dict[item] = 1;

    print(vowel_dict);
    print (vowel_dict.keys())


def pallindrome():
    st = 'rcar';
    reverse_st = st[::-1];

    if(st == reverse_st):
        return True;


    return False;


# print(pallindrome());
# count_chars();
count_words();
# count_vowels();
