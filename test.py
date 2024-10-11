newphrase = "rainstorm"
           # 012345678
           # 123456789 -- college board version
# create a new variable called shortpage
# and assign it a value by slicing the newphrase variable by removing the first 3 characters and the last 3 characters
# the first three characters are "rai". the last three characters are "orm"
# substring(string, start. end)

shortpage = newphrase[3:len(newphrase)-3]
print(shortpage)

# collegeboard version [4:len(newphrase)-6]
# print(shortphrase)
# why does it end eith 6?
# because the last index is not included