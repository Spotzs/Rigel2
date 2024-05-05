let btnMenu = document.getElementById('btn-menu');
let mainNav = document.getElementById('main-nav');
btnMenu.addEventListener('click', function(){
  mainNav.classList.toggle('mostrar');
});

const slider = document.querySelector("#slider");
let sliderSection = document.querySelectorAll(".slider__section");
let sliderSectionLast = sliderSection[sliderSection.length -1];

const btnLeft = document.querySelector("#btn-left");
const btnRight = document.querySelector("#btn-right");

slider.insertAdjacentElement('afterbegin', sliderSectionLast);

function Next() {
  let sliderSectionFirst = document.querySelectorAll(".slider__section")[0];
  slider.style.marginLeft = "-200%";
  slider.style.transition = "all 0.5s";
  setTimeout(function(){
    slider.style.transition = "none";
    slider.insertAdjacentElement('beforeend', sliderSectionFirst);
    slider.style.marginLeft = "-100%";
  }, 500);
}

function Prev() {
  let sliderSection = document.querySelectorAll(".slider__section");
  let sliderSectionLast = sliderSection[sliderSection.length -1];
  slider.style.marginLeft = "0";
  slider.style.transition = "all 0.5s";
  setTimeout(function(){
    slider.style.transition = "none";
    slider.insertAdjacentElement('afterbegin', sliderSectionLast);
    slider.style.marginLeft = "-100%";
  }, 500);
}

btnRight.addEventListener('click', function(){
  Next();
});

btnLeft.addEventListener('click', function(){
  Prev();
});

setInterval(function(){
  Next();
}, 5000);

const agregarAlCarrito = function(producto_id, csrf_token){
    console.log(producto_id);
    console.log(csrf_token);  
    cantidad = 1;
    $.ajax({
        url: `/agregar_alcarrito/`,
        type: 'POST',
        data: {
            csrfmiddlewaretoken: csrf_token,
            // Envia los datos del formulario
            producto_id: producto_id,
            cantidad: cantidad, 
        },
        success: function (data) {
            // Muestra SweetAlert con el mensaje
            Swal.fire(data.title, data.text, data.icon);
            // Recarga la página o realiza alguna otra acción si es necesario
            setTimeout(function () {
                location.reload();
            }, 1500); // Recarga la página después de 1.5 segundos
        },
        error: function (xhr, status, error) {
            // Maneja errores si es necesario
            console.error(xhr.responseText);
        }
    });
}