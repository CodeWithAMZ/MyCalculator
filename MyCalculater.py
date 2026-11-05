#-----Module Imports------
import flet as ft
import math

#-----Main Function------
def main(page:ft.Page):
    page.title="My Calculater v0.1"
    page.window.width = 350
    page.window.height = 450
    page.window.center()
    page.window.maximizable = False
    page.window.resizable = False
    page.theme_mode = ft.ThemeMode.DARK

    def f1(e):
        if e.control.data in ['1','2','3','4','5','6','7','8','9']:
            if t1.value == '0':
                t1.value = e.control.data
            else:
                t1.value += e.control.data
        elif e.control.data=='c':  #Clear Button
            t1.value='0'
        elif e.control.data == '0' and t1.value != '0':
            t1.value += '0'
        elif e.control.data in ['+','-','*','/'] and len(t1.value)>0 and not(t1.value[-1] in ['+','-','*','/']) :
            t1.value+=e.control.data
        elif e.control.data == 'del':
            t1.value=t1.value[:-1]
            if t1.value=='':
                t1.value='0'

        if e.control.data == '=' and len(t1.value) > 0:
            if t1.value[-1] in ['+', '-', '*', '/']:
                t1.value = 'لطفا عدد بعد را وارد کنید'
            else:
                try:
                    t1.value = str(eval(t1.value))
                except ZeroDivisionError:
                    t1.value = 'نمیتوان بر صفر تقسیم کرد'

        elif e.control.data == 'fac' and t1.value.isdigit():     #Factorial Button
            t1.value = str(math.factorial(int(t1.value)))
        
        elif e.control.data == 'sqrt' and t1.value.isdigit():     #SQRT Button
                    t1.value = str(math.sqrt(int(t1.value)))

        elif e.control.data == 'pow' and t1.value.isdigit():     #Power Button
            t1.value += '**'
        page.update()
#------Rows------
    #row0
    t1=ft.TextField(value='0' , read_only=True , bgcolor='#1B1D2B' , color='#FFFFFF')
    r0=ft.Row(controls=[t1] , alignment=ft.MainAxisAlignment.CENTER)
    #row1
    b7=ft.ElevatedButton(text='7',bgcolor="#292B3C",color="#FFFFFF",width=65,height=55,on_click=f1,data='7')
    b8=ft.ElevatedButton(text='8',bgcolor="#292B3C",color="#FFFFFF",width=65,height=55,on_click=f1,data='8')
    b9=ft.ElevatedButton(text='9',bgcolor="#292B3C",color="#FFFFFF",width=65,height=55,on_click=f1,data='9')
    bplus=ft.ElevatedButton(text='+',bgcolor="#6548C8",color="#050505",width=65,height=55,on_click=f1,data='+')
    r1=ft.Row(controls=[b7,b8,b9,bplus], alignment=ft.MainAxisAlignment.CENTER)
    #row2
    b4=ft.ElevatedButton(text='4',bgcolor="#292B3C",color="#FFFFFF",width=65,height=55,on_click=f1,data='4')
    b5=ft.ElevatedButton(text='5',bgcolor="#292B3C",color="#FFFFFF",width=65,height=55,on_click=f1,data='5')
    b6=ft.ElevatedButton(text='6',bgcolor="#292B3C",color="#FFFFFF",width=65,height=55,on_click=f1,data='6')
    bmin=ft.ElevatedButton(text='-',bgcolor="#6548C8",color="#050505",width=65,height=55,on_click=f1,data='-')
    r2=ft.Row(controls=[b4,b5,b6,bmin],alignment=ft.MainAxisAlignment.CENTER)
    #row3
    b1=ft.ElevatedButton(text='1',bgcolor="#292B3C",color="#FFFFFF",width=65,height=55,on_click=f1,data='1')
    b2=ft.ElevatedButton(text='2',bgcolor="#292B3C",color="#FFFFFF",width=65,height=55,on_click=f1,data='2')
    b3=ft.ElevatedButton(text='3',bgcolor="#292B3C",color="#FFFFFF",width=65,height=55,on_click=f1,data='3')
    bmul=ft.ElevatedButton(text='*',bgcolor="#6548C8",color="#050505",width=65,height=55,on_click=f1,data='*')
    r3=ft.Row(controls=[b1,b2,b3,bmul],alignment=ft.MainAxisAlignment.CENTER)
    #row4
    bclear=ft.ElevatedButton(text='C',bgcolor="#E8435B",color="#050505",width=65,height=55,on_click=f1,data='c')
    b0=ft.ElevatedButton(text='0',bgcolor="#292B3C",color="#FFFFFF",width=65,height=55,on_click=f1,data='0')
    bequal=ft.ElevatedButton(text='=',bgcolor="#00A98F",color="#050505",width=65,height=55,on_click=f1,data='=')
    bdiv=ft.ElevatedButton(text='/',bgcolor="#6548C8",color="#050505",width=65,height=55,on_click=f1,data='/')
    r4=ft.Row(controls=[bclear,b0,bequal,bdiv] , alignment=ft.MainAxisAlignment.CENTER)
    #row5
    bbspace=ft.ElevatedButton(text='<--', bgcolor="#E5A52A" , color="#050505",width=65,height=55,on_click=f1,data='del')
    bfac=ft.ElevatedButton(text='n!', bgcolor="#087F83" , color="#050505",width=65,height=55,on_click=f1,data='fac')
    bsqrt=ft.ElevatedButton(text='SQRT', bgcolor="#087F83" , color="#050505",width=65,height=55,on_click=f1,data='sqrt')
    bpower=ft.ElevatedButton(text='**', bgcolor="#087F83" , color="#050505",width=65,height=55,on_click=f1,data='pow')
    r5=ft.Row(controls=[bbspace,bfac,bsqrt,bpower], alignment=ft.MainAxisAlignment.CENTER)
    
    page.add(r0,r1,r2,r3,r4,r5)
    page.update()

ft.app(main)
