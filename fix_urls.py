import re
import os

template_dir = r"g:\business_accelartor\business_accelartor\user\templates"
base_path = os.path.join(template_dir, "base.html")
pages_path = os.path.join(template_dir, "pages.html")

def update_static(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # The assets are under user/static/assests/assets/
    # So we change {% static 'assets/...' %} to {% static 'assests/assets/...' %}
    content = re.sub(r'\{%\s*static\s+[\'"]assets/([^\'"]+)[\'"]\s*%\}', r"{% static 'assests/assets/\g<1>' %}", content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

update_static(base_path)
update_static(pages_path)
print("Updated static URLs successfully.")
