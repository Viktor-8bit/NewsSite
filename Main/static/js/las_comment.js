






// {% verbatim %}


//{% verbatim %}


Vue.component('my-coment-div', {
    props: ['coment'],
    // {id: '175', text: 'ппнопо', dat: '2023-06-20 13:52:18', name: 'sus', parent: null}
    template:  `
    <div class = "com">
        <p class = "name">{{coment.name}}</p>
        <p class = "text">{{coment.text}}</p>
        <p class = "date">{{coment.dat}}</p>
        <div v-show='isLogin(1)' class="btn-group" role="group" aria-label="Basic example">'
            <button v-on:click="delete_comment(1)" class="btn btn-dark">Удалить</button>
            <button v-on:click="change_comment(1)" class="btn btn-dark">Изменить</button>
        </div>
    </div>
    `,
    methods: {
        delete_comment(id) {
        },
        change_comment(id) {
        }       
    },
    computed: {
        isLogin(name) {
            return name == 'SUS';
        }
    }
})

var comments_app = new Vue({
    el: '#comments',
    data: { 
        comentList: []
    }
})


async function get_commets() {
    const get_comments_qwery = $.get({
        url: 'get_comments?cid=' + id,     /* Куда пойдет запрос  {% url 'post' %}?&postid={{p.id}} */
        method: 'get',                                                /* Метод передачи (post или get) */
        dataType: 'json',                                             /* Тип данных в ответе (xml, json, script, html). */
        success: function(data) {
             console.log(data)
             for (let i = 0; i < data['comments'].length; i++) {
                console.log(data['comments'][i])
                comments_app.comentList.push(data['comments'][i])
             }    
        }
    });
    get_comments_qwery.done() 
}

get_commets();