## this is a test from json format to csv format

## JSON format: ‘{“name”: "JSON", "age":30, "car":null}’


## CSV format:
## name, age, car
## json, 30, null

## function: firist  read a json, use "" to spilt first line , and use tow buffer to record

## use {} to spilt first, use "" to get differnt tuple 

## first , use the most simple format to change
## use disctpry to record and write into files
test = '{"name":"json", "age" : "30", "car":"null"}'


f = open("test.csv","w")
f_dict = dict()
y_split = test.split("{")
print(y_split)

# here we can add into a function

def readInBraces():
    x_split = test.split(",")   ## first split the ,
        for i in x_split :
        i_split = i.split(":")  ## second split the :
        f_dict[i_split[0]] = i_split[1] ## we suppose that it isi rigid format 	

## write keys
def writeKeys():
    for i in f_dict.keys():
        print(i)
        f.write(i+",")
    f.write("\n")

## write values
def writeValues():
    for i in  f_dict.values():
        f.write(i+",")
    f.write("\n")


if __name__=="__main__":
    readOneFiles
    f1 = open("JsonInput.txt", "r")
    f2 = open("CsvOutput.csv","w")
     first: read f1 and split in {
             use for circle to readInBraces
                   writekeys
                   use for to writeValues

## then start to write into files

## split test, thisDict"name",

## write to file, first , write the keys

## start spilt , delete values

## update value, when complete split, then write to file


 




