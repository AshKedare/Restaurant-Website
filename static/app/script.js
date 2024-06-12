$(function (){
    $("#button").blur(function(event){
        var screenwidth=window.innerWidth;
        if(screenwidth<768){
            $("#navbarNav").collapse('hide');
        }
    })
})

const pages = [
    "single-category.html",
    "page2.html",
    "page3.html"
  ];

  function loadRandomPage() {
    const randomIndex = Math.floor(Math.random() * pages.length);
    const randomPage = pages[randomIndex];
    window.location.href = randomPage;
  }

// menu.html
// owl carousel
// $(document).ready(function(){
//     $(".owl-carousel").owlCarousel({
//         loop: true,
//         autoplay: true,
//         autoplayTimeout: 2000,
//         autoplayHoverPause: true,
//         responsive: {
//             0: {
//                 items: 1,
//                 nav: false
//             },
//             600: {
//                 items: 2,
//                 nav: false
//             },
//             1000: {
//                 items: 3,
//                 nav: false,
//                 loop: true
//             }
//         }
//     });
// });
    

  
