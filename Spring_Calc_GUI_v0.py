import PySimpleGUI as sg
import utilities as ut

#------------------------ default variables ----------------------------------#
function1_active = function2_active = function3_active = False

# Okabe-Ito Color Blind Palette
black = '#000000'
orange = '#E69F00'
sky_blue = '#56B4E9'
bluish_green = '#009E73'
yellow = '#F0E442'
blue = '#0072B2'
vermilion = '#D55E00'
reddish_purple = '#CC79A7'

# fonts and buttons
default_background_color = "#d3d3d3"

f1 = ("Arial", 12, "bold")
f2 = ("Arial", 10, "bold")
f3 = ("Arial", 24, "bold")
f4 = ("Arial", 12)
f5 = ("Arial", 8, "bold")

b1 = {"size":(17,3), "font":("Arial", 12, "bold"), "button_color":("white", bluish_green)}
b2 = {"size":(17,1), "font":("Arial", 12, "bold"), "button_color":("white", bluish_green)}

#-----------------------------------------------------------------------------#


def make_home_window():
    
    layout_home = [
        
        [sg.Text("Welcome to Callum's Spring Calculator", font=f1, background_color=default_background_color, text_color="#151515")],
        [sg.Text("", background_color=default_background_color)],
        [sg.Text("I have 3 functionalities (at present)...", background_color=default_background_color, text_color="#151515")],
        [sg.Text("(1) calculate the total spring constant for multiple springs in series.", background_color=default_background_color, text_color="#151515")],
        [sg.Text("(2) calculate the total spring constant for multiple springs in paralell.", background_color=default_background_color, text_color="#151515")],
        [sg.Text("(3) calculate the combinations of springs in parallel to hit a target overall spring constant.", background_color=default_background_color, text_color="#151515")], 
        [sg.Text("", background_color=default_background_color)],
        [sg.Text("", background_color=default_background_color)],
        [sg.Text("", background_color=default_background_color)],
        [sg.Text("", background_color=default_background_color)],
        [sg.Text("", background_color=default_background_color)],
        [sg.Text("", background_color=default_background_color)],
        [sg.Push(background_color=default_background_color), sg.Button("Function 1", **b1), sg.Button("Function 2", **b1), sg.Button("Function 3", **b1), sg.Push(background_color=default_background_color)],
        [sg.Text("", background_color=default_background_color)],
        [sg.Text("", background_color=default_background_color)],
        [sg.Text("", background_color=default_background_color)],
        [sg.Text("", background_color=default_background_color)],
        [sg.Text("", background_color=default_background_color)],
        [sg.Text("", background_color=default_background_color)],
        [sg.Text("", background_color=default_background_color)],
        [sg.Text("", background_color=default_background_color)],   
        [sg.Push(background_color=default_background_color), sg.Button("Exit", **b2)]
    
    ]
    
    home_window = sg.Window("Program Home", layout_home, background_color="#d3d3d3", size=(580,660))
    
    return home_window


def run_function1_window():
    
    home_window.hide()
    
    event = "Starting Function1"
       
    layout = [
        [sg.Text("Calculate total spring constant for multiple springs in series...", size=(550,1), font=f2, justification="right", background_color="#d3d3d3", text_color="black")],
        [sg.Text("0.0000", size=(550,1), font=f3, justification="right", background_color="#2a2a2a", text_color="white", relief="sunken", key="_DISPLAY_")],
        [sg.Input("Enter spring constants seperated by a space...", size=(550,1), justification="left", font=f4, text_color="#949494", key="_INPUT_")],
        [sg.Text("", background_color=default_background_color, size=(21,1)), sg.Button("Calculate", **b2), sg.Button("Home", **b2)]
    ]
    
    window = sg.Window("Function1", layout, background_color="#d3d3d3", size=(580,660))  
    
    while True: 
        print(event)
        event, values = window.read()
        if event in [None, "Home", sg.WIN_CLOSED]:            
            break
        elif event == "Calculate":
            value = values["_INPUT_"]
            result = ut.calc_series_spring_const(value)         
            window["_DISPLAY_"].update(value=result)
    print(event)
    function1_active = False
    window.close()
    home_window.un_hide()
 
    return function1_active


