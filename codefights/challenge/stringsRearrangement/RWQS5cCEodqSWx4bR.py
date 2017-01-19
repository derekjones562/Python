def inserted(str1, config_array):
    new_config = []
    for element in config_array:
        for i in range(0,len(element)+1):
            tmp = []
            tmp = element*1
            tmp.insert(i, str1)
            new_config.append(tmp)
    return new_config
        
def buildConfigurationArray(inputArray):
    config_array = []
    config_array.append([inputArray.pop()])
    return factorial(inputArray, config_array)

def factorial(inputArray, config_array):
    if len(inputArray) ==0:
        return config_array
    else:
        str1=inputArray.pop()
        config_array = inserted(str1, config_array)
        return factorial(inputArray, config_array)      

def check_difference(str1, str2):
    letters_different =0
    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            letters_different +=1
    return letters_different

def check_arrangement(inputArray):
    for i in range(0, len(inputArray)):
        if i == len(inputArray)-1:
            break
        letters_different = check_difference(inputArray[i], inputArray[i+1])
        if letters_different != 1:
            return False
    return True

def stringsRearrangement(inputArray):
    config_array = buildConfigurationArray(inputArray)
    num_of_configurations = len(config_array)
    checked_configurations = 0
    while checked_configurations != num_of_configurations:
        inputArray = config_array[checked_configurations]
        if check_arrangement(inputArray):
            return True
        checked_configurations +=1
    return False
