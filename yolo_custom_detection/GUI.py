#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#    Mar 31, 2020 11:43:20 AM IST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import GUI_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    GUI_support.set_Tk_var()
    top = Toplevel1 (root)
    GUI_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    GUI_support.set_Tk_var()
    top = Toplevel1 (w)
    GUI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1100x650+326+171")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("Object Detection")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=0.167)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#F3F3F3")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.TButton1 = ttk.Button(self.Frame1)
        self.TButton1.place(relx=0.054, rely=0.092, height=60, width=160)
        self.TButton1.configure(command=GUI_support.open_files)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Open Folder''')

        self.TButton2 = ttk.Button(self.Frame1)
        self.TButton2.place(relx=0.054, rely=0.292, height=60, width=160)
        self.TButton2.configure(command=GUI_support.next_image)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Next Image''')

        self.TButton3 = ttk.Button(self.Frame1)
        self.TButton3.place(relx=0.054, rely=0.492, height=60, width=160)
        self.TButton3.configure(command=GUI_support.previous_image)
        self.TButton3.configure(takefocus="")
        self.TButton3.configure(text='''Previous Image''')

        self.TButton4 = ttk.Button(self.Frame1)
        self.TButton4.place(relx=0.054, rely=0.692, height=60, width=160)
        self.TButton4.configure(command=GUI_support.save_annotation)
        self.TButton4.configure(takefocus="")
        self.TButton4.configure(text='''Save Annotation''')

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.773, rely=0.0, relheight=1.0, relwidth=0.227)
        self.Frame2.configure(relief='flat')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(background="#F3F3F3")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.Frame2)
        self.Label1.place(relx=0.08, rely=0.015, height=46, width=212)
        self.Label1.configure(activebackground="#595959")
        self.Label1.configure(activeforeground="white")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#FFFFFF")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 16")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(highlightthickness="2")
        self.Label1.configure(relief="groove")
        self.Label1.configure(text='''Select Model''')

        self.Frame3 = tk.Frame(self.Frame2)
        self.Frame3.place(relx=0.08, rely=0.108, relheight=0.285, relwidth=0.86)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#FFFFFF")
        self.Frame3.configure(highlightbackground="#d9d9d9")
        self.Frame3.configure(highlightcolor="black")

        self.Checkbutton1 = tk.Checkbutton(self.Frame3)
        self.Checkbutton1.place(relx=0.047, rely=0.054, relheight=0.33
                , relwidth=0.921)
        self.Checkbutton1.configure(activebackground="#f9f9f9")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(anchor='w')
        self.Checkbutton1.configure(background="#FFFFFF")
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(font="-family {Segoe UI} -size 11")
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(text='''yolo''')
        self.Checkbutton1.configure(variable=GUI_support.model1)

#         self.Checkbutton2 = tk.Checkbutton(self.Frame3)
#         self.Checkbutton2.place(relx=0.047, rely=0.324, relheight=0.292
#                 , relwidth=0.921)
#         self.Checkbutton2.configure(activebackground="#ececec")
#         self.Checkbutton2.configure(activeforeground="#000000")
#         self.Checkbutton2.configure(anchor='w')
#         self.Checkbutton2.configure(background="#FFFFFF")
#         self.Checkbutton2.configure(disabledforeground="#a3a3a3")
#         self.Checkbutton2.configure(font="-family {Segoe UI} -size 12")
#         self.Checkbutton2.configure(foreground="#000000")
#         self.Checkbutton2.configure(highlightbackground="#d9d9d9")
#         self.Checkbutton2.configure(highlightcolor="black")
#         self.Checkbutton2.configure(justify='left')
#         self.Checkbutton2.configure(text='''faster-rcnn''')
#         self.Checkbutton2.configure(variable=GUI_support.model2)
#         tooltip_font = "TkDefaultFont"
#         ToolTip(self.Checkbutton2, tooltip_font, '''ssd_inception_v2_
# coco''', delay=0.5)

