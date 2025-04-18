import json

with open('aml_image_othermodels.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

widgets_meta = nb.get("metadata", {}).get("widgets", {})
widget_data = widgets_meta.get("application/vnd.jupyter.widget-state+json", {})

# Check if 'state' is missing and keys look like widget IDs
if "state" not in widget_data:
    new_state = {}
    for k, v in widget_data.items():
        if isinstance(v, dict) and "state" in v:
            new_state[k] = v
    # Replace the widget_data with the correct format
    nb["metadata"]["widgets"]["application/vnd.jupyter.widget-state+json"] = {
        "state": new_state
    }

with open('your_notebook.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2)
