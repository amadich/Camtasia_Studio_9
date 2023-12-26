file_path = r'C:\ProgramData\TechSmith\Camtasia Studio 18\RegInfo.ini'

new_content = '''[RegistrationInfo]
ValidationData3=1
RegistrationKey=BBCUVUVDRCM8C5SCHMX72M3A5
RegisteredTo=YR-Invasion
ValidationData1=V7L+Ex2/T==OV:BE
ValidationData2=1'''

# Write the new content to the file
with open(file_path, 'w') as file:
    file.write(new_content)

print("File content updated successfully.")
