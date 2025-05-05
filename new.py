import os
import yaml

# Input file
input_file = "azure-crds.yaml"
output_base_dir = "output_crds"

# Load all documents from the YAML file
with open(input_file, 'r', encoding='utf-8') as stream:
    docs = list(yaml.safe_load_all(stream))

for i, doc in enumerate(docs):
    if doc and doc.get("kind") == "CustomResourceDefinition":
        group = doc.get("spec", {}).get("group", "unknown")
        name = doc.get("metadata", {}).get("name", f"crd_{i}")

        # Create directory for the group
        group_dir = os.path.join(output_base_dir, group)
        os.makedirs(group_dir, exist_ok=True)

        # Write each CRD to a separate file
        output_file = os.path.join(group_dir, f"{name}.yaml")
        with open(output_file, "w", encoding='utf-8') as out:
            yaml.dump(doc, out, default_flow_style=False)

print("CRDs have been split and saved group-wise.")
