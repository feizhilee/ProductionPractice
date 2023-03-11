var btn = document.getElementsByClassName('btn btn-primary')[0];
var url = '/jobdetaik';
check = function () {
            if (input.value == 'change') {
                window.location = url;
            } else {
                alert('输入错误')
            }
        };
