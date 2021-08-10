verse = {1: "first",
             2: "second",
             3: "third",
             4: "fourth",
             5: "fifth",
             6: "sixth",
             7: "seventh",
             8: "eighth",
             9: "ninth",
             10: "tenth",
             11: "eleventh",
             12: "twelfth"}

verse_1 =  ["a partridge in a pear tree",
              "two turtle doves",
              "three french hens",
              "four calling birds",
              "five golden rings",
              "six geese-a-laying",
              "seven swans-a-swimming",
              "eight maids-a-milking",
              "nine ladies dancing",
              "ten lords-a-leaping",
              "eleven pipers-a-piping",
              "twelve drummers drumming"]

def recite(start_verse, end_verse):

    if start_verse<end_verse:
        for i in range(start_verse, end_verse+1):

            message = f"on the {verse[i]} day of christmas my true love gave to me: {verse_1[0:i]} , "
            print(message)
    if start_verse > end_verse:
        for i in range(start_verse, end_verse-1 , -1):
            message = f"on the {verse[i]} day of christmas my true love gave to me: {verse_1[i-1::-1]} , "
            print(message)


recite(6, 8)
