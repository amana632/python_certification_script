import tkinter as tk
from tkinter import filedialog
import pandas as pd

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

def getCSV ():
    global df
    
    import_file_path = filedialog.askopenfilename()
    df = pd.read_csv (import_file_path)
    print (df)
    
browseButton_CSV = tk.Button(text="      Import CSV File     ", command=getCSV, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=browseButton_CSV)
# tk.Button(root, text='Close',command=root.destroy).grid(row=1, column=1)


root.mainloop()

for i in df.index: 
    if df['Batch'][i]=="Devops":
        certificate_url = "./devops-certi.png"
    elif df['Batch'][i]=="Fullstack" :
        certificate_url = "./fullstack-certi.png"
    else:
        certificate_url = "./ml-certi.png"
    from PIL import Image, ImageDraw, ImageFont

    image = Image.open(certificate_url)

    draw = ImageDraw.Draw(image)
    
    font = ImageFont.truetype('./GoogleSans-Regular.ttf', size=25)

    (x, y) = (645, 375)

    message = df['Dates'][i]
    color = 'rgb(0, 0, 0)' # black color

    draw.text((x, y), message, fill=color, font=font)

    (x, y) = (120, 1200)

    message = df['Code Number'][i]
    draw.text((x, y), message, fill=color, font=font)
    
    font = ImageFont.truetype('./GoogleSans-Bold.ttf', size=55)
    (x, y) = (490, 700)
    message = df['Name'][i]
    draw.text((x, y), message, fill=color, font=font)

    image.save('./final_cert/'+message+'.png')
