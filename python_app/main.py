import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class PatientRecordsApp(App):
    def build(self):
        layout = GridLayout(cols=2)

        # Add labels and text input widgets for each field in the patient record
        layout.add_widget(Label(text='Patient Name'))
        self.patient_name = TextInput()
        layout.add_widget(self.patient_name)

        layout.add_widget(Label(text='Patient ID'))
        self.patient_id = TextInput()
        layout.add_widget(self.patient_id)

        layout.add_widget(Label(text='Doctor Name'))
        self.doctor_name = TextInput()
        layout.add_widget(self.doctor_name)

        layout.add_widget(Label(text='Symptoms'))
        self.symptoms = TextInput()
        layout.add_widget(self.symptoms)

        layout.add_widget(Label(text='Diagnosis'))
        self.diagnosis = TextInput()
        layout.add_widget(self.diagnosis)

        layout.add_widget(Label(text='Prescription'))
        self.prescription = TextInput()
        layout.add_widget(self.prescription)

        # Add buttons for saving and retrieving patient records
        save_button = Button(text='Save')
        save_button.bind(on_press=self.save_record)
        layout.add_widget(save_button)

        get_button = Button(text='Get Records')
        get_button.bind(on_press=self.get_records)
        layout.add_widget(get_button)

        return layout

    def save_record(self):
        print(f"Patient Name: {self.patient_name.text}")
        print(f"Patient ID: {self.patient_id.text}")
        print(f"Doctor Name: {self.doctor_name.text}")
        print(f"Symptoms: {self.symptoms.text}")
        print(f"Diagnosis: {self.diagnosis.text}")
        print(f"Prescription: {self.prescription.text}")

    def get_records(self):
        # TODO: Implement method for retrieving patient records from a database or file
        pass
