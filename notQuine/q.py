n = '\nq = "n = " + repr(n)\nwith open(f"q.py", "w") as s:\n    s.write(q + n)'
q = "n = " + repr(n)
with open(f"q.py", "w") as s:
    s.write(q + n)
