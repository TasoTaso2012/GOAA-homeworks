
//1
let i = 1;
while (i <= 10) {
console.log(i );
i++;
}


//2
let o = 2; 
while (o <= 20) {
console.log(o ); 
    o += 2; 
 }


 //3
let  u= 1; 
let sum = 0;

while (u <= 10) {
sum += u; 
u++; 
}
 console.log("The sum of numbers from 1 to 10 is: " + sum);


 //4
let y = 10;
while (y >= 1) {
console.log(y);
y--;
}


//5
let randomNumber = 46; 
let guess = 0;

while (guess !== randomNumber) {
    guess = (prompt("Guess a number between 1 and 50:"));

    if (guess < randomNumber) {
        alert("your numbrr is too low. Try again!");
    } else if (guess > randomNumber) {
        alert("your number is too high. Try again!");
    } else if (guess = randomNumber) {
        alert("you guessed the correct number! ");
    } else {
        alert("enter a number.");
    }
}