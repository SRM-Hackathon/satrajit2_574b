// content.js
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  switch (request.type) {
    case 'openMovieModal': {
      const dataObj = $('#moodx-movie-suggest-card');
      if (!dataObj.length) {
        $.get('https://api.themoviedb.org/3/movie/475557?api_key=836ac18a40145ed02495aa8f3c6346a9', res => {
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
      }
      break;
    }
    /*case 'captureMood': {
      chrome.windows.create({url: chrome.extension.getURL("mood.html"), type: "popup"});
      /*const dataObj = $('#moodx-mood-capture-card');
      if (!dataObj.length) {
        $.get(chrome.extension.getURL('mood.html'), data => {
          $($.parseHTML(data)).appendTo('body').slideDown();
          $(document).on('click', () => {
            const dataObj = $('#moodx-movie-suggest-card');
            if (dataObj.length)
              dataObj.slideUp(() => dataObj.remove());
          });
        });
      }
      break;
    }*/
  }
});