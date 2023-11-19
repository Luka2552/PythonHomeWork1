# x1 and x2 = X-axis on the chess board, y1 and y2 = Y-axis on the chess board
# იქს1 და იქს2 = იქს-ღერძი ჭადრაკის დაფაზე, იგრეკ1 და იგრეკ2 = იგრეკ-ღერძი ჭადრაკის დაფაზე

# While running the code, it sometimes gives an error: "ValueError: invalid literal for int() with base 10:", run it again and it should be fixed.
# როდესაც კოდს ვტვირთავთ, ხანდახან შემდეგ შეცდომას გვაძლევს: "ValueError: invalid literal for int() with base 10:", გადატვირთეთ და წესით უნდა მუშაობდეს.

x1 = int(input("Please enter the X-axis of the 1st square from 1-8: "))
if not (8 >= x1 >= 1):
    print("Error! Please enter a whole number between 1 and 8.")
    x1 = int(input("Please Re-enter the X-axis of the 1st square from 1-8: "))

y1 = int(input("Please enter the Y-axis of the 1st square from 1-8: "))
if not (8 >= y1 >= 1):
    print("Error! Please enter a whole number between 1 and 8.")
    y1 = int(input("Please Re-enter the Y-axis of the 1st square from 1-8: "))

x2 = int(input("Please enter the X-axis of the 2nd square from 1-8: "))
if not (8 >= x2 >= 1):
    print("Error! Please enter a whole number between 1 and 8.")
    x2 = int(input("Please Re-enter the X-axis of the 2nd square from 1-8: "))

y2 = int(input("Please enter the Y-axis of the 2nd square from 1-8: "))
if not (8 >= y2 >= 1):
    print("Error! Please enter a whole number between 1 and 8.")
    y2 = int(input("Please Re-enter the Y-axis of the 2nd square from 1-8: "))

Black = 0
White = 0

if x1 == 1 and y1 in [1, 3, 5, 7] or x2 == 1 and y2 in [1, 3, 5, 7]:
    Black = 1
if x1 == 2 and y1 in [2, 4, 6, 8] or x2 == 2 and y2 in [2, 4, 6, 8]:
    Black = 1
if x1 == 3 and y1 in [1, 3, 5, 7] or x2 == 3 and y2 in [1, 3, 5, 7]:
    Black = 1
if x1 == 4 and y1 in [2, 4, 6, 8] or x2 == 4 and y2 in [2, 4, 6, 8]:
    Black = 1
if x1 == 5 and y1 in [1, 3, 5, 7] or x2 == 5 and y2 in [1, 3, 5, 7]:
    Black = 1
if x1 == 6 and y1 in [2, 4, 6, 8] or x2 == 6 and y2 in [2, 4, 6, 8]:
    Black = 1
if x1 == 7 and y1 in [1, 3, 5, 7] or x2 == 7 and y2 in [1, 3, 5, 7]:
    Black = 1
if x1 == 8 and y1 in [2, 4, 6, 8] or x2 == 8 and y2 in [2, 4, 6, 8]:
    Black = 1

if x1 == 1 and y1 in [2, 4, 6, 8] or x2 == 1 and y2 in [2, 4, 6, 8]:
    White = 1
if x1 == 2 and y1 in [1, 3, 5, 7] or x2 == 2 and y2 in [1, 3, 5, 7]:
    White = 1
if x1 == 3 and y1 in [2, 4, 6, 8] or x2 == 3 and y2 in [2, 4, 6, 8]:
    White = 1
if x1 == 4 and y1 in [1, 3, 5, 7] or x2 == 4 and y2 in [1, 3, 5, 7]:
    White = 1
if x1 == 5 and y1 in [2, 4, 6, 8] or x2 == 5 and y2 in [2, 4, 6, 8]:
    White = 1
if x1 == 6 and y1 in [1, 3, 5, 7] or x2 == 6 and y2 in [1, 3, 5, 7]:
    White = 1
if x1 == 7 and y1 in [2, 4, 6, 8] or x2 == 7 and y2 in [2, 4, 6, 8]:
    White = 1
if x1 == 8 and y1 in [1, 3, 5, 7] or x2 == 8 and y2 in [1, 3, 5, 7]:
    White = 1
    
if White == 1 and Black == 1:
    print("NO")
else:
    print("YES")
    
    # Akhsna - (x1 + x2 + y1 + y2) % 2 == 1
    
    
    
    # Def Solution
    
def square_input(name):
    
    while True:
        
        coord = int(input(f"{name}: "))
        
        if coord < 1 or coord > 8:
            print("Out of Range")
            continue
        
        return coord            
    
x1 = square_input()
y1 = square_input()
x2 = square_input()
y2 = square_input()

print(x1, y1, x2, y2)