def jnck(target):
    return f"+{'—' * (len(str(target)) + 2)}"

t = "kocak"
y = "hihi"
print(f"{jnck(t)}{jnck(y)}")
