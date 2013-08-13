import csv
import wx
import os

class toSpreadsheet(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Add Commas', size =(300,200))
        selectFile = wx.FileDialog(None)
        selectFile.ShowModal()
        addCommas = selectFile.GetPath()

        #opens the first comma seperated value file
        f = open(addCommas, 'r')
        #reads in the csv file
        name = f.read()
        #prints it out, 'cause testing
        print name
        #replace space with comma
        numlist = (name.replace(' ',',')) #replace space with commas
        #more verification
        print numlist
        #opens the file that the edited version of the first file is written to
        newfile = open('FinalSpreadsheet.csv' , 'w+')
        #writes to the new file
        newfile.write(numlist)
        #close the file
        newfile.close()
        raise SystemExit
        os._exit


if __name__ =='__main__':
    app=wx.PySimpleApp()
    frame = toSpreadsheet(parent = None, id = -1)
    frame.Show()
    app.MainLoop()

    




