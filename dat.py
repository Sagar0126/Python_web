import json
from jinja2 import Environment, FileSystemLoader

# Load the data from the JSON file
with open("data.json", "r") as f:
    data = json.load(f)

# Create the Jinja environment
env = Environment(loader=FileSystemLoader("C:\\Users\\sagar\\Downloads\\new"))

# Render the template
template = env.get_template("template.jinja")
output = template.render(data=data)

# Write the output to a file
with open("output.html", "w") as f:
    f.write(output)

