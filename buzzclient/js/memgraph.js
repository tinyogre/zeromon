X = [0];
Y = [0];
NEXT = 0;

getSample = function(data) {
    X[NEXT] = NEXT;
    Y[NEXT] = data['total'];
    NEXT += 1;

    r.clear()
    r.text(160, 10, "Memory Usage").attr(txtattr);
    r.linechart(100, 10, 690, 580, X, Y, {axis: "0 0 1 1"});
}

window.onload = function() {
	jQuery.error = console.error;

    r = Raphael("holder"),
        txtattr = { font: "12px sans-serif" };
    r.setSize(800, 600);

    window.setInterval(function() {
            $.ajax(
                {
                  url: '/sample', 
                        dataType: 'json',
                        success: getSample,
                        error: function(xhr, status, fff) { alert('error'); }
                }
                );
        }, 5000);
};

