var prevVScroll = $(window).scrollTop()
var showing = true

$(window).scroll(function() {
  var vScroll = $(window).scrollTop()
  $('.parallax-bg')
    .css('background-position', 'center ' + -vScroll * 0.6 + 'px')
    .css('opacity', 1 - vScroll / ($('.parallax-bg').height() * 2))

  if (vScroll <= prevVScroll) {
    $('header').css('top', '0px')
    showing = true
  } else {
    $('header').css('top', '-55px')
    showing = false
  }

  prevVScroll = vScroll
})

$(window).mousemove(function(e) {
  if (e.pageY - $(window).scrollTop() < 30) {
    $('header').css('top', '0px')
  } else if (!showing) {
    $('header').css('top', '-55px')
  }
})

$(document).ready(function() {
  $('.subscribe-btn').click(function() {
    $([document.documentElement, document.body]).animate(
      {
        scrollTop: $('#home-subscribe').offset().top
      },
      500
    )
  })
})
