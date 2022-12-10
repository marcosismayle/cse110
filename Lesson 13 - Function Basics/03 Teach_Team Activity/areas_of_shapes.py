square_length = 0

def compute_area_square(square_length):
    return square_length ** 2

def compute_area_rectangle(rectangle_length, rectangle_width):
    return rectangle_length * rectangle_width
    
def compute_area_circle(circle_radius):
    return 3.14 * (circle_radius ** 2)


shape = ''

while shape.lower() != 'quit':

    shape = input('What shape do you want to calculate? ')

    if shape.lower() == 'square':
        square_length = float(input('What is the length of a side of the square? '))
        area = compute_area_square(square_length)
        print(f'The area of the square is: {area} m')
    elif shape.lower() == 'rectangle':
        rectangle_length = float(input('What is the length? '))
        rectangle_width = float(input('What is the widthw? '))
        area = compute_area_rectangle(rectangle_length, rectangle_width)
        print(f'The area of the rectangle is: {area} m')
    elif shape.lower() == 'circle':
        circle_radius = float(input('What is the radius? '))
        area = compute_area_circle(circle_radius)
        print(f'The area of the circle is: {area} m')

print('Thank you. Good Bye.')