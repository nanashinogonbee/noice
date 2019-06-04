n = '\nq = f"""n = {n!r}\nd = {d!r}"""'
d = '\nwith open(f"q2.py", "w") as s:\n    s.write(q + n + d)'
q = f"""n = {n!r}
d = {d!r}"""
with open(f"q2.py", "w") as s:
    s.write(q + n + d)
