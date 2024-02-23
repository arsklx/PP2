import json
with open("sample-data.json", "r") as my_file:
    json_string = my_file.read()
data = json.loads(json_string)

interfacess = data.get('imdata', [])
print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 50, "-" * 20, "-" * 8, "-" * 6)

for i in interfacess:
    l1physif = i.get('l1PhysIf', {})
    att = l1physif.get('attributes', {})
    
    DN = att.get('dn', '')
    description = att.get('descr', '')
    speed = att.get('speed', 'inherit')
    MTU = att.get('mtu', '')
    
    print("{:<50} {:<20} {:<8} {:<6}".format(DN, description, speed, MTU))