#         self.Checkbutton3 = tk.Checkbutton(self.Frame3)
#         self.Checkbutton3.place(relx=0.047, rely=0.649, relheight=0.346
#                 , relwidth=0.921)
#         self.Checkbutton3.configure(activebackground="#ececec")
#         self.Checkbutton3.configure(activeforeground="#000000")
#         self.Checkbutton3.configure(anchor='w')
#         self.Checkbutton3.configure(background="#FFFFFF")
#         self.Checkbutton3.configure(disabledforeground="#a3a3a3")
#         self.Checkbutton3.configure(font="-family {Segoe UI} -size 12")
#         self.Checkbutton3.configure(foreground="#000000")
#         self.Checkbutton3.configure(highlightbackground="#d9d9d9")
#         self.Checkbutton3.configure(highlightcolor="black")
#         self.Checkbutton3.configure(justify='left')
#         self.Checkbutton3.configure(text='''yolo''')
#         self.Checkbutton3.configure(variable=GUI_support.model3)

        self.Label2 = tk.Label(self.Frame2)
        self.Label2.place(relx=0.08, rely=0.415, height=66, width=152)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#FFFFFF")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 14")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(relief="ridge")
        self.Label2.configure(text='''Detection
Threshold''')

        self.Entry1 = tk.Entry(self.Frame2)
        self.Entry1.place(relx=0.72, rely=0.431,height=45, relwidth=0.18)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")
        self.Entry1.configure(textvariable=GUI_support.threshold)
        tooltip_font = "TkDefaultFont"
        ToolTip(self.Entry1, tooltip_font, '''value beween 0 and 1 in steps of 0.05''', delay=0.5)

        self.Frame5 = tk.Frame(self.Frame2)
        self.Frame5.place(relx=0.08, rely=0.538, relheight=0.329, relwidth=0.86)
        self.Frame5.configure(relief='groove')
        self.Frame5.configure(borderwidth="2")
        self.Frame5.configure(relief="groove")
        self.Frame5.configure(background="#FFFFFF")
        self.Frame5.configure(highlightbackground="#d9d9d9")
        self.Frame5.configure(highlightcolor="black")

        self.Checkbutton4 = tk.Checkbutton(self.Frame5)
        self.Checkbutton4.place(relx=0.047, rely=0.042, relheight=0.131
                , relwidth=0.874)
        self.Checkbutton4.configure(activebackground="#ececec")
        self.Checkbutton4.configure(activeforeground="#000000")
        self.Checkbutton4.configure(anchor='w')
        self.Checkbutton4.configure(background="#FFFFFF")
        self.Checkbutton4.configure(disabledforeground="#a3a3a3")
        self.Checkbutton4.configure(foreground="#000000")
        self.Checkbutton4.configure(highlightbackground="#d9d9d9")
        self.Checkbutton4.configure(highlightcolor="black")
        self.Checkbutton4.configure(justify='left')
        self.Checkbutton4.configure(text='''Car''')
        self.Checkbutton4.configure(variable=GUI_support.car_check)

        # self.Checkbutton5 = tk.Checkbutton(self.Frame5)
        # self.Checkbutton5.place(relx=0.047, rely=0.234, relheight=0.131
        #         , relwidth=0.874)
        # self.Checkbutton5.configure(activebackground="#ececec")
        # self.Checkbutton5.configure(activeforeground="#000000")
        # self.Checkbutton5.configure(anchor='w')
        # self.Checkbutton5.configure(background="#FFFFFF")
        # self.Checkbutton5.configure(disabledforeground="#a3a3a3")
        # self.Checkbutton5.configure(foreground="#000000")
        # self.Checkbutton5.configure(highlightbackground="#d9d9d9")
        # self.Checkbutton5.configure(highlightcolor="black")
        # self.Checkbutton5.configure(justify='left')
        # self.Checkbutton5.configure(text='''Cat''')
        # self.Checkbutton5.configure(variable=GUI_support.cat_check)

        # self.Checkbutton6 = tk.Checkbutton(self.Frame5)
        # self.Checkbutton6.place(relx=0.047, rely=0.421, relheight=0.131
        #         , relwidth=0.874)
        # self.Checkbutton6.configure(activebackground="#ececec")
        # self.Checkbutton6.configure(activeforeground="#000000")
        # self.Checkbutton6.configure(anchor='w')
        # self.Checkbutton6.configure(background="#FFFFFF")
        # self.Checkbutton6.configure(disabledforeground="#a3a3a3")
        # self.Checkbutton6.configure(foreground="#000000")
        # self.Checkbutton6.configure(highlightbackground="#d9d9d9")
        # self.Checkbutton6.configure(highlightcolor="black")
        # self.Checkbutton6.configure(justify='left')
        # self.Checkbutton6.configure(text='''Dog''')
        # self.Checkbutton6.configure(variable=GUI_support.dog_check)

        # self.Checkbutton7 = tk.Checkbutton(self.Frame5)
        # self.Checkbutton7.place(relx=0.047, rely=0.607, relheight=0.131
        #         , relwidth=0.874)
        # self.Checkbutton7.configure(activebackground="#ececec")
        # self.Checkbutton7.configure(activeforeground="#000000")
        # self.Checkbutton7.configure(anchor='w')
        # self.Checkbutton7.configure(background="#FFFFFF")
        # self.Checkbutton7.configure(disabledforeground="#a3a3a3")
        # self.Checkbutton7.configure(foreground="#000000")
        # self.Checkbutton7.configure(highlightbackground="#d9d9d9")
        # self.Checkbutton7.configure(highlightcolor="black")
        # self.Checkbutton7.configure(justify='left')
        # self.Checkbutton7.configure(text='''Bottle''')
        # self.Checkbutton7.configure(variable=GUI_support.bottle_check)

        # self.Checkbutton8 = tk.Checkbutton(self.Frame5)
        # self.Checkbutton8.place(relx=0.047, rely=0.794, relheight=0.131
        #         , relwidth=0.874)
        # self.Checkbutton8.configure(activebackground="#ececec")
        # self.Checkbutton8.configure(activeforeground="#000000")
        # self.Checkbutton8.configure(anchor='w')
        # self.Checkbutton8.configure(background="#FFFFFF")
        # self.Checkbutton8.configure(disabledforeground="#a3a3a3")
        # self.Checkbutton8.configure(foreground="#000000")
        # self.Checkbutton8.configure(highlightbackground="#d9d9d9")
        # self.Checkbutton8.configure(highlightcolor="black")
        # self.Checkbutton8.configure(justify='left')
        # self.Checkbutton8.configure(text='''Chair''')
        # self.Checkbutton8.configure(variable=GUI_support.chair_check)

        self.Button1 = tk.Button(self.Frame2)
        self.Button1.place(relx=0.08, rely=0.892, height=50, width=215)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#FFFFFF")
        self.Button1.configure(command=GUI_support.detect_image)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI} -size 14")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(relief="ridge")
        self.Button1.configure(text='''Detect''')

        self.Frame4 = tk.Frame(top)
        self.Frame4.place(relx=0.164, rely=0.0, relheight=1.0, relwidth=0.615)
        self.Frame4.configure(relief='groove')
        self.Frame4.configure(borderwidth="2")
        self.Frame4.configure(relief="groove")
        self.Frame4.configure(background="#FFFFFF")
        self.Frame4.configure(highlightbackground="#d9d9d9")
        self.Frame4.configure(highlightcolor="black")

        self.Label3 = tk.Label(self.Frame4)
        self.Label3.place(relx=0.0, rely=0.0, height=645, width=670)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#FFFFFF")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Open image from Open Folder''')

