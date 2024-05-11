/*=============== SHOW MENU ===============*/
const navMenu = document.getElementById('nav-menu'),
      navToggle = document.getElementById('nav-toggle'),
      navClose = document.getElementById('nav-close')

/*===== MENU SHOW =====*/
/* Validate if constant exists */
if(navToggle){
    navToggle.addEventListener('click', () =>{
        navMenu.classList.add('show-menu')
    })
}

/*===== MENU HIDDEN =====*/
/* Validate if constant exists */
if(navClose){
    navClose.addEventListener('click', () =>{
        navMenu.classList.remove('show-menu')
    })
}

/*=============== REMOVE MENU MOBILE ===============*/
const navLink = document.querySelectorAll('.nav__link')

function linkAction(){
    const navMenu = document.getElementById('nav-menu')
    // When we click on each nav__link, we remove the show-menu class
    navMenu.classList.remove('show-menu')
}
navLink.forEach(n => n.addEventListener('click', linkAction))

/*=============== CHANGE BACKGROUND HEADER ===============*/
function scrollHeader(){
    const header = document.getElementById('header')
    // When the scroll is greater than 50 viewport height, add the scroll-header class to the header tag
    if(this.scrollY >= 50) header.classList.add('scroll-header'); else header.classList.remove('scroll-header')
}
window.addEventListener('scroll', scrollHeader)

/*=============== SHOW SCROLL UP ===============*/
function scrollUp(){
    const scrollUp = document.getElementById('scroll-up');
    // When the scroll is higher than 200 viewport height, add the show-scroll class to the a tag with the scroll-top class
    if(this.scrollY >= 200) scrollUp.classList.add('show-scroll'); else scrollUp.classList.remove('show-scroll')
}
window.addEventListener('scroll', scrollUp)

/*=============== SCROLL SECTIONS ACTIVE LINK ===============*/
const sections = document.querySelectorAll('section[id]')

function scrollActive(){
    const scrollY = window.pageYOffset

    sections.forEach(current =>{
        const sectionHeight = current.offsetHeight
        const sectionTop = current.offsetTop - 50;
        sectionId = current.getAttribute('id')

        if(scrollY > sectionTop && scrollY <= sectionTop + sectionHeight){
            document.querySelector('.nav__menu a[href*=' + sectionId + ']').classList.add('active-link')
        }else{
            document.querySelector('.nav__menu a[href*=' + sectionId + ']').classList.remove('active-link')
        }
    })
}
window.addEventListener('scroll', scrollActive)

/*=============== SCROLL REVEAL ANIMATION ===============*/
const sr = ScrollReveal({
    distance: '60px',
    duration: 2500,
    delay: 400,
    // reset: true
})

sr.reveal(`.home__header, .section__title`,{delay: 600})
sr.reveal(`.home__footer`,{delay: 700})
sr.reveal(`.home__img`,{delay: 900, origin: 'top'})

sr.reveal(`.sponsor__img, .products__card, .footer__logo, .footer__content, .footer__copy`,{origin: 'top', interval: 100})
sr.reveal(`.specs__data, .discount__animate`,{origin: 'left', interval: 100})
sr.reveal(`.specs__img, .discount__img`,{origin: 'right'})
sr.reveal(`.case__img`,{origin: 'top'})
sr.reveal(`.case__data`)

const agregarAlCarrito = function(producto_id, csrf_token) {
    const cantidadInput = $(`#input${producto_id}`);
    const cantidad = parseInt(cantidadInput.val());
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

const AbrirModalCarrito = function() {
        
    // function AbrirModalCarrito() {
        // console.log('probando')
        // $.ajax({
        //     url: "{% url 'carrito' %}",
        //     success: function(data) {
        //         $('#carritoModal .modal-body').html(data);
        //         $('#carritoModal').modal('show');
        //     }
        // });
       $('#carritoModal .modal-body').html('<p>hola</p>');
    $('#carritoModal').modal('show');
    }
    
    $('.btn-primary').click(function() {
        AbrirModalCarrito();
    });

$(document).ready(function() {
    $('#btn-carrito').click(function(e) {
        e.preventDefault();
        $.ajax({
            url: "{% url 'carrito' %}",
            type: 'GET',
            success: function(data) {
                Swal.fire({
                    title: 'Mi Carrito',
                    html: data.carrito_html,
                    showCloseButton: true,
                    showCancelButton: false,
                    focusConfirm: false
                });
            },
            error: function() {
                Swal.fire('Error', 'Hubo un error al cargar el carrito', 'error');
            }
        });
    });
});