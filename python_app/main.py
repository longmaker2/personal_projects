from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '550')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

class PatientRecordsApp(App):
    def build(self):
        # Set background color
        Window.clearcolor = (0.3, 0.3, 0.3, 1)

        # Create custom title
        title_layout = GridLayout(cols=1, size_hint=(1, None), height=100)
        title_label = Label(text='Patient Records', font_size=36)
        title_layout.add_widget(title_label)

        # Create main layout
        main_layout = GridLayout(cols=2, spacing=10, padding=30)
        main_layout.add_widget(Label(text='Patient Name'))
        self.patient_name = TextInput(multiline=False)
        main_layout.add_widget(self.patient_name)

        main_layout.add_widget(Label(text='Patient ID'))
        self.patient_id = TextInput(multiline=False)
        main_layout.add_widget(self.patient_id)

        main_layout.add_widget(Label(text='Doctor Name'))
        self.doctor_name = TextInput(multiline=False)
        main_layout.add_widget(self.doctor_name)

        main_layout.add_widget(Label(text='Symptoms'))
        self.symptoms = TextInput(multiline=True)
        main_layout.add_widget(self.symptoms)

        main_layout.add_widget(Label(text='Diagnosis'))
        self.diagnosis = TextInput(multiline=True)
        main_layout.add_widget(self.diagnosis)

        main_layout.add_widget(Label(text='Prescription'))
        self.prescription = TextInput(multiline=True)
        main_layout.add_widget(self.prescription)

        # Create buttons layout
        buttons_layout = GridLayout(cols=2, size_hint_y=None, height=50)
        buttons_layout.add_widget(Button(text='Save', on_press=self.save_record))
        buttons_layout.add_widget(Button(text='Get Records', on_press=self.get_records))

        # Combine all layouts into one
        root_layout = GridLayout(cols=1)
        root_layout.add_widget(title_layout)
        root_layout.add_widget(main_layout)
        root_layout.add_widget(buttons_layout)

        return root_layout

    def save_record(self, instance):
        print(f"Patient Name: {self.patient_name.text}")
        print(f"Patient ID: {self.patient_id.text}")
        print(f"Doctor Name: {self.doctor_name.text}")
        print(f"Symptoms: {self.symptoms.text}")
        print(f"Diagnosis: {self.diagnosis.text}")
        print(f"Prescription: {self.prescription.text}")

    def get_records(self, instance):
        # TODO: Implement method for retrieving patient records from a database or file
        pass

if __name__ == '__main__':
    PatientRecordsApp().run()
