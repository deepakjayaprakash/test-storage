import yaml


inputFile=open("input.yml",'r')
dataMap=yaml.load(inputFile)

outputFile=open('paramFile','w+')


storageDefinition= "fsd="+dataMap['SDName']+","+"anchor="+dataMap['Anchor']+","+"depth="+dataMap['Depth']+","+"files="+dataMap['Files']+","+"size="+dataMap['Size']+","+"width="+dataMap['Width']+"\n"

workDefinition= "fwd="+dataMap['WDName']+","+"fsd="+dataMap['SDForWD']+","+"rdpct="+dataMap['ReadPercentage']+","+"xfersize="+dataMap['TransferSize']+","+"fileio="+dataMap['FileIO']+","+"threads"+dataMap['Threads']+","+"fileselect="+dataMap['FileSelect']+"\n"


runDefinition= "rd="+dataMap['RDName']+","+"fwd="+dataMap['WDForRD']+","+"elapsed="+dataMap['Duration']+","+"interval="+dataMap['Interval']+"\n"

outputFile.write(storageDefinition)
outputFile.write(workDefinition)
outputFile.write(runDefinition)




outputFile.close()
inputFile.close()

