console.log("post detail");

const postBox = document.getElementById("post-box");
const alertBox = document.getElementById("alert-box");

// buttons
const backBtn = document.getElementById("back-btn");
const updateBtn = document.getElementById("update-btn");
const deleteBtn = document.getElementById("delete-btn");

// to fill update form
const titleInput = document.getElementById("id_title");
const bodyInput = document.getElementById("id_body");

// for ajax url
const url = window.location.href + "data/";
const updateUrl = window.location.href + "update/";
const deleteUrl = window.location.href + "delete/";

// for update/delete form
const updateForm = document.getElementById("update-form");
const deleteForm = document.getElementById("delete-form");
const csrf = document.getElementsByName("csrfmiddlewaretoken");

const spinnerBox = document.getElementById("spinner-box");

backBtn.addEventListener("click", () => {
	history.back();
});

// function for loading post data to page
$.ajax({
	type: "GET",
	url: url,
	success: function (response) {
		console.log(response);
		const data = response.data;

		if (data.logged_in !== data.author) {
			console.log("different");
		} else {
			console.log("the same");
			updateBtn.classList.remove("not-visible");
			deleteBtn.classList.remove("not-visible");
		}

		titleEl = document.createElement("h3");
		titleEl.setAttribute("class", "mt-3");
		titleEl.setAttribute("id", "title");

		bodyEl = document.createElement("p");
		bodyEl.setAttribute("class", "mt-1");
		bodyEl.setAttribute("id", "body");

		titleEl.textContent = data.title;
		bodyEl.textContent = data.body;

		postBox.appendChild(titleEl);
		postBox.appendChild(bodyEl);

		titleInput.value = data.title;
		bodyInput.value = data.body;

		spinnerBox.classList.add("not-visible");
	},
	error: function (error) {
		console.log(error);
	},
});

// event list for update post
updateForm.addEventListener("submit", (e) => {
	// dont submit form and dont reload page
	e.preventDefault();

	const title = document.getElementById("title");
	const body = document.getElementById("body");

	$.ajax({
		type: "POST",
		url: updateUrl,
		data: {
			csrfmiddlewaretoken: csrf[0].value,
			title: titleInput.value,
			body: bodyInput.value,
		},
		success: function (response) {
			console.log(response);
			handleAlerts("success", "post has been updated");
			title.textContent = response.title;
			body.textContent = response.body;
		},
		error: function (error) {
			console.log(error);
		},
	});
});

// event list for delete post
deleteForm.addEventListener("submit", (e) => {
	e.preventDefault();

	$.ajax({
		type: "POST",
		url: deleteUrl,
		data: {
			csrfmiddlewaretoken: csrf[0].value,
		},
		success: function (response) {
			window.location.href = window.location.origin;
			localStorage.setItem("title", titleInput.value);
		},
		error: function (error) {
			console.log(error);
		},
	});
});
