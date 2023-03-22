#import dependencies 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

#class defifnition
class MainApp(App):
    def build(self):
        #change icon
        self.icon = "calc.png"
        #list of operators
        self.operators = ["/", "*", "-", "+"]
        self.last_was_operator = None
        self.last_button = None

        #the layout of the calculator
        main_layout = BoxLayout(orientation = "vertical" )

        #the solution screen style
        self.solution = TextInput(background_color = "black", foreground_color = "white", multiline=False, halign="right", font_size=55, readonly=True)

        #add the self.solution to the main calculator layout
        main_layout.add_widget(self.solution)

        #creating input buttons
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "C", "-"]
        ]

        #looping through buttons
        for row in buttons:
            #creating a layout for buttons
            h_layout = BoxLayout()
            #loop through the buttons
            for label in row:
                #styling the buttons and setting positions and size
                button = Button(
                    text = label, font_size=30, background_color = "grey",
                    pos_hint = {"center_x": 0.5, "center_y": 0.5},
                )
                #make buttons functional
                button.bind(on_press = self.on_button_press)

                #add buttons in the horizontyal layout
                h_layout.add_widget(button)

                #insert h-layout in main layout
            main_layout.add_widget(h_layout)

        #styling the equal button
        equal_button = Button(
            text ="=", font_size=30, background_color = "grey",
            pos_hint = {"center_x": 0.5, "center_y": 0.5},
        )
        #setting the equal button to the on_solution function
        equal_button.bind(on_press=self.on_solution)

        #add the equal button to the main_layout widget
        main_layout.add_widget(equal_button)

        #return the entire main_layout and all the widgets
        return main_layout
    
    #function for when button is pressed
    def on_button_press(self, instance):
        #initial value for screen
        current = self.solution.text
        #initial value for button
        button_text = instance.text

        #if button_text = C, return empty string
        if button_text == 'C':
            self.solution.text = ""
        else:
            #don't add two operators together return none
            if current and (self.last_was_operator and button_text in self.operators):
                return
            #if screen is not empty and the inputted text is an operator return none
            elif current == "" and button_text in self.operators:
                return
            else:
                #if all is good, new_text would be current screen plus the input
                new_text = current + button_text
                #store new value in the screen
                self.solution.text = new_text

        #set default values
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators
    
    #set up the function
    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            #set solution in the screen
            self.solution.text = solution


if __name__ == "__main__":
    app = MainApp()
    app.run()

                     