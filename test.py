from textbox import TextBox
from label import Label
import time
from form import FontStyle, Form, Size, Font, Color, ColorMap
from item import Item
from button import Button
from point import Point

form = Form()
form.setBackgroudColor(ColorMap.AZURE)
form.show()

button = Button()
button.Text = 'Click'
size = Size(55, 30)
point = Point(form.Size.width / 2, form.Size.height / 2)
font = Font(FontStyle.FONT_HERSHEY_SIMPLEX, 0.5, ColorMap.BLACK)

button.Size = size
button.Point = point
button.Font = font
button.BackColor = Color(ColorMap.GOLD)
button.BoredColor = Color(ColorMap.BLACK)

form.Add(button)


button = Button()
button.Text = 'Click1'
size = Size(70, 30)
point = Point(40, 40)
font = Font(FontStyle.FONT_HERSHEY_PLAIN, 1, ColorMap.WHITESMOKE)

button.Size = size
button.Point = point
button.Font = font
button.BackColor = Color(ColorMap.BLUE)
button.BoredColor = Color(ColorMap.BLACK)

form.Add(button)

label = Label()
label.Text = "Hello World"
point = Point(100, 50)
font = Font(FontStyle.FONT_HERSHEY_PLAIN, 1, ColorMap.BLACK)

label.Point = point
label.Font = font

form.Add(label)


textbox = TextBox()
point = Point(300, 50)
size = Size(150, 30)
font = Font(FontStyle.FONT_HERSHEY_PLAIN, 1, ColorMap.BLACK)

textbox.Point = point
textbox.Size = size
textbox.Font = font
textbox.BackColor = Color(ColorMap.WHITESMOKE)
textbox.BoredColor = Color(ColorMap.BLACK)

form.Add(textbox)