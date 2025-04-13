import os
import shutil

# Source and destination paths
src_dir = "/teamspace/studios/this_studio/verse19/dataset-01training/derivatives"
dst_dir = "/teamspace/studios/this_studio/monai-radiology/images/labels/final/train"

# Make sure destination directory exists
os.makedirs(dst_dir, exist_ok=True)

# Walk the directory structure (DFS)
for root, dirs, files in os.walk(src_dir):
    for file in files:
        if file.endswith(".nii.gz"):
            # New filename without '_seg-vert_msk'
            new_filename = file.replace("_seg-vert_msk", "_label")
            src_path = os.path.join(root, file)
            dst_path = os.path.join(dst_dir, new_filename)

            # Copy and rename the file
            shutil.copy2(src_path, dst_path)
            print(f"Copied: {src_path} -> {dst_path}")
