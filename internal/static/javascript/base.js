function PageNumber(){
	var num = Math.floor((Math.random() * 100) + 1);
	num = Math.floor(num / 10);
	return(num);
}

function NumString(){
	var num = PageNumber();
	num = num.toString();
	num = "/static/pictures/".concat(num, ".jpg"); // The answer was just a slash... :(
	num = decodeURIComponent("url('".concat(num, "')"));
	return(num);
}

