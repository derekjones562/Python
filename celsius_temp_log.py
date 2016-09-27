#!/usr/bin/python

short_temp_log = "\n\
2015-04-08_16-53-14 22.25\n\
2015-04-11_16-56-58 22.312\n\
2015-04-11_17-06-58 22.312\n\
2015-04-11_17-16-58 23.125\n\
2015-04-11_17-26-58 23.0\n\
"

long_temp_log = "\n\
2015-04-08_16-53-14 22.25\n\
2015-04-11_16-56-58 22.312\n\
2015-04-11_17-06-58 22.312\n\
2015-04-11_17-16-58 23.125\n\
2015-04-11_17-26-58 23.0\n\
2015-04-11_17-36-58 23.062\n\
2015-04-11_17-46-58 23.062\n\
2015-04-11_17-56-58 23.125\n\
2015-04-11_18-06-58 23.25\n\
2015-04-11_18-16-58 23.312\n\
2015-04-11_18-26-58 23.312\n\
2015-04-11_18-36-58 23.312\n\
2015-04-11_18-46-58 23.187\n\
2015-04-11_18-56-58 23.0\n\
2015-04-11_19-06-58 22.75\n\
2015-04-11_19-16-58 22.687\n\
2015-04-11_19-26-58 22.625\n\
2015-04-11_19-36-58 22.562\n\
2015-04-11_19-46-58 22.312\n\
2015-04-11_19-56-58 22.187\n\
2015-04-11_20-06-58 22.0\n\
2015-04-11_20-16-58 21.75\n\
2015-04-11_20-26-58 21.687\n\
2015-04-11_20-36-58 21.125\n\
2015-04-11_20-46-58 20.687\n\
2015-04-11_20-56-58 20.5\n\
2015-04-11_21-06-58 20.375\n\
2015-04-11_21-16-58 20.187\n\
2015-04-11_21-26-58 20.062\n\
2015-04-11_21-36-58 20.062\n\
2015-04-11_21-46-58 20.0\n\
2015-04-11_21-56-58 19.812\n\
"

def process_temp_log_record(rawlogEntry):
  numString = ""
  processedLog=[]
  #print rawlogEntry;
  for s in range(0, len(rawlogEntry)):
    if(rawlogEntry[s] is '-' or rawlogEntry[s] is'_' or rawlogEntry[s] is " " or rawlogEntry[s] is'\n'):
      numInt = int(numString)
      processedLog.append(numInt)
      numString=""
    else:
      numString += rawlogEntry[s]
  numInt = float(numString)
  processedLog.append(numInt)
  return processedLog

def process_temp_log(logEntry):
  singleLog=""
  processedLog=[]
  
  splitLog = logEntry.split('\n')
  #print splitLog,"\n"
  #print len(splitLog)," =l\n"
  for s in splitLog:
    if(s is not''):
      #print s, "  =s\n"
      temp = process_temp_log_record(s)
      processedLog.append(temp)
    singleLog=""
  return processedLog

def display_max_celsius_temp(tempLog):
  processedTempLog = process_temp_log(tempLog);
  maxTempIndex =0;
  currMaxTemp=processedTempLog[0][6]
  for t in range(1, len(processedTempLog)):
    if(processedTempLog[t][6] > currMaxTemp):
      currMaxTemp = processedTempLog[t][6]
      maxTempIndex = t	
  print "Maximum Celcius Temperature of ", processedTempLog[maxTempIndex][6], " was at " , processedTempLog[maxTempIndex][3],":",processedTempLog[maxTempIndex][4] , ":" , processedTempLog[maxTempIndex][5], " on " ,processedTempLog[maxTempIndex][1],"\\",processedTempLog[maxTempIndex][2],"\\",processedTempLog[maxTempIndex][0]


def display_min_celsius_temp(tempLog):
  processedTempLog = process_temp_log(tempLog);
  minTempIndex =0;
  currMinTemp=processedTempLog[0][6]
  for t in range(1, len(processedTempLog)):
    if(processedTempLog[t][6] < currMinTemp):
      currMinTemp = processedTempLog[t][6]
      minTempIndex = t	
  print "Minimum Celcius Temperature of ", processedTempLog[minTempIndex][6], " was at " , processedTempLog[minTempIndex][3],":",processedTempLog[minTempIndex][4] , ":" , processedTempLog[minTempIndex][5], " on " ,processedTempLog[minTempIndex][1],"\\",processedTempLog[minTempIndex][2],"\\",processedTempLog[minTempIndex][0]


def display_average_celsius_temp(tempLog):
  processedTempLog = process_temp_log(tempLog)
  averageTemp=0.0
  sumOfTemps=0
  numOfTemps=0
  for t in range(0, len(processedTempLog)):
    sumOfTemps+=processedTempLog[t][6]
    numOfTemps+=1
  averageTemp = float(sumOfTemps)/numOfTemps
  print "Average Celcius Temperature from ",processedTempLog[0][3],":",processedTempLog[0][4],":",processedTempLog[0][5]," on ",processedTempLog[0][1],"\\",processedTempLog[0][2],"\\",processedTempLog[0][0]," to ",processedTempLog[len(processedTempLog)-1][3],":",processedTempLog[len(processedTempLog)-1][4],":",processedTempLog[len(processedTempLog)-1][5]," on ",processedTempLog[len(processedTempLog)-1][1],"\\",processedTempLog[len(processedTempLog)-1][2],"\\",processedTempLog[len(processedTempLog)-1][0]," is ",averageTemp


## tests
#process_temp_log(short_temp_log)
display_max_celsius_temp(short_temp_log)
display_min_celsius_temp(short_temp_log)
display_average_celsius_temp(short_temp_log)

display_max_celsius_temp(long_temp_log)
display_min_celsius_temp(long_temp_log)
display_average_celsius_temp(long_temp_log)
