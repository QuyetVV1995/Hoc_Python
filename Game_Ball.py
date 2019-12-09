from tkinter import *
import time
import random

class Ball:
    def __init__(seft, canvas, color, thanh): # khoi tao qua bong
        seft.canvas = canvas
        seft.thanhtruot = thanh
        seft.id = canvas.create_oval(10,10,25,25, fill=color)
        seft.canvas.move(seft.id, 100, 200)
        start = [-3, -2, -1, 1,2,3]
        random.shuffle(start)   #xao tron mang start
        seft.x = start[0];
        seft.y = start[1];
        seft.canvas_height = 500;
        seft.canvas_width = 400;
        seft.over = False
        seft.diem = 0;
    
    def vacham(seft, v_pos_bong):
        v_pos_thanhtruot = seft.canvas.coords(seft.thanhtruot.id)
        if v_pos_bong[0] >= v_pos_thanhtruot[0] and v_pos_bong[0] <= v_pos_thanhtruot[2]: # Bat su kien va cham bong va thanh truot
            if v_pos_bong[1] >= v_pos_thanhtruot[1] and v_pos_bong[3] <= v_pos_thanhtruot[3]:
                seft.diem += 1
                print(seft.diem)
                return True
        return False
            
    def draw(seft): # Di chuyen qua bong den vi tri x  y
        seft.canvas.move(seft.id, seft.x, seft.y)
        v_pos_bong = seft.canvas.coords(seft.id) # lay vi tri cua seft (qua bong)
       
        if v_pos_bong[1] <= 0:
            seft.y = 3
        if v_pos_bong[3] >= seft.canvas_height:
            seft.over = True
        if seft.vacham(v_pos_bong) == True: # kiem tra dieu kien va cham
            seft.y = -3
        if v_pos_bong[0] <= 0:
            seft.x = 3
        if v_pos_bong[2] >= seft.canvas_width:
            seft.x = -3
            
        
            
class thanhTruot:
    def __init__(seft, canvas, color):
        seft.canvas = canvas
        seft.id = canvas.create_rectangle(0,0,100,20, fill = color)
        seft.canvas.move(seft.id, 300, 400)
        seft.canvas.bind_all('<KeyPress-Left>',seft.trai)
        seft.canvas.bind_all('<KeyPress-Right>',seft.phai)
        seft.x = 0
        seft.y = 0

    def draw(seft):
        seft.canvas.move(seft.id, seft.x, seft.y)
        
    def trai(seft, event):
        seft.x = -2
        
    def phai(seft, event):
        seft.x = 2


tk = Tk()
tk.title('Game Bong')
tk.resizable(0,0)   # Co dinh khung
can = Canvas(tk, width=400, height=500)
can.pack()

ob_thanhtruot = thanhTruot(can, "blue")
ob_bong = Ball(can, 'red',ob_thanhtruot)

while 1:
    if ob_bong.over != True:
        ob_bong.draw()
        ob_thanhtruot.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
    else:
        break;

print('Game over')
