# Calculate the area of a circle, rectangle, and triangle.

def ar_circle(rad):
    return (3.14157*rad*rad)

def ar_rectangle(length, width):
    return (length * width)

def ar_triangle(base, height):
    return (0.5 * base * height)


while True:
    shape = input("What shape (circle/rectangle/triangle), you want to calculate area of ? : ").strip().lower()

    if shape == 'circle':
        try:
            rad = float(input("Enter the radius : "))
        except ValueError:
            print("Please Enter a Number.")
            continue
        print(f"Radius of circle is: {ar_circle(rad)}")

    elif shape == 'rectangle':
        try:
            dim = list(map(float, input("Enter the space-seperated dimensions: ").split()))
            print(f"Area of Rectangle = {ar_rectangle(dim[0], dim[1])}")
        except IndexError:
            print("Please enter length(space)width.")
            continue
        except ValueError:
            print("Both entries must be numbers only.")
            continue


    elif shape == 'triangle':
        try:
            dim = list(map(float, input("Enter the space-seperated dimensions: ").split()))
            print(f"Area of Triangle = {ar_triangle(dim[0], dim[1])}")
        except IndexError:
            print("Please enter base(space)height.")
            continue
        except ValueError:
            print("Both entries must be numbers only.")
            continue


        

    query = input("Do you want to continue : (y/n) ").strip().lower()
    if query == 'n':
        print("See you very soon.....")
        break