function borderRadius() {
    let image = document.getElementById('poster');
    image.style.borderRadius = '15px';
}

function changeBoxShadow() {
    let image = document.getElementById('poster');
    image.style.boxShadow = '0px 0px 50px 0px rgb(70, 70, 70)';
}


function changePicture() {
    let image = document.getElementById('poster');
    image.src = 'nogravity.jpg'; // Replace with the actual path to the new image
}



document.getElementById('bs').addEventListener('click', changeBoxShadow);
document.getElementById('cp').addEventListener('click', changePicture);