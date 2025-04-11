let count =0;

let countDisplay = document.getElementById('count');
let resetButton = document.getElementById('reset');
let plusButton = document.getElementById('plus');
let minusButton = document.getElementById('minus');

function plus() {
  count +=1;
  countDisplay.textContent=count;
}

function minus() {
  count -=1;
  countDisplay.textContent =count;
}

function reset() {
  count =0;
  countDisplay.textContent =count;
}



countDisplay.textContent = count;