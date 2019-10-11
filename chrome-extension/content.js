// content.js
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  switch (request.type) {
    case "openMovieModal": {
      // Add code to show modal
      console.log('Adding modal!');
      $.get(chrome.extension.getURL('modal.html'), data => {
        $($.parseHTML(data)).appendTo('body').slideDown();;
        $(document).on('click', () => {
          const dataObj = $('#moodx-movie-suggest-card');
          console.log('clicked fuk');
          if (dataObj.length)
            dataObj.slideUp(() => dataObj.remove());
        });
      });
      break;
    }
  }
});