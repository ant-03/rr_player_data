#from pygubudesigner.main import start_pygubu
#start_pygubu()
from pygubu import Builder
from pandas import read_csv
from matplotlib import rcParams
from matplotlib.pyplot import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
rcParams.update({"figure.autolayout": True})


app = Builder()
app.add_from_file("project_rr.ui")
window = app.get_object("window")
canvas_frame = app.get_object("canvas_frame")

data = read_csv("Python Project Data.csv", sep=",")
print(data)

fig = Figure(figsize=(4,3))
canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
canvas.get_tk_widget().pack()


#axis = fig.add_subplot()
#data.plot(
 #   ax=axis,
  #  kind="hist",
   # y="Total"
#)


#def click_all_players():
 # fig.clf()
  #axis = fig.add_subplot()
  #data.plot(
   # ax=axis,
    #kind="hist",
    #y="Name"
  #)

  #canvas.draw()


def click_by_inv():
    fig.clf()
    axis = fig.add_subplot()
    inv_total = data.groupby(["Player"]).mean(numeric_only=True)
    inv_total.plot(
        ax=axis,
        kind="barh",
        y="Inventions"
    )

    canvas.draw()


def click_by_room():
    fig.clf()
    axis = fig.add_subplot()
    room_total = data.groupby(["Player"]).mean(numeric_only=True)
    room_total.plot(
        ax=axis,
        kind="barh",
        y="Rooms"
    )

    canvas.draw()


#def click_by_genre():
    #fig.clf()
    #axis = fig.add_subplot()
    #genre_total = data.groupby(["Genre"]).mean()
    #genre_total.plot(
        #ax=axis,
        #kind="barh",
       # y="Total"
   # )
  
  #  canvas.draw()

# comment for above code: the biggest flaw is that it is string data, not numerical!

def click_by_sub():
    fig.clf()
    axis = fig.add_subplot()
    sub_total = data.groupby(["Player"]).mean(numeric_only=True)
    sub_total.plot(
        ax=axis,
        kind="barh",
        y="Subscribers"
    )
    canvas.draw()


canvas.draw()

app.connect_callbacks({
    "click_by_inv": click_by_inv,
    "click_by_room": click_by_room,
    "click_by_sub": click_by_sub
})


window.mainloop()