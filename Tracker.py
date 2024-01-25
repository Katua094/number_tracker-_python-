dict_items={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "0":"zero",
}

result=""
number=input("put down your number!")
No_mapping_found= True

for digit in number:
    if digit in dict_items:
        result+=dict_items[digit]+" "
        No_mapping_found=False
    else:
        result+="No_mapping_found"
if No_mapping_found:
    print("No mapping of number found")
else:
    print(result)

