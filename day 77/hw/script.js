function cbc() {
    document.body.style.backgroundColor = 'lightblue'; 
}

function cbtx() {
    document.querySelectorAll('button').forEach(button => {
        button.style.color = 'red'; 
    });
}

function changeImage() {
    let image = document.getElementById('image');
    image.src = 'img2.jpg'; 
}