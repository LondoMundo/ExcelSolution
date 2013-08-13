import xlrd
import csv
import wx

class converter(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'ToCSV', size = (400, 400))
        panel = wx.Panel(self)
        selectFile = wx.FileDialog(None)
        selectFile.ShowModal()
        filePlace = selectFile.GetPath()
        print filePlace
        question = wx.TextEntryDialog(None, "What do you want to name the output .csv file? be usre to add .csv to the end", 'ToCSV', 'output' )
        question.ShowModal()
        outputFileName = question.GetValue()
        
        with xlrd.open_workbook(filePlace) as wb:
            sh = wb.sheet_by_index(0)  # or wb.sheet_by_name('name_of_the_sheet_here')
            with open(outputFileName, 'wb') as f:
                c = csv.writer(f)
                for r in range(sh.nrows):
                    c.writerow(sh.row_values(r))
        f.close()

if __name__ == '__main__':
    app=wx.PySimpleApp()
    frame = converter(parent = None, id = -1)
    frame.Show()
    app.MainLoop()
    

  





