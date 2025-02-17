def CyclicGroup(n):
    """Returns the cyclic group C_n (integers mod n under addition)."""
    elements = [str(i) for i in range(n)]
    multiplication = {
        a: {b: str((int(a) + int(b)) % n) for b in elements} for a in elements
    }
    generators = ["1"]  
    return elements, multiplication, generators


def DihedralGroup(n):
    """Returns the dihedral group D_n (symmetries of a regular n-gon)."""
    elements = [f"r{i}" for i in range(n)] + [f"s{i}" for i in range(n)]
    
    multiplication = {}
    for i in range(n):
        multiplication[f"r{i}"] = {f"r{j}": f"r{(i + j) % n}" for j in range(n)}
        multiplication[f"s{i}"] = {f"r{j}": f"s{(i + j) % n}" for j in range(n)}
        multiplication[f"r{i}"]["s0"] = f"s{i}"
        multiplication[f"s{i}"]["s0"] = f"r{i}"

    generators = ["r1", "s0"]  
    return elements, multiplication, generators


# Some fun predefined groups
S3Group = (
    ["e", "(12)", "(13)", "(23)", "(123)", "(132)"],
    {
        "e": {"e": "e", "(12)": "(12)", "(13)": "(13)", "(23)": "(23)", "(123)": "(123)", "(132)": "(132)"},
        "(12)": {"e": "(12)", "(12)": "e", "(13)": "(132)", "(23)": "(123)", "(123)": "(23)", "(132)": "(13)"},
        "(13)": {"e": "(13)", "(12)": "(123)", "(13)": "e", "(23)": "(132)", "(123)": "(12)", "(132)": "(23)"},
        "(23)": {"e": "(23)", "(12)": "(132)", "(13)": "(123)", "(23)": "e", "(123)": "(13)", "(132)": "(12)"},
        "(123)": {"e": "(123)", "(12)": "(23)", "(13)": "(12)", "(23)": "(13)", "(123)": "e", "(132)": "(132)"},
        "(132)": {"e": "(132)", "(12)": "(13)", "(13)": "(23)", "(23)": "(12)", "(123)": "(132)", "(132)": "e"},
    },
    ["(12)", "(123)"]
)

Q8Group = (
    ["1", "-1", "i", "-i", "j", "-j", "k", "-k"],
    {
        "1": {"1": "1", "-1": "-1", "i": "i", "-i": "-i", "j": "j", "-j": "-j", "k": "k", "-k": "-k"},
        "-1": {"1": "-1", "-1": "1", "i": "-i", "-i": "i", "j": "-j", "-j": "j", "k": "-k", "-k": "k"},
        "i": {"1": "i", "-1": "-i", "i": "-1", "-i": "1", "j": "k", "-j": "-k", "k": "-j", "-k": "j"},
        "-i": {"1": "-i", "-1": "i", "i": "1", "-i": "-1", "j": "-k", "-j": "k", "k": "j", "-k": "-j"},
        "j": {"1": "j", "-1": "-j", "i": "-k", "-i": "k", "j": "-1", "-j": "1", "k": "i", "-k": "-i"},
        "-j": {"1": "-j", "-1": "j", "i": "k", "-i": "-k", "j": "1", "-j": "-1", "k": "-i", "-k": "i"},
        "k": {"1": "k", "-1": "-k", "i": "j", "-i": "-j", "j": "-i", "-j": "i", "k": "-1", "-k": "1"},
        "-k": {"1": "-k", "-1": "k", "i": "-j", "-i": "j", "j": "i", "-j": "-i", "k": "1", "-k": "-1"},
    },
    ["i", "j"]
)
