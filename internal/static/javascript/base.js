function PageNumber(){
	var num = Math.floor((Math.random() * 100) + 1);
	num = Math.floor(num / 10);
	return(num.toString()+ '.jpg');
}

function NumString(){
	var num = PageNumber();
	num = 'url("static/pictures/' + num + '")';
	return(num);
}