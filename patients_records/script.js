function savePatients() {
	localStorage.setItem("patients", JSON.stringify(patients));
}

function loadPatients() {
	let data = localStorage.getItem("patients");
	if (data) {
		patients = JSON.parse(data);
		displayPatients();
	}
}

function deletePatient(index) {
	if (confirm("Are you sure you want to delete this patient?")) {
		patients.splice(index, 1);
		savePatients();
		displayPatients();
	}
}

function submitForm() {
	if (document.querySelector("button").innerHTML == "Save") {
		let index = document.getElementById("patient-index").value;
		let patient = patients[index];
		patient.name = document.getElementById("name").value;
		patient.age = document.getElementById("age").value;
		patient.gender = document.querySelector('input[name="gender"]:checked').value;
		patient.medicalHistory = document.getElementById("medical-history").value;
		patient.labResults = document.getElementById("lab-results").value;
		patient.treatmentPlan = document.getElementById("treatment-plan").value;
		savePatients();
		displayPatients();
		clearForm();
		document.querySelector("button").innerHTML = "Add Patient";
	} else {
		addPatient();
	}
}

loadPatients();
