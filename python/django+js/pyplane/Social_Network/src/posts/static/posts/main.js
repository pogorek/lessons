const postsBox = document.getElementById("posts-box");
const spinnerBox = document.getElementById("spinner-box");
const loadBtn = document.getElementById("load-btn");
const endBox = document.getElementById("end-box");
const alertBox = document.getElementById("alert-box");

// var for url - detail page
const url = window.location.href;

// new post form
const postForm = document.getElementById("post-form");
const title = document.getElementById("id_title");
const body = document.getElementById("id_body");
const csrf = document.getElementsByName("csrfmiddlewaretoken");
console.log("csrf: ", csrf[0].value);

// function from django csrf documentation
const getCookie = (name) => {
	let cookieValue = null;
	if (document.cookie && document.cookie !== "") {
		const cookies = document.cookie.split(";");
		for (let i = 0; i < cookies.length; i++) {
			const cookie = cookies[i].trim();
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === name + "=") {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
};
const csrftoken = getCookie("csrftoken");

// func show message if post was deleted and there is value in local storage
const deleted = localStorage.getItem("title");
if (deleted) {
	handleAlerts("danger", `Post "${deleted}" has been deleted`);
	localStorage.clear();
}

// function to like button - like/unlike
const likeUnlikePosts = () => {
	// transform elements to array with spread operator
	const likeUnlikeForms = [...document.getElementsByClassName("like-unlike-forms")];
	// listen for submit of each form
	likeUnlikeForms.forEach((form) =>
		form.addEventListener("submit", (e) => {
			// we dont want form to submit, we want to create our own logic - send data with ajax
			e.preventDefault();
			// get id from "data-" id of the form that has been clicked/submitted
			const clickedId = e.target.getAttribute("data-form-id");
			// get button element that has been clicked
			const clickedBtn = document.getElementById(`like-unlike-${clickedId}`);

			$.ajax({
				type: "POST",
				url: "/like-unlike/",
				data: {
					csrfmiddlewaretoken: csrftoken,
					pk: clickedId,
				},
				success: function (response) {
					console.log(response);
					clickedBtn.textContent = response.liked ? `Unlike (${response.count})` : `Like (${response.count})`;
				},
				error: function (error) {
					console.log(error);
				},
			});
		})
	);
};

// var for posts loaded
let visible = 3;

// Function to get data about posts and show it in div
const getData = () => {
	$.ajax({
		type: "GET",
		url: `/data/${visible}`,
		success: function (response) {
			// whole response
			console.log(response);
			// passed arg data
			console.log(response.data);
			// post objects in data
			const data = response.data;
			console.log(data);
			setTimeout(() => {
				spinnerBox.classList.add("not-visible");
				data.forEach((el) => {
					postsBox.innerHTML += `
	<div class="card mb-2">
		<div class="card-body">
			<h5 class="card-title">${el.title}</h5>
			<p class="card-text">${el.body}</p>
		</div>
		<div class="card-footer">
			<div class="row">
				<div class="col-2">
					<a href="${url}${el.id}" class="btn btn-primary">Details</a>
				</div>
				<div class="col-2">
					<form class="like-unlike-forms" data-form-id="${el.id}">
						<button href="#" class="btn btn-primary" id="like-unlike-${el.id}">${el.liked ? `Unlike (${el.count})` : `Like (${el.count})`}</button>
					</form>
				</div>
			</div>
		</div>
	</div>
					`;
				});
				likeUnlikePosts();
			}, 700);
			console.log(response.size);
			// checking for posts count number
			if (response.size === 0) {
				endBox.textContent = "No posts added yet...";
			} else if (response.size <= visible) {
				loadBtn.classList.add("not-visible");
				endBox.textContent = "No more posts to load";
			}
		},
		error: function (error) {
			console.log(error);
		},
	});
};

// listener to show posts
loadBtn.addEventListener("click", () => {
	spinnerBox.classList.remove("not-visible");
	visible += 3;

	getData();
});

// listener for new post form
postForm.addEventListener("submit", (e) => {
	// prevent submitting , prevent reload the page
	e.preventDefault();

	$.ajax({
		type: "POST",
		url: "",
		data: {
			csrfmiddlewaretoken: csrf[0].value,
			title: title.value,
			body: body.value,
		},
		success: function (response) {
			console.log(response);
			// insertAdjacentHTML() method inserts a text as HTML, into a specified position.
			//
			postsBox.insertAdjacentHTML(
				"afterbegin",
				`
	<div class="card mb-2">
		<div class="card-body">
			<h5 class="card-title">${response.title}</h5>
			<p class="card-text">${response.body}</p>
		</div>
		<div class="card-footer">
			<div class="row">
				<div class="col-2">
					<a href="#" class="btn btn-primary">Details</a>
				</div>
				<div class="col-2">
					<form class="like-unlike-forms" data-form-id="${response.id}">
						<button href="#" class="btn btn-primary" id="like-unlike-${response.id}">Like (0)</button>
					</form>
				</div>
			</div>
		</div>
	</div>
			`
			);
			// add function so we can like new post without reloading page
			likeUnlikePosts();
			// hide modal after submitting new post
			$("#addPostModal").modal("hide");
			// display message in alertBox
			handleAlerts("success", "New post added!");
			// reset form after adding to remove values from form if er open it again
			postForm.reset();
		},
		error: function (error) {
			console.log(error);
			// hide modal after submitting new post
			$("#addPostModal").modal("hide");
			// display message in alertBox
			handleAlerts("danger", "ups... something went wrong");
		},
	});
});

getData();
