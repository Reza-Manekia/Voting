nationality = input("Are you Pakistani(y/n): ")
if nationality == 'y':
    age = int(input("write your age: "))
    if age >= 18:
        print("Eligible")
    else:
        print("not eligible")
else:
    print("not eligible")

