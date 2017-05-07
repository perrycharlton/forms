jQuery(document).ready(function ($) {
    console.log("I'am here");
    $('ul li').on("click", function (e) {
       var link = $(this).data('link');
        quiz.side_menu(link);
    });

});
var quiz = (function () {

    function side_menu(link) {
         // $('ul li').on("click", function (e) {
        // var link = item.data('link');
        if (link == 'quiz/shuffle') {
            var question = JSON.parse(localStorage.getItem("questions"));

            var quiz_html = quiz.make_page(main.shuffle(question));
            $('#quiz_page').html(quiz_html)
                .on("click", "#quiz_save_btn", function () {
                    quiz.save_quiz();
                });


        } else {
            main.get_data(link).done(function (result) {
                if (result.sub_content) {
                    $('#sub_content').html(result.sub_content);
                }
                if (result.side_menu) {
                    $('#side_menu').html(result.side_menu);
                }
                if (result.questions) {
                    quiz_html = quiz.update_questions(result);

                    $('#quiz_container').html(quiz_html)
                        .on("click", "#quiz_save_btn", function () {
                            quiz.save_quiz();
                        });
                }
            })
        }

    // });

    }

    function update_questions(result) {
            // Store information
            for (var x in ['questions', 'unit', 'user']) {
                if (result[x]) {
                    localStorage.setItem(x, JSON.stringify(result[x]));
                }
                else {
                    console.log("could not store: ", x)
                }
            }
            return quiz.make_page(result.questions);
    }
    function save_quiz() {
        var r_selected = $('.quiz_quest');
        var unit = localStorage.getItem('unit');
        var question = {};
        r_selected.each(function (index) {
            question[index] = {
                "question": $(this).data('q_no'),
                "answer": "none"
            };
        });
        $(".quiz_input:checked").each(function () {
            var g = $(this).val().split('');
            question[g[0]] = {
                "question": g[0],
                "answer": g[1]
            };
        });
        question['unit'] = localStorage.getItem('unit');
        question['user'] = JSON.parse(localStorage.getItem('user'));
        return question;
    }
    function search_text(text, s1, s2) {
        text = search_text1(text);
        return text.replace(s1 + s2, s1 + '<sup>' + s2 + '</sup>')
    }

    // Replace oc for centigrade
    function search_text1(text) {
        var s2 = String.fromCharCode(176);
        return text.replace('0C', s2)
        // });

    }
    function activate_radio(answers) {
        $('.form-check-input').click(function (e) {
            var ans = $(this).val();
            var question = $(this).prop('name');
            var score = "";
            $.each(answers, function (k, v) {
                if (v['no'] == question) {
                    score = v['scores'][ans - 1]
                }
            });
            $('i[data-opt=opt' + question + ']').removeClass();
            if (score === 1) {
                $('#question' + question + ans).addClass('fa fa-check text-success');
            } else if (score === 0) {
                $('#question' + question + ans).addClass('fa fa-times text-danger');
            }
        });
    }
    function import_quiz(elem) {
        $(elem).on("click", function () {

        })
    }

    // These 2 function build the quiz from the json text that is supplied
    function make_page(data) {
        console.log(data);
        var page = "";
        for (var prop in data) {
            // var question_no = data[prop]['no'];
            var question = search_text(data[prop]['question'], "mm", "2");
            page += "<div class='quiz_quest' data-q_no='" + (parseInt(prop) + 1) + "'>" +
                "Q " + (parseInt(prop) + 1) + ":  " + question + "</div>";
            page += "<div>LO" + data[prop]['LO'] + "</div>";
            for (var opt_no in data[prop]['options']) {
                var opt_text = data[prop]['options'][opt_no]['option'];
                // var question_no = data[prop]['no'];
                page += build_opts(opt_text, opt_no, parseInt(prop));
            }

        }
        page += '<div class="quiz_quest">' +
            '<input type="button" id="quiz_save_btn"  class="btn btn-danger" value="Submit">' +
            '</div>';
        return page;
    }

    function build_opts(text, opt, no) {
        var html = search_text(text, 'mm', '2');
        var input = '<input type="radio" class="quiz_input" data-number="' + no + '" name="radio' + no + '" value="' + opt + '">';
        var label = '<label class="form-check-label radio inline">' + input + html + '</label>';
        return '<div class="form-check form-inline quiz_input">' + label + '</div>';
    }


    return {
        activate_radio: activate_radio,
        save_quiz: save_quiz,
        search_text: search_text,
        search_text1: search_text1,
        make_page: make_page,
        import_quiz: import_quiz,
        update_questions: update_questions,
        side_menu: side_menu
    }


})();
