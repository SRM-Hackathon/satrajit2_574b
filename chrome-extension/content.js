// content.js
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  switch (request.type) {
    case 'openMovieModal': {
      $.get('https://api.themoviedb.org/3/movie/?api_key=', res => {
        $.get(chrome.extension.getURL('modal.html'), data => {
          $($.parseHTML(data)).appendTo('body').slideDown();

          $('#title').text(`${res.original_title} (${res.release_date.split('-')[0]})`);
          $('#runtime').text(`${res.runtime} min`);
          $('#genres').text(res['genres'].map(e => e.name).join(', '));
          $('#overview').text(res.overview);
          $('#poster').attr('src', `https://image.tmdb.org/t/p/original${res.poster_path}`);
          $(".bright_back").css("background-image", `url(https://image.tmdb.org/t/p/w400${res.backdrop_path}`);

          $(document).on('click', () => {
            const dataObj = $('#moodx-movie-suggest-card');
            if (dataObj.length)
              dataObj.slideUp(() => dataObj.remove());
          });
        });
      })
      break;
    }
  }
});