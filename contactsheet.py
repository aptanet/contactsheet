import PySimpleGUI as sg
from datetime import datetime
from subprocess import call

# create contact sheet using montage command
form = sg.FlexForm('Photo Montage')

# not playing with the look at the moment
# sg.ChangeLookAndFeel('SandyBeach')

# input form
# choose a directory, thumbnail sizes and spacing for now
layout = [
    [sg.Text('Source Folder'), sg.InputText(''), sg.FolderBrowse()],
    [sg.Text('Thumbnail Width'), sg.Spin([i for i in range(100,200)],initial_value=180),
        sg.Text('Horzontal Spacing'), sg.Spin([i for i in range(0,10)],initial_value=5)],
    [sg.Text('Thumbnail Height'), sg.Spin([i for i in range(100,200)],initial_value=180),
        sg.Text('Vertical Spacing'), sg.Spin([i for i in range(0,10)],initial_value=5)],
    [sg.Submit(), sg.Cancel()]
         ]
         
button, values = form.LayoutAndRead(layout)

# grab the date and time to format the unique filename for the contact sheet
now = datetime.now()
timestamp = str(now.strftime("%Y%m%d_%H-%M-%S"))

# hard coded bits for now
# drop shadoes, A4 (works?), geometry values from form
# only scans for .jpg files (case specific)
# outputs to contactsheet_YYYYmmdd_HH-MM-SS.jpg to avoid overwriting other files
call (["montage", "-shadow", "-page", "A4", "-geometry", values[1]+"x"+values[3]+"+"+values[2]+"+"+values[4], 
    values[0]+"/*.jpg", values[0]+"/contactsheet_"+timestamp+".jpg"])

# and that's all folks
