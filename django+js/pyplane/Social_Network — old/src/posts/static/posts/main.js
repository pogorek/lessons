// console.log("HEELL");
// console.log(document);

// const test = document.getElementById("test");
const posts2 = document.getElementById("posts2");
const spinner = document.getElementById("spinner-box");

// console.log(test);

// setTimeout(() => {
// 	test.textContent = "hru?";
// }, 2000);

$.ajax({
	type: "GET",
	url: "/posts-json/",
	success: function (response) {
		// whole response
		console.log(response);
		// passed arg data
		console.log(response.data);

		const data = JSON.parse(response.data);
		// post objects in data
		console.log(data);

		// settimeout just to see if its working
		// for each object add it to post2 inner html
		setTimeout(() => {
			data.forEach((el) => {
				posts2.innerHTML += `${el.fields.body}<br>`;
			});
			spinner.classList.add("not-visible");
		}, 2000);
	},
	error: function (error) {
		console.log(error);
	},
});
