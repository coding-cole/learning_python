temps = [221, 234, 340, -9999, 230]

new_temps = []
for temp in temps:
    new_temps.append(temp / 10)

# if there is no need for else like the next line, this is the syntax
new_temperature = [temp / 10 for temp in temps if temp != -9999]

new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]



print(new_temps)
print(new_temperature)
       
def mean(value):
    if isinstance(value, dict):
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean

student_grades = {"Marry":3.4, "John":4.4, "Tilly":0.2}
doubles_list = list(range(0, 29, 2))

def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"

user_input = float(input("Enter temperature: "))

print(weather_condition(user_input))

# String Formating
name = input("Enter your name: ")
surname = input("Enter your surname: ")

# for python 3 and above
message = f"Hello {name}"

# for < Python 3
message = "Hello %s %s!" %(name, surname)
print(message)

monday_temp = {9.1, 8.8, 7.6}
student_grades = {"Marry":3.4, "John":4.4, "Tilly":0.2}

for grades in student_grades.values():
    print(grades)

for temperature in monday_temp:
    print(round(temperature))

for letter in "Hello":
    print(letter.title())

username = ''

while username != "pypy":
    username = input("Enter username: ")

def sentence_maker(phrase):
    interogatives = ("what", "where", "how", "when")
    capitalised = phrase.capitalize()
    if phrase.startswith(interogatives):
        return "{}?".format(capitalised)
    else:
        return "{}.".format(capitalised)

results = []
# while True:
    # user_input = input("Say something: ")
#     if user_input == "/end":
#         break
#     else:
#         results.append(sentence_maker(user_input))
        
# print(" ".join(results))

# non default arg
def triangle_area(a, b):
    return a * b

# default arg
def tri_area(a, b=4):
    return a * b

# non-keyword arg
print(tri_area(4, 5))

# keyword arg
print(triangle_area(b=4, a=5))

# non-keyword limitles args
def mean2(*args):
    return sum(args) / len(args)

# keyword limitles args
def limitls_kw(**kwargs):
    return sum()

print(mean2(1, 2, 3))
print(limitls_kw(a=0, b=0, c=0, d=0))


