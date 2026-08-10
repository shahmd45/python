#check if 'e' is present in the string


# string = "hello";

# if ('e' in string):
#     print("character e exists");


# if, elif and else condition
'''

color = input("Enter color : ");

if color == 'Red':
    print("Stop");
elif color == 'Green': 
    print("Go");
elif color == 'Yellow' or color == 'Orange':
    print("Wait");
else:
    print("Wrong color");

'''

# Match & case condition

color = input("Enter color : ")

match color:
    case "green":
        print("GO")
    case "yellow":
        print("WAIT")
    case "orange":
            print("WAIT")
    case "red":
        print("STOP")
    case _:
        print("Wrong Color")
