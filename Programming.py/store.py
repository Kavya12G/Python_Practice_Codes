p = {}

while  True:
   inp = input().strip()
   if inp.lower() == "done":
      break
   name, price = inp.split(",")
   price = float(price.strip())
   p[name] = price

for name, price in p.items():
    print(f"{name}: {price}")
