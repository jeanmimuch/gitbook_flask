import jinja2

templateLoader = jinja2.FileSystemLoader( searchpath="./")
templateEnv = jinja2.Environment( loader=templateLoader )
template = templateEnv.get_template("index.html")

print(template.render())
