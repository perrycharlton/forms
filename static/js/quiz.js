 var quiz = (function () {

        function save_quiz(answers) {
            $('#quiz_btn').on("click", function () {
                var r_selected = $('.form-question');
                var unit = $('#clue_title').data('unit');
                var question ={};
                var total_score = 0, no_questions = r_selected.length + 1;
                r_selected.each(function () {
                    question[$(this).data('question')] = {"question":$(this).data('question')};
                });
                $(".form-check-input:checked").each(function () {
                    var a = $(this).val();
                    var q_no = $(this).prop('name');
                    $.each(answers, function (k, v) {
                        if(v['no'] === parseInt(q_no)) {
                            total_score += parseInt(v['scores'][a - 1]);
                            question[q_no]['results'] = {
                                'answer': a,
                                'score': v['scores'][a - 1]
                            }
                        }
                    });
                });
                var results = {
                    "questions": question,
                    "score": total_score,
                    "number": no_questions,
                    "first": sessionStorage.getItem('user')
                };
                main.post_data('test/test_result', JSON.stringify(results))
                    .done(function (data) {
                        console.log(data);
                        $("#content").html(data.page);
                    });
                console.log(question, total_score, no_questions, total_score/no_questions*100)
            });
        }

        function search_text(s1, s2) {
            $(".form-question").html(function (index, html) {

//                var s1 = 'mm', s2 = '2';
                return html.replace(s1 + s2, s1 + '<sup>' + s2 + '</sup>')
            });

        }
        function search_text1() {
            $(".form-question").html(function (index, html) {
                console.log(html);
                var s2 = String.fromCharCode(176);
                return html.replace('0C', s2)
            });

        }

        function activate_radio(answers) {
            $('.form-check-input').click(function (e) {
                var ans = $(this).val();
                var question = $(this).prop('name');
                var score = "";
                $.each(answers, function (k, v) {
                    if(v['no'] == question){
                        score = v['scores'][ans-1]
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

        return {
            activate_radio: activate_radio,
            save_quiz: save_quiz,
            search_text: search_text,
            search_text1: search_text1
        }


    })();
