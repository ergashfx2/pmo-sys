function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue
}


document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('add-task').addEventListener('click', function () {
        var form = document.getElementById('phase-form')
        form.insertAdjacentHTML('beforeend', `<div><label> Task nomini yozing :
            <input class="form-control mb-4 task-inputs" type="text" name="task">
            </label><br></div>`);
    })

    document.getElementById('save-all-data').addEventListener('click', function () {
        var data = {}
        var tasks = []
        data['phase_name'] = document.getElementById('phase-input').value
        document.querySelectorAll('.task-inputs').forEach(task => {
            tasks.push(task.value)

        })
        data['tasks'] = tasks
        var ref = window.location.href
        var token = getCookie('csrftoken')
fetch(`${ref}/add-phase/`, {
    method: "POST",
    headers: {
        "Content-type": "application/json",
        "X-CSRFToken": token
    },
    body: JSON.stringify(data),
}).then(res => {
    location.reload()
});

    })

})

document.addEventListener('DOMContentLoaded', function () {
    var select = document.getElementById('input-select');
    var array = []
    var button = document.getElementById('do-buton')
    var confirm_delete = document.getElementById('confirm')
    var delete_button = document.getElementById('delete-button')
    var all_delete_buttons = document.querySelectorAll('.delete-button')
    var delButton = document.getElementById('del-confirm')
    var selectedFiles = document.querySelectorAll('.del-files')
    var delFiles = []
    delButton.addEventListener('click', function () {

        selectedFiles.forEach(file => {
            file.addEventListener('change', function () {
                if (file.checked === true) {
                    delFiles.push(file.id)
                }
                if (file.checked === false) {
                    delFiles = delFiles.filter(item => item !== file.id)
                }
            })
        })


        all_delete_buttons.forEach(value => {
            value.addEventListener('click', function () {
                confirm_delete.addEventListener('click', function () {
                    fetch(`delete/${value.id}`).then(res => {
                        location.reload()
                    })

                })
            })
        })


        document.querySelectorAll("input[type='checkbox']").forEach(value => {
            value.addEventListener('change', function () {
                if (value.checked === true) {
                    array.push(value.id)
                }

            })
        })




        delete_button.addEventListener('click', function () {
            for (i = 0; i < array.length; i++) {
                fetch(`delete-user/${array[i]}`).then(res => {
                    location.reload()
                })
            }

        })

        button.addEventListener('click', function () {
            if (select.value === 'Bloklash') {
                for (i = 0; i < array.length; i++) {
                    fetch(`block/${array[i]}`).then(res => {
                        location.reload()
                    })
                }
            }
            if (select.value === 'Blokdan ochish') {
                for (i = 0; i < array.length; i++) {
                    fetch(`unblock/${array[i]}`).then(res => {
                        location.reload()
                    })
                }
            }
        })
    })
})

document.addEventListener('DOMContentLoaded',function (){
    document.getElementById('icons-panel{{ data.phase_id }}')
})

document.addEventListener('DOMContentLoaded', function() {
    document.addEventListener('click', function(event) {
        if (event.target.classList.contains('icon-buttons')) {
            var phase_id = event.target.classList[3];
            var element = document.getElementById('phase' + phase_id).textContent.toString()
            document.getElementById('phase'+ phase_id).innerHTML = `<input type="text" value="${element}"/>`
            document.getElementById('icons-panel' + phase_id ).innerHTML = `<i id="icon-save" class="fa-solid fa-circle-check btn btn-outline-secondary mt-1"></i>`
        }

    document.getElementById('icon-save').addEventListener('click',function (){
        var new_input = document.getElementById('phase'+ phase_id).children.item(0).value
                var token = getCookie('csrftoken')
        fetch(`update-phase/${phase_id}`,{
                method: "POST",
    headers: {
        "Content-type": "application/json",
        "X-CSRFToken": token
    },
    body: JSON.stringify({'phase_name':new_input}),


        }).then(res=>{
            location.reload()
        })
    })

    });
});

