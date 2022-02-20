from pydub import AudioSegment
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter.messagebox import *

_VERSION = '1.0 Alpha'


def MP32WAV(mp3_path, wav_path):
    """
    这是MP3文件转化成WAV文件的函数
    :param mp3_path: MP3文件的地址
    :param wav_path: WAV文件的地址
    """
    MP3_File = AudioSegment.from_mp3(file=mp3_path)
    MP3_File.export(wav_path, format="wav")


class Method:
    def timeProcess(self):
        if file_path.get() == '':
            print("No File.")
            ui.selectPath()

        print(times.get())
    def textConvert(self):
        pass


class UI_Method:
    def selectPath(self):
        # 选择文件path_接收文件地址
        path_ = askopenfilename()

        # 通过replace函数替换绝对文件地址中的/来使文件可被程序读取
        # 注意：\\转义后为\，所以\\\\转义后为\\
        path_ = path_.replace("/", "\\\\")
        # path设置path_的值
        path.set(path_)

    def customChosen(self):
        print('a')

    def more(self):
        root.geometry('720x380')
        more_run['text'] = '收回'
        more_run['command'] = ui.back

    def back(self):
        root.geometry('255x380')
        more_run['text'] = '更多'
        more_run['command'] = ui.more

method = Method()
ui = UI_Method()
# MP32WAV('b.mp3', 'b.wav')

root = Tk()
root.geometry('255x380')
root.title('AnsAudio ' + _VERSION)
menubar = Menu(root)
path = StringVar()
times = StringVar()
times.set(1)
isCustom = BooleanVar()

# lb1 = Label(root, text='AnsAudio ' + _VERSION)
# lb1.place(x=20, y=5, width=120, height=30)

# ------文件选择部分------
frame1 = Frame(root)
frame1.place(x=20, y=20, width=205, height=60)
file_path = Entry(frame1, textvariable=path)
file_path.place(x=5, y=5, width=135, height=35)

choose_file = Button(frame1, text='选择', command=ui.selectPath)
choose_file.place(x=145, y=5, width=60, height=35)

# ------倍速功能部分------
frame2 = Frame(root)
frame2.place(x=20, y=95, width=205, height=80)
_0_5x = Radiobutton(frame2, text="0.5x", variable=times, value=0.5)
_0_5x.place(x=5, y=5)
_1_3x = Radiobutton(frame2, text="1.3x", variable=times, value=1.3)
_1_3x.place(x=60, y=5)
_1_5x = Radiobutton(frame2, text="1.5x", variable=times, value=1.5)
_1_5x.place(x=5, y=25)
_2_0x = Radiobutton(frame2, text="2.0x", variable=times, value=2.0)
_2_0x.place(x=60, y=25)

time_scale = Scale(frame2, variable=times, length=130, value=1, from_=0.1, to=5)
time_scale.place(x=5, y=55)

time_label = Label(frame2, textvariable=times)
time_label.place(x=140, y=55, width=60, height=30)

time_run = Button(frame2, text='开始', command=method.timeProcess)
time_run.place(x=130, y=15, width=70, height=30)

# ------拓展功能部分------
frame3 = Frame(root)
frame3.place(x=20, y=190, width=205, height=120)

convert_run = Button(frame3, text='转文本', command=method.textConvert)
convert_run.place(x=5, y=5, width=80, height=30)

more_run = Button(frame3, text='更多', command=ui.more)
more_run.place(x=5, y=50, width=80, height=30)

root.mainloop()
