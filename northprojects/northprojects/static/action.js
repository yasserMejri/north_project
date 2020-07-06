$(document).ready(function(){
    $(".services__one").hide();
    $('.services__list__title').click(function(){
        // alert($(this).attr('name'))
        $(".services__one").hide();
        $("#" + $(this).attr('name')).fadeIn('slow');
        $('.services__list__title').removeClass('active');
        $(this).addClass('active');
    });
    $('.header__small').hide();
    $('a.icon').click(function() {
        $('.header__small').toggle()
    });
    $('.header').addClass($('#theme').attr('class')+'-header');
    $('.logo-svg').addClass($('#theme').attr('class')+'-logo');
    $('a.icon').addClass($('#theme').attr('class')+'-icon');

    $('img.logo-svg').each(function(){
        var $img = jQuery(this);
        var imgID = $img.attr('id');
        var imgClass = $img.attr('class');
        var imgURL = $img.attr('src');

        $.get(imgURL, function(data) {
                // Get the SVG tag, ignore the rest
                var $svg = $(data).find('svg');

                // Add replaced image's ID to the new SVG
                if(typeof imgID !== 'undefined') {
                    $svg = $svg.attr('id', imgID);
                }
                // Add replaced image's classes to the new SVG
                if(typeof imgClass !== 'undefined') {
                    $svg = $svg.attr('class', imgClass+' replaced-svg');
                }

                // Remove any invalid XML tags as per http://validator.w3.org
                $svg = $svg.removeAttr('xmlns:a');

                // Check if the viewport is set, if the viewport is not set the SVG wont't scale.
                if(!$svg.attr('viewBox') && $svg.attr('height') && $svg.attr('width')) {
                    $svg.attr('viewBox', '0 0 ' + $svg.attr('height') + ' ' + $svg.attr('width'))
                }

                // Replace image with new SVG
                $img.replaceWith($svg);

            }, 'xml');

    });
    

});