# ======================================================
# Modified by Rozen to remove Tkinter import statements and to receive
# the font as an argument.
# ======================================================
# Found the original code at:
# http://code.activestate.com/recipes/576688-tooltip-for-tkinter/
# ======================================================

from time import time, localtime, strftime

class ToolTip(tk.Toplevel):
    """
    Provides a ToolTip widget for Tkinter.
    To apply a ToolTip to any Tkinter widget, simply pass the widget to the
    ToolTip constructor
    """
    def __init__(self, wdgt, tooltip_font, msg=None, msgFunc=None,
                 delay=1, follow=True):
        """
        Initialize the ToolTip

        Arguments:
          wdgt: The widget this ToolTip is assigned to
          tooltip_font: Font to be used
          msg:  A static string message assigned to the ToolTip
          msgFunc: A function that retrieves a string to use as the ToolTip text
          delay:   The delay in seconds before the ToolTip appears(may be float)
          follow:  If True, the ToolTip follows motion, otherwise hides
        """
        self.wdgt = wdgt
        # The parent of the ToolTip is the parent of the ToolTips widget
        self.parent = self.wdgt.master
        # Initalise the Toplevel
        tk.Toplevel.__init__(self, self.parent, bg='black', padx=1, pady=1)
        # Hide initially
        self.withdraw()
        # The ToolTip Toplevel should have no frame or title bar
        self.overrideredirect(True)

        # The msgVar will contain the text displayed by the ToolTip
        self.msgVar = tk.StringVar()
        if msg is None:
            self.msgVar.set('No message provided')
        else:
            self.msgVar.set(msg)
        self.msgFunc = msgFunc
        self.delay = delay
        self.follow = follow
        self.visible = 0
        self.lastMotion = 0
        # The text of the ToolTip is displayed in a Message widget
        tk.Message(self, textvariable=self.msgVar, bg='#FFFFDD',
                font=tooltip_font,
                aspect=1000).grid()

        # Add bindings to the widget.  This will NOT override
        # bindings that the widget already has
        self.wdgt.bind('<Enter>', self.spawn, '+')
        self.wdgt.bind('<Leave>', self.hide, '+')
        self.wdgt.bind('<Motion>', self.move, '+')

    def spawn(self, event=None):
        """
        Spawn the ToolTip.  This simply makes the ToolTip eligible for display.
        Usually this is caused by entering the widget

        Arguments:
          event: The event that called this funciton
        """
        self.visible = 1
        # The after function takes a time argument in miliseconds
        self.after(int(self.delay * 1000), self.show)

    def show(self):
        """
        Displays the ToolTip if the time delay has been long enough
        """
        if self.visible == 1 and time() - self.lastMotion > self.delay:
            self.visible = 2
        if self.visible == 2:
            self.deiconify()

    def move(self, event):
        """
        Processes motion within the widget.
        Arguments:
          event: The event that called this function
        """
        self.lastMotion = time()
        # If the follow flag is not set, motion within the
        # widget will make the ToolTip disappear
        #
        if self.follow is False:
            self.withdraw()
            self.visible = 1

        # Offset the ToolTip 10x10 pixes southwest of the pointer
        self.geometry('+%i+%i' % (event.x_root+20, event.y_root-10))
        try:
            # Try to call the message function.  Will not change
            # the message if the message function is None or
            # the message function fails
            self.msgVar.set(self.msgFunc())
        except:
            pass
        self.after(int(self.delay * 1000), self.show)

    def hide(self, event=None):
        """
        Hides the ToolTip.  Usually this is caused by leaving the widget
        Arguments:
          event: The event that called this function
        """
        self.visible = 0
        self.withdraw()

# ===========================================================
#                   End of Class ToolTip
# ===========================================================

if __name__ == '__main__':
    vp_start_gui()





