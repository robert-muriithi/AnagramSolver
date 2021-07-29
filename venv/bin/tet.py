email = "washi@ifix.com"
em = email[email.index("@") + 1: email.index(".")]
# uname = email
x = slice(0, email.index("@"))
y = slice(email.index("@") + 1, email.index("."))
print(email[x])
print(email[y])

sum1 = 0
i = 0
while i <= 3:
    sum1 += i
    i = i + 1

print(sum1)
