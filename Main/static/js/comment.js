
        csrf = $.cookie('csrftoken')
        $.ajaxSetup({
        headers: {
            'X-CSRF-TOKEN': $(csrf).attr('content')
            }
        });
        console.log( $('meta[name="csrf-token"]'))

        class Comment {
            constructor(name, date, text) { // имя, дата, текст
                this.name = name;
                this.date = date;
                this.text = text;
            }
        }

        let name = ''

        function set_const_name(_name) {
            username = _name
        }

        let post_id
        Login = $.cookie('log')
        Password = $.cookie('pass')
        async function _get_com_from_server(data){                                      /* функция которая будет выполнена после успешного запроса.  */
                    comments = document.getElementById('comments')
                    comments.innerHTML = ''
                    for (var i = 0; i < data['comments'].length; i++) {
                        element = data['comments'][i];
                        text = element['text']
                        dat = element['dat']
                        name = element['name']
                        parent = element['parent']
                        coment_id = element['id']
                        comment = `
                                    <div class = "com" id=${coment_id}>
                                        <p class = "name">${name}</p>
                                        <p class = "text">${text}</p>
                                        <p class = "date">${dat}</p>
                                    `
                        // проверка на возможность удаления
                        if (name == username) {
                            comment += '<div class="btn-group" role="group" aria-label="Basic example">'
                            comment += `<button onclick="delete_comment(${coment_id})" class="btn btn-dark">Удалить</button>`
                            comment += `<button onclick="change_comment(${coment_id})" class="btn btn-dark">Изменить</button>`
                            comment += '</div>'
                        }
                        comment += '</div>'
                        $('div.comments').add(comment).appendTo(comments)
                    }
                }

        async function get_comment(id) {
            post_id = id
            comments = document.getElementById('comments')
            // $.ajax({
            $.get({
                url: 'http://127.0.0.1:8000/post/get_comments?cid=' + id,     /* Куда пойдет запрос */
                method: 'get',                                                /* Метод передачи (post или get) */
                dataType: 'json',                                             /* Тип данных в ответе (xml, json, script, html). */
                success: function(data) { _get_com_from_server(data) }
            });
        }

        async function delete_comment(id) {
            const del = $.get({
                url: 'http://127.0.0.1:8000/post/delete_comment?&id=' + id + '&pid=' + post_id,     /* Куда пойдет запрос */
                method: 'get',                                                /* Метод передачи (post или get) */
                dataType: 'json',                                             /* Тип данных в ответе (xml, json, script, html). */
                success: function(data) { _get_com_from_server(data) }
            })
            console.log(del)
            del.then(function() { alert('комментарий удалён') });
        }

        async function change_comment(id) {

            main_element = $(`[class='com'][id='${id}']`)
            stand_com = new Comment(main_element.children('.name').text(), main_element.children('.date').text(), main_element.children('.text').text())
            main_element.children('p').remove()
            main_element.children('div').remove()
            comment_change = `
                                    <p class = "name">${stand_com.name}</p>
                                    <textarea class = "text" id = '${id}t'>${stand_com.text}</textarea>
                                    <p class = "date">${stand_com.date}</p>
                                    <div class="btn-group" role="group" aria-label="Basic example">
                                        <button onclick="Ok(${id})" class="btn btn-dark">ОК</button>
                                        <button onclick='Clancell(${id}, "${stand_com.name}",  "${stand_com.text}",  "${stand_com.date}" )' class="btn btn-dark">Отмена</button>
                                    </div>
                            `
            main_element.append(comment_change)
        }

        async function Ok(id) {
            text = document.getElementById(`${id}t`).value
            $.get({
                url: 'http://127.0.0.1:8000/post/change_comment?&id=' + id + '&pid=' + post_id + '&text=' + text,     /* Куда пойдет запрос */
                method: 'get',                                                /* Метод передачи (post или get) */
                dataType: 'json',                                             /* Тип данных в ответе (xml, json, script, html). */
                success: function(data) { _get_com_from_server(data) }
            });
        }

        async function Clancell(id, name, text, date) {
            console.log('функция работает')
            main_element = $(`[class='com'][id='${id}']`)
            main_element.children('textarea').remove()
            main_element.children('p').remove()
            main_element.children('div').remove()
            comment_clacel =
                    `
                    <p class = "name">${name}</p>
                    <p class = "text">${text}</p>
                    <p class = "date">${date}</p>
                    <div class="btn-group" role="group" aria-label="Basic example">
                        <button onclick="delete_comment(${id})" class="btn btn-dark">Удалить</button>
                        <button onclick="change_comment(${id})" class="btn btn-dark">Изменить</button>
                    </div>
                    `
            main_element.append(comment_clacel)
        }

