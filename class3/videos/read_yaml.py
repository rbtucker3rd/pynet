import yaml

# filename = "test1.yml"
filename = input("Enter filename: ")
with open(filename) as f:
    yaml_out = yaml.load(f)
print(yaml_out)