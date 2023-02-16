from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class AddPatientScreen(Screen):
    def save_patient_record(self):
        # Add code here to save the patient record to the database
        name = self.ids.name_input.text
        dob = self.ids.dob_input.text
        med_history = self.ids.med_history_input.text
        treat_plan = self.ids.treat_plan_input.text
        print(f"Record saved for {name}")

class PatientRecordApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(AddPatientScreen(name='add_patient'))
        return screen_manager

if __name__ == '__main__':
    PatientRecordApp().run()
