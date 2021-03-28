$(document).ready(function () {
    /* sticky nav*/
    $('.js--section-features').waypoint(function (direction) {
        if (direction == "down") {
            $('nav').addClass('sticky');
        } else {
            $('nav').removeClass('sticky');
        }
    }, {
        offset: '95%'
    });
    /*scroll nav*/
    $('.js--scroll-to-plans').click(function () {
        $('html, body').animate({
            scrollTop: $('.js--section-plans').offset().top
        }, 1000);
    });

    $('.js--scroll-to-start').click(function () {
        $('html, body').animate({
            scrollTop: $('.js--section-features').offset().top
        }, 1000);
    });


    $(function () {
        $('a[href*=#]:not([href=#])').click(function () {
            if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') &&
                location.hostname == this.hostname) {
                var target = $(this.hash);
                target = target.length && target || $('[name=' + this.hash.slice(1) + ']');
                if (target.length) {
                    $('html,body').animate({
                        scrollTop: target.offset().left
                    }, 2000);
                    return false;
                }
            }
        });
    });

    $('.js--wp-1').waypoint(function (direction) {
        $('.js--wp-1').addClass('animate__fadeIn');
    }, {
        offset: '50%'
    });

    $('.js--wp-2').waypoint(function (direction) {
        $('.js--wp-2').addClass('animate__fadeInLeft');
    }, {
        offset: '50%'
    });
    $('.js--wp-3').waypoint(function (direction) {
        $('.js--wp-3').addClass('animate__fadeInLeft');
    }, {
        offset: '50%'
    });
    $('.js--wp-4').waypoint(function (direction) {
        $('.js--wp-4').addClass('animate__fadeInUp');
    }, {
        offset: '50%'
    });
    $('.js--wp-5').waypoint(function (direction) {
        $('.js--wp-5').addClass('animate__fadeInRight');
    }, {
        offset: '50%'
    });
    $('.js--wp-6').waypoint(function (direction) {
        $('.js--wp-6').addClass('animate__slideInLeft');
    }, {
        offset: '50%'
    });
    $('.js--wp-7').waypoint(function (direction) {
        $('.js--wp-7').addClass('animate__slideInRight');
    }, {
        offset: '50%'
    });
    $('.js--wp-8').waypoint(function (direction) {
        $('.js--wp-8').addClass('animate__slideInRight');
    }, {
        offset: '50%'
    });
    $('.js--wp-9').waypoint(function (direction) {
        $('.js--wp-9').addClass('animate__pulse');
    }, {
        offset: '50%'
    });

    /*Mobile nav*/
    $('.js--nav-icon').click(function () {
        var nav = $('.js--main-nav');

        var icon = $('.js--nav-icon i');
        nav.slideToggle(200);
        if (icon.hasClass('ion-navicon-round')){
            icon.addClass('ion-ios-close-outline');
            icon.removeClass('ion-navicon-round');
        }else{
             icon.removeClass('ion-ios-close-outline');
            icon.addClass('ion-navicon-round');
        }
        
    });
});
