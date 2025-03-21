$(document).ready(function ($) {
    "use strict";

    // Book Table Slider
    var book_table = new Swiper(".book-table-img-slider", {
        slidesPerView: 1,
        spaceBetween: 20,
        loop: true,
        autoplay: {
            delay: 3000,
            disableOnInteraction: false,
        },
        speed: 2000,
        effect: "coverflow",
        coverflowEffect: {
            rotate: 3,
            stretch: 2,
            depth: 100,
            modifier: 5,
            slideShadows: false,
        },
        loopAdditionalSlides: true, // Fixed typo from original
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
    });

    // Team Slider
    var team_slider = new Swiper(".team-slider", {
        slidesPerView: 3,
        spaceBetween: 30,
        loop: true,
        autoplay: {
            delay: 3000,
            disableOnInteraction: false,
        },
        speed: 2000,
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
        breakpoints: {
            0: { slidesPerView: 1.2 },
            768: { slidesPerView: 2 },
            992: { slidesPerView: 3 },
            1200: { slidesPerView: 3 },
        },
    });

    // Menu Filter
    jQuery(".filters").on("click", function () {
        jQuery("#menu-dish").removeClass("bydefault_show");
    });

    $(function () {
        var filterList = {
            init: function () {
                $("#menu-dish").mixItUp({
                    selectors: {
                        target: ".dish-box-wp",
                        filter: ".filter",
                    },
                    animation: {
                        effects: "fade scale(0.9)", // Added scale effect for more dynamism
                        easing: "ease-in-out",
                    },
                    load: {
                        filter: ".all, .breakfast, .lunch, .dinner",
                    },
                });
            },
        };
        filterList.init();
    });

    // Mobile Menu Toggle
    jQuery(".menu-toggle").click(function () {
        jQuery(".main-navigation").toggleClass("toggled");
    });

    jQuery(".header-menu ul li a").click(function () {
        jQuery(".main-navigation").removeClass("toggled");
    });

    // Sticky Header with GSAP
    gsap.registerPlugin(ScrollTrigger);

    var elementFirst = document.querySelector(".site-header");
    ScrollTrigger.create({
        trigger: "body",
        start: "30px top",
        end: "bottom bottom",
        onEnter: () => myFunction(),
        onLeaveBack: () => myFunction(),
    });

    function myFunction() {
        elementFirst.classList.toggle("sticky_head");
    }

    // Parallax Effect
    var scene = $(".js-parallax-scene").get(0);
    var parallaxInstance = new Parallax(scene);

    // Added Dynamic Dish Box Animation
    gsap.utils.toArray(".dish-box-wp").forEach(function (dish) {
        gsap.from(dish, {
            opacity: 0,
            y: 50,
            duration: 0.8,
            scrollTrigger: {
                trigger: dish,
                start: "top 80%",
                toggleActions: "play none none reset",
            },
        });
    });
});

// Window Load Event
jQuery(window).on("load", function () {
    $("body").removeClass("body-fixed");

    // Filter Tab Animation with Color Sync
    let targets = document.querySelectorAll(".filter");
    let activeTab = 0;
    let old = 0;
    let dur = 0.4;
    let animation;

    for (let i = 0; i < targets.length; i++) {
        targets[i].index = i;
        targets[i].addEventListener("click", moveBar);
    }

    // Initial position with updated color
    gsap.set(".filter-active", {
        x: targets[0].offsetLeft,
        width: targets[0].offsetWidth,
        backgroundColor: "#e67e22", // Sync with --primary-color (orange)
    });

    function moveBar() {
        if (this.index !== activeTab) {
            if (animation && animation.isActive()) {
                animation.progress(1);
            }
            animation = gsap.timeline({
                defaults: {
                    duration: 0.4,
                },
            });
            old = activeTab;
            activeTab = this.index;
            animation.to(".filter-active", {
                x: targets[activeTab].offsetLeft,
                width: targets[activeTab].offsetWidth,
                backgroundColor: "#e67e22", // Orange for active filter
            });

            animation.to(targets[old], {
                color: "#0d0d25", // Dark color for inactive
                ease: "none",
            }, 0);
            animation.to(targets[activeTab], {
                color: "#fff", // White for active
                ease: "none",
            }, 0);
        }
    }
});