import nbformat

notebooks = ["yolov8-kaggle-final.ipynb", "rtdetr-model.ipynb", "faster-rcnn-FINAL.ipynb"]

merged = nbformat.v4.new_notebook(cells=[])

for nb in notebooks:
    with open(nb, "r", encoding="utf-8") as f:
        nbf = nbformat.read(f, as_version=4)
        merged.cells.extend(nbf.cells)

with open("merged.ipynb", "w", encoding="utf-8") as f:
    nbformat.write(merged, f)

print("Merged notebook saved as merged.ipynb")
