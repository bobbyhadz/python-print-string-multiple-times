# Repeat a string N times in Python

my_str = 'bobby'

# ✅ Repeat a string N times
new_str = my_str * 2
print(new_str)  # 👉️ bobbybobby

# ---------------------------------------

# ✅ Repeat a substring N times
new_str = my_str[0:3] * 2
print(new_str)  # 👉️ bobbob

# ---------------------------------------

# ✅ Repeat a string N times with a separator
new_str = ' '.join([my_str] * 2)
print(new_str) # 👉️ bobby bobby