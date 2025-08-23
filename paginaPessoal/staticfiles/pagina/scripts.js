var btnPytohn = document.querySelector('#btnPython');
var btnJavaScript = document.querySelector('#btnJavaScript');
var btnDocker = document.querySelector('#btnDocker');
var btnDjango = document.querySelector('#btnDjango');
console.log(btnPytohn)
var timer;


var pytohn = document.querySelector('#respostaPython');
var javaScript = document.querySelector('#respostaJavaScript');
var docker = document.querySelector('#respostaDocker');
var django = document.querySelector('#respostaDjango');

btnPytohn.addEventListener('mouseover', function () {

    pytohn.classList.remove('hide');

})

btnPytohn.addEventListener('mouseout', function () {

    pytohn.classList.add('hide');
    
})


btnJavaScript.addEventListener('mouseover', function () {
    javaScript.classList.remove('hide');
   

})

btnJavaScript.addEventListener('mouseout', function () {
    javaScript.classList.add('hide');
})

btnDocker.addEventListener('mouseover', function () {
    docker.classList.remove('hide');
})

btnDocker.addEventListener('mouseout', function () {
    docker.classList.add('hide');
})

btnDjango.addEventListener('mouseover', function () {
    django.classList.remove('hide');
})

btnDjango.addEventListener('mouseout', function () {
    django.classList.add('hide');
})