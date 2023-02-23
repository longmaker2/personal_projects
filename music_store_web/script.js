// Validate form input
function validateForm() {
    var media = document.getElementById("media").value;
    var title = document.getElementById("title").value;
    var description = document.getElementById("description").value;
    if (media == "" || title == "" || description == "") {
        alert("All fields must be filled out");
        return false;
    }
}

// Upload the files
function uploadFiles() {
	var file = document.getElementById("media").files[0];
	var formData = new FormData();
	formData.append("file", file);
	formData.append("title", document.getElementById("title").value);
	formData.append("description", document.getElementById("description").value);
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "upload.php", true);
	xhr.onload = function () {
		if (xhr.status === 200) {
			alert("File uploaded successfully");
			document.getElementById("media").value = "";
			document.getElementById("title").value = "";
			document.getElementById("description").value = "";
		} else {
			alert("Error uploading file");
		}
	};
	xhr.send(formData);
}

// Play the media file
function playMedia() {
	var audio = document.getElementsByTagName("audio")[0];
	var video = document.getElementsByTagName("video")[0];
	var sourceAudio = document.getElementsByTagName("source")[0];
	var sourceVideo = document.getElementsByTagName("source")[1];
	if (audio.canPlayType(sourceAudio.type)) {
		audio.src = sourceAudio.src;
		audio.load();
		audio.play();
	} else if (video.canPlayType(sourceVideo.type)) {
		video.src = sourceVideo.src;
		video.load();
		video.play();
	} else {
		alert("Media format not supported");
	}
}

document.getElementById("media").addEventListener("change", validateForm);
document.getElementById("upload-form").addEventListener("submit", function (e) {
	e.preventDefault();
	uploadFiles();
});
document.getElementById("play-button").addEventListener("click", playMedia);
