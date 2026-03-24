import os
from jinja2 import Environment, FileSystemLoader, TemplateSyntaxError

tpls_dir = os.path.join(os.getcwd(), 'templates')
env = Environment(loader=FileSystemLoader(tpls_dir))

errors = []
for fname in os.listdir(tpls_dir):
    if fname.endswith('.html'):
        try:
            env.get_template(fname)
            print(f'{fname}: OK')
        except TemplateSyntaxError as e:
            errors.append((fname, e))
            print(f'{fname}: SyntaxError - {e}')

if errors:
    print('\nTemplates with errors:')
    for fname, e in errors:
        print(fname, e)
else:
    print('\nAll templates parsed successfully')
