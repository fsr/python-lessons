function codereplace(snippet) {
    var frontmatter = '<div class="repl-top">\
<div align="right">\
<button class="run-button" disabled>connecting</button>\
</div>\
</div>\
<div class="repl">\
<div class="repl-code">\
<pre class="input">\
';

    var postmatter = '</pre>\
</div>\
<div class="repl-result">\
<p><strong>Output:</strong></p>\
<pre class="out"></pre>\
</div>\
</div>';

    var code = frontmatter + snippet + postmatter;
    return code;
}

function init() {
    var elements = document.getElementsByClassName('exec');
    for (var i=0; i < elements.length; i++) {
        var snippet = elements[i].innerHTML;
        elements[i].innerHTML = codereplace(snippet);
    }
}

window.onload = function () {
    init();


    repl = new ReplitClient('api.repl.it', '80', 'python3', TOKEN);


    repl.connect().then(
        function () {
            document.querySelector('.run-button').innerHTML = 'RUN';
            document.querySelector('.run-button').disabled = false;
            start();
        },
        function () {
            document.querySelector('.run-button').innerHTML = 'failed';
            document.querySelector('.run-button').disabled = true;

        }
    );

    function start() {
    document.querySelector('.run-button').onclick = function () {
        document.querySelector('.run-button').disabled = true;
        document.querySelector('.run-button').innerHTML = 'running';
        repl.evaluate(
            document.querySelector('.input').innerHTML, {
                stdout: function (str) {
                    document.querySelector('.out').innerHTML += str;
                }
            }
        ).then(
            function (err) {
                console.log(err);
            }
        );
        document.querySelector('.run-button').innerHTML = 'RUN';
        document.querySelector('.run-button').disabled = false;
    };
}
}
