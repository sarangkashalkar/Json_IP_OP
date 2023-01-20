import json
import re
landmark = None
area = None

print("Please enter the name of the state:")
state= input(str())

print("Please enter the name of the country:")
country= input(str())

print("Please enter the address")
addr_1 = input(str())

regex= "\d{6}"
pin_code = re.findall(regex, addr_1)
new_add = addr_1.replace(pin_code[0], '')

x = new_add.split(",")
city_name = x[-1]
house = x[0]
locality = x[1]

if len(x) >3:
    landmark = x[2]
    if len(x)>4:
        area = x[3]
    else:
        pass
else:
    pass

final = {"house":house,
         "locality":locality,
        "landmark":landmark,
        "area":locality,
        "city":city_name,
        "state":state,
        "country":country,
        "pin_code":pin_code[0]}

out_file = open("myfile.json", "w")

json.dump(out_file, out_file, indent=6)

out_file.close()
