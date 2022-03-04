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

//Now, instead of passing a callback
//a promise will be returned
function createPost(post) {
	//A promise takes in a callback.
	//Takes in two parameters
	//resolve and reject
	//resolve = when you wanna resolve a promise sucessfully
	//resolve is called
	//reject = when something goes wrong/there's some kinda error
	//reject is called
	return new Promise((resolve, reject) => {
		/*It's basically waiting and setting the time out.
         as soon as it's done. it's gonna resolve and 
         once it's resolved, then the getPosts is called*/
		setTimeout(() => {
			//It runs right after it is pushed
			//and not waiting two seconds
			posts.push(post);
			//To resolve, a const called error is created
			const error = false;

			//If you wanna to do some error checking
			if (!error) {
				resolve();
			} else {
				reject("Error: Something went wrong!");
			}
		}, 2000);
	});
}

//The callback won't be passed anymore.
//This return a promise, meaning that the ".then"
//syntax
// createPost({title: 'Post Three', body: 'This is post three'})
//     .then(getPosts)//in here the getPosts will be passed
//     .catch(err => console.log(err));

//Async / Await
//the function needs to labeled "async"
// async function init(){
//     //Await just waits for an ascyncronous process/action
//     //to complete

//    await createPost({title: 'Post Three', body: 'This is post three'});

//    //So it's basically waiting for the createPost to done
//    //and move on
//    getPosts();
// }

// init();

//Async / Await with Fetch

async function fetchUsersData() {
	const res = await fetch("https://jsonplaceholder.typicode.com/users");

	const data = await res.json();

	console.log(data);
}

fetchUsersData();

//promise.all
//IMPORTANT: The time it takes to show is how much
//the longest takes to show the values
// const promise1 = Promise.resolve('Hello World');
// const promise2 = 10;
// const promise3 = new Promise((resolve, reject) => setTimeout(resolve,2000,'Goodbye!'));

// //In Fecth it's needed to do two ".then"
// //Because, first need to format it
// //and in the next ".then" will output the data
// const promise4 = fetch('https://jsonplaceholder.typicode.com/users').then(res => res.json);

// //It takes in an array of promises
// //then, pass in "then" a callback values
// Promise.all([promise1,promise2,promise3,promise4]).then((values) =>
//  console.log(values));
