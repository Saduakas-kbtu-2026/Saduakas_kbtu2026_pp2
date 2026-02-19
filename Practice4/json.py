import json

# Load JSON file
with open("sample-data.json") as f:
    data = json.load(f)

# Print header
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<6} {'MTU':<6}")
print("-" * 50, "-" * 20, "-" * 6, "-" * 6)

# Iterate over each interface
for item in data['imdata']:
    attrs = item['l1PhysIf']['attributes']
    dn = attrs.get('dn', '')
    descr = attrs.get('descr', '')
    speed = attrs.get('speed', '')
    mtu = attrs.get('mtu', '')
    print(f"{dn:<50} {descr:<20} {speed:<6} {mtu:<6}")
