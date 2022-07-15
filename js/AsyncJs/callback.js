const posts = [
	{ title: "Post One", body: "This is post one" },
	{ title: "Post Two", body: "This is post two" },
];

//We are mimicking how it is to fetch from a server
//So it should takes a couples seconds to respond the request
//and so on

function getPosts() {
	//It takes a callback function
	//And it takes a some amount of time of delay
	setTimeout(() => {
		//The purpose is to get the post and
		//get them on the page
		let output = "";

		posts.forEach((post, index) => {
			//For each post will be added to the
			//output variable
			output += `<li>${post.title}</li>`;
		});
		//Now it will be inserted to the body
		document.body.innerHTML = output;
	}, 1000);
}

function createPost(post, callback) {
	setTimeout(() => {
		//It runs right after it is pushed
		//and not waiting two seconds
		posts.push(post);
		callback();
	}, 2000);
}

createPost({ title: "Post Three", body: "This is post three" }, getPosts);
