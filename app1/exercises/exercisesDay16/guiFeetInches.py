import PySimpleGUI as gui

feet_label = gui.Text("Enter feet: ")
feet_input = gui.Input()

inches_label = gui.Text("Enter inches: ")
inches_input = gui.Input()

convert_button = gui.Button("Convert")

window = gui.Window("Convertor", 
                    layout= [[feet_label, feet_input],
                            [inches_label, inches_input],
                            [convert_button]])

window.read()
window.close()