def run_function2_window():
    
    home_window.hide()
    
    event = "Starting Function2"
       
    layout = [
        [sg.Text("Calculate total spring constant for multiple springs in parallel...", size=(550,1), font=f2, justification="right", background_color="#d3d3d3", text_color="black")],
        [sg.Text("0.0000", size=(550,1), font=f3, justification="right", background_color="#2a2a2a", text_color="white", relief="sunken", key="_DISPLAY_")],
        [sg.Input("Enter spring constants seperated by a space...", size=(550,1), justification="left", font=f4, text_color="#949494", key="_INPUT_")],
        [sg.Text("", background_color=default_background_color, size=(21,1)), sg.Button("Calculate", **b2), sg.Button("Home", **b2)]
    ]
    
    window = sg.Window("Function1", layout, background_color="#d3d3d3", size=(580,660))  
    
    while True:  
        print(event)
        event, values = window.read()
        if event in [None, "Home", sg.WIN_CLOSED]:            
            break
        elif event == "Calculate":
            value = values["_INPUT_"]
            result = ut.calc_series_spring_const(value)         
            window["_DISPLAY_"].update(value=result)
    print(event) 
    function2_active = False
    window.close()
    home_window.un_hide()
 
    return function2_active


def run_function3_window():
    
    home_window.hide()
    
    event = "Starting Function3"
    
    default_data = [ 
        
        ["0.000", "0.000", "0.000", "0.000", "0.000", "0.000"],
        ["0.000", "0.000", "0.000", "0.000", "0.000", "0.000"],
        ["0.000", "0.000", "0.000", "0.000", "0.000", "0.000"],
        ["0.000", "0.000", "0.000", "0.000", "0.000", "0.000"],
        ["0.000", "0.000", "0.000", "0.000", "0.000", "0.000"],
        ["0.000", "0.000", "0.000", "0.000", "0.000", "0.000"],
        
        ]
    
    default_headings = ["k1", "k2", "k3", "k4", "k5", "k6"]
       
    layout = [
        [sg.Text("Calculate combinations of springs in series to achieve target rate...", size=(550,1), font=f2, justification="right", background_color="#d3d3d3", text_color="black")],
        #[sg.Table("", size=(550,36), font=f5, justification="right", background_color="#2a2a2a", text_color="white", key="_DISPLAY_")],
        [sg.Push(background_color=default_background_color), sg.Table(default_data, size=(550,31), headings=default_headings, justification="centre", def_col_width = 100, background_color="#2a2a2a", text_color="white", key="_DISPLAY_"), sg.Push(background_color=default_background_color)],
        [sg.Input("Enter target spring rate...", size=(550,1), justification="left", font=f4, text_color="#949494", key="_INPUTa_")],
        [sg.Input("Enter desired number of springs...", size=(550,1), justification="left", font=f4, text_color="#949494", key="_INPUTb_")],
        [sg.Button("Calculate", **b2), sg.Button("Save .csv", **b2), sg.Button("Home", **b2)]
    ]
    
    window = sg.Window("Function3", layout, background_color="#d3d3d3", size=(580,660))  
    
    while True:   
        print(event)   
        event, values = window.read()
        if event in [None, "Home", sg.WIN_CLOSED]:            
            break
        elif event == "Calculate":
            result = ut.find_spring_combinations_series(values["_INPUTa_"], values["_INPUTb_"]) 
            window["_DISPLAY_"].update(values=result[1])
        elif event == "Save .csv":
            ut.save_csv()
    print(event)
    function3_active = False
    window.close()
    home_window.un_hide()
 
    return function3_active





home_window = make_home_window()
event ="Starting Program"

while True:
    
    if event != None:
        print(event)
            
    if not function1_active:
        event, values = home_window.read()
        if event is None or event == "Exit":
            break

    if not function1_active and event == "Function 1":
        function1_active = True
        function1_active = run_function1_window()
        
    if not function2_active and event == "Function 2":
        function2_active = True
        function2_active = run_function2_window()
            
    if not function3_active and event == "Function 3":
        function3_active = True
        function3_active = run_function3_window()  
   
    event = None
    
home_window.close()
