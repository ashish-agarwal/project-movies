$(document).ready(function () {
    // the "href" attribute of .modal - trigger must specify the modal ID that wants to be triggered
    $('.modal').modal({
        complete: function () { $("#trailer-video-container").empty(); }
    });
    $('.card').hide().first().show("fast", function showNext() {
        $(this).next("div").show("fast", showNext);
    });
});

$('.modal-trigger').click(function () {
    var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
    var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
    $("#trailer-video-container").empty().append($("<iframe></iframe>", {
        'id': 'trailer-video',
        'type': 'text-html',
        'src': sourceUrl,
        'frameborder': 0
    }));

    $('#trailer').modal('open');
})
$('#trailer').on('hidden.bs.modal', function () {
    $("#trailer iframe").attr("src", $("#trailer iframe").attr("src"));
});
