/**
 * Created by perry on 12/03/17.
 */

var csrftoken = $('meta[name=csrf-token]').attr('content');
$.ajaxSetup({
  beforeSend: function (xhr, settings) {
    if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type)) {
      xhr.setRequestHeader('X-CSRFToken', csrftoken)
    }
  }
});

jQuery(document).ready(function ($) {
  // csrftoken();
  $('#content button').click(function (e) {
    var link = $(this).data('link');
    main.get_data(link).done(function (result) {
      console.log(result);
       $('#content').html(result.page);
      })

  });


});


function ativate_menu () {
  $('#main-menu div').click(function (e) {
    var myFile = $(this).data('link');
    if (myFile == 'logout') {
      menu_setup({'auth': false})
    }
    main.get_data(myFile)
      .done(function (data) {
        $('#content').html(data.page);
        if (typeof data['data'] != 'undefined') {
          // localStorage.setItem('quiz', data.data.questions);
          quiz.activate_radio(data.data.questions);
          quiz.save_quiz(data.data.questions);
          quiz.search_text('mm', '2');
          quiz.search_text1()
          // console.log(data.data)
        }
      });
    e.preventDefault()
  })
}
function menu_setup (info) {
  if (info['auth']) {
    console.log(info['auth']);
    sessionStorage.setItem('user', info['first']);
    $('.hidden').removeClass('invisible');
    $('#logged_in').html('Welcome ' + info['first']);
    $('#login_btn').data('link', 'logout');
    $('#login_btn>button').text('Log Out');

    $('#user_img').attr('src', '/static/images/' + info.src)

  }
  else {
    $('.hidden').addClass('invisible');
    $('#logged_in').html('You are not logged in');
    $('#login_btn').data('link', 'login');
    $('#login_btn>button').text('Login')
  }
}

var main = (function () {

  // Function to the css rule
  var checkSize = function (elem) {
    if ($(elem).width() >= 980) {
      console.log($(elem).width());
      return true
    }
  };

  var getHeight = function (item) {
    var maxHeight = $(item).map(function () {
      console.log($(this).height());
      return $(this).height()
    }).get();
    $(item).height(Math.max.apply(null, maxHeight))
  };

  var first_upper = function (str) {
    return (str + '').toLowerCase().replace(/\b[a-z]/g, function ($1) {
      return $1.toUpperCase()
    })
  };

  var get_data = function (myFile) {
    return $.get('/' + myFile)
  };

  var post_data = function (myFile, data) {
    console.log(myFile, data);
    return $.post('/' + myFile, data)
  };

  return {
    getHeight: getHeight,
    checkSize: checkSize,
    first_upper: first_upper,
    get_data: get_data,
    post_data: post_data
  }

})();





