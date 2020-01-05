function PageNumber(){
	var num = Math.floor((Math.random() * 100) + 1);
	num = Math.floor(num / 10);
	return(num);
}

function NumString(num){
	num = num.toString();
	num = "/static/pictures/".concat(num, ".jpg");
	num = decodeURIComponent("url('".concat(num, "')"));
	return(num);
}

function SetString(bol){
	if (bol){
		var pgnum = NumString(10);
	}else{
		var num = PageNumber();
		var pgnum = NumString(num);
	}
	return(pgnum);
}