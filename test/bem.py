import time

def jnck(target):
    return f"+{'—' * (len(str(target)) + 2)}"

t = "kocak"
y = "hihi"
print(f"{jnck(t)}{jnck(y)}")

w = time.strftime("%A %d %B %Y")

print(w)
