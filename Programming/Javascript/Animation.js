var xPos = 400; //starting position of the shooting star
var yPos = 0;   //starting position of the shooting star
var starSize = 60;  
var planetSize = 70;
var sizeDecrease = 1; //size decrease of the shooting star with movement
var xMovement = 0; //horizontal speed of the star
var yMovement = 0; //vertical speed of the star
var explosionRadius = 0;
var explosionRadiusIncrease = 0;
var increase = true;



var draw = function(){
    background(55, 56, 61);
    
    // drawing the planet
    fill(240, 232, 233);
    ellipse(85,330,planetSize,planetSize);
    
    //drawing the shooting star
    fill(255, 242, 0);
    ellipse(xPos, yPos, starSize, starSize);
	
	//drawing the explosion blast
	fill(255, 123, 0);
	ellipse(xPos,yPos,explosionRadius,explosionRadius-30);
	
	//defining the course and decreasing size of the star until collision point
	if(xPos>90){
        xMovement = 2;
        yMovement = 3/(xPos/150);
        sizeDecrease = 0.3;
        explosionRadiusIncrease = 0;
	}
	
	//stopping the star at collision point and starting the explosion
	else if(xPos<=90 && increase ===true){
	    xMovement = 0;
	    yMovement = 0;
	    explosionRadiusIncrease = 3;
	}
	
	//receding the explosion blast when reached a certain size
	if(explosionRadius>200 && increase === true){
	    increase = false;
	    explosionRadiusIncrease = -5;
	    planetSize = 0;
	}
	
	//implementing animation
	xPos -= xMovement;
	yPos += yMovement;
	starSize -= sizeDecrease;
	explosionRadius += explosionRadiusIncrease;
};

