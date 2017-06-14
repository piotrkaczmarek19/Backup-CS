$(document).ready(function(){
	var newLink = document.createElement('a');

	newLink.href = "http://www.wikipedia.fr";

	document.querySelector('body').appendChild(newLink);

	var newLinkText = document.createTextNode("This link is created w/ Jquery");
	newLink.appendChild(newLinkText);
});