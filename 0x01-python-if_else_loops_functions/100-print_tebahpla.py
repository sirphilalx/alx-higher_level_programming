#!/usr/bin/python3
for i in range(122, 97, -1):
    character = chr(i)
    if i % 2 == 0:
      print(f"{character.lower()}", end="")
    else:
      print(f"{character.upper()}", end="")
