import os
import json
import pandas as pd
import re
base_path = "E:\\Jsons"
excel_file = os.path.join(base_path, "forjson.xlsx")
template_file = os.path.join(base_path, "6tap.json")
data = pd.read_excel(excel_file, header=None)
group_paths = data.iloc[:, 0]
def sanitize_path(path):
    sanitized = re.sub(r'[<>:"/\\|?*]', '_', path)
    sanitized = sanitized.strip()
    return sanitized
with open(template_file, "r") as file:
    template_json = json.load(file)

for group_path in group_paths:
    sanitized_group_path = "/".join([sanitize_path(part) for part in group_path.split("/")])
    modified_json = template_json.copy()
    modified_json["android.app.extra.PROVISIONING_ADMIN_EXTRAS_BUNDLE"]["GroupPath"] = group_path
    group_path_dir = os.path.join(base_path, *sanitized_group_path.split("/"))
    os.makedirs(group_path_dir, exist_ok=True)
    output_file_path = os.path.join(group_path_dir, "6tap.json")
    with open(output_file_path, "w") as output_file:
        json.dump(modified_json, output_file, indent=4)

print(f"All JSON files have been created in {base_path}.")
