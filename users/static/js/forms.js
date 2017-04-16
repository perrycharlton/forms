jQuery(document).ready(function () {
  console.log('ready');

  submit_event();
empty()
});

function submit_event () {
  $('#login_form').click(function (e) {

    var contact_data = {};
    $('input').each(function () {
      contact_data[$(this).attr('name')] = $(this).val()
    });
    console.log(contact_data);
    main.post_data('login', contact_data).done(function (result) {
      $('#content').html(result['page'])
    });
    e.preventDefault()
  })
}

function empty () {
  $('input').prop('required', true).each(function (e) {
    if ($(this).val()) {
      console.log('all forms ok')
    } else {
      console.log('please make sure forms are not empty')
    }
  })
}

// var form_validate = function () {

  function field_empty (select, elem) {
    select = $('input[type=password]');
    elem = $('#pswd_info');
    select.keyup(function () {
      // keyup code here
    }).focus(function () {
      elem.show()
    }).blur(function () {
      elem.hide()
    });
    return field_empty()
  }

  function field_len () {
    if (pswd.length < 8) {
      $('#length').removeClass('valid').addClass('invalid')
    } else {
      $('#length').removeClass('invalid').addClass('valid')
    }
    return field_len()
  }

  function letter(strg) {
   return strg.match(/[A-z]/)
  }
function capital (strg) {
  return strg.match(/[A-Z]/)
}


function number(strg){
    return strg.match(/\d/)
}

// }