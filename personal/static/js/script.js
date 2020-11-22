let charts = [];

$(document).ready(function () {
    resizeChart();
    fixNavbar();
    updateNavbarProgress();
    fadeIn();
    showChart();

    // Remove fade in effect from elements already in the viewport
    $('.fade-in').each(function () {
        if ($(this)[0].getBoundingClientRect().top < window.innerHeight) $(this).removeClass('fade-in');
    });

    // Toggle the hamburger menu
    $('.navbar-burger').click(function () {
        $(this).toggleClass('is-active');
        $('.navbar-menu').toggleClass('is-active');
        if ($('.navbar-menu.is-active').length === 1) {
            $('.navbar-menu.is-active').css('height', $('.navbar-menu.is-active')[0].scrollHeight);
        } else {
            $('.navbar-menu').css('height', '');
        }
        $('.navbar').toggleClass('force-shadow', $('.navbar-menu').toggleClass('.is-active'));
    });

    // Copy media link to clipboard
    $('.copy-to-clipboard').click(function () {
        copyToClipboard($(this).attr('data-url'));
        $('.copy-to-clipboard p').text('Copy URL to clipboard');
        $(this).find('p').text('Copied');
    });
    
    $(window).scroll(function () {
        fixNavbar();
        updateNavbarProgress();
        fadeIn();
        showChart();
    });

    $(window).resize(function () {
        resizeChart();
        fixNavbar();
        updateNavbarProgress();
        fadeIn();
        showChart();
    });

    // Update Bulma file input name
    $('.file-input').change(function () {
        let filename = $(this).val().split('/').pop().split('\\').pop();
        $(this).parent().find('.file-name').html(filename);
    });
});

// Fix the navbar if it has been scrolled past
function fixNavbar() {
    $('.navbar').toggleClass('is-fixed', $(window).scrollTop() > 48);
}

// Update the scrolling progress bar in navbar
function updateNavbarProgress() {
    $('.nav-progress').css('width', Math.min(100, (($(window).scrollTop() - 48) / (document.body.scrollHeight - window.innerHeight - 48)) * 100) + '%');
}

// Fade elements in when they become visible in the viewport
function fadeIn() {
    $('.fade-in').each(function () {
        if ($(this)[0].getBoundingClientRect().top < window.innerHeight) $(this).addClass('faded-in');
    });
}

// Create a Chart.js chart
function registerChart(id, options) {
    let element = document.getElementById(id);
    new Chart(element.getContext('2d'), options);
    charts.push({ element: element, options: options, shown: false });
    showChart();
}

// Replay chart creation animation when they become visible in the viewport
function showChart() {
    for (let i in charts) {
        if (!charts[i].shown && charts[i].element.getBoundingClientRect().top < window.innerHeight) {
            // This refreshes the animation
            new Chart(charts[i].element.getContext('2d'), charts[i].options);
            charts[i].shown = true;
        }
    }
}

// Update chart font size for mobile devices
function resizeChart() {
    if ($(window).width() > 768) {
        Chart.defaults.global.defaultFontSize = 20;
    } else {
        Chart.defaults.global.defaultFontSize = 10;
    }
}

// Copy contents to clipboard
function copyToClipboard(text) {
    let $temp = $('<input>');
    $('body').append($temp);
    $temp.val(text).select();
    document.execCommand('copy');
    $temp.remove();
}
