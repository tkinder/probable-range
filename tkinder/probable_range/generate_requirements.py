import ast
import sys


def extract_imports(filename):
    with open(filename, "r") as f:
        node = ast.parse(f.read())

    imports = []
    for n in node.body:
        if isinstance(n, ast.Import):
            for alias in n.names:
                imports.append(alias.name)
        elif isinstance(n, ast.ImportFrom):
            for alias in n.names:
                imports.append(f"{n.module}.{alias.name}")

    return imports


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_requirements.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    imports = extract_imports(filename)
    with open("requirements.txt", "w") as f:
        f.write("\n".join(imports))
