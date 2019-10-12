chrome.browserAction.onClicked.addListener(tab => {
  // Send a message to the active tab
  chrome.tabs.query({ active: true, currentWindow: true }, tabs => {
    var activeTab = tabs[0];
    chrome.tabs.sendMessage(activeTab.id, { "message": "clicked_browser_action" });
  });
});


chrome.browserAction.onClicked.addListener(tab => {
  console.log('Hello: ');

  chrome.windows.create({url: chrome.extension.getURL("mood.html"), type: "popup", width: 360, height: 300});

  /*chrome.tabs.query({ active: true, currentWindow: true }, tabs => {
    chrome.tabs.sendMessage(tabs[0].id, { type: "openMovieModal" });
  });*/

  /*chrome.tabs.query({ active: true, currentWindow: true }, tabs => {
    chrome.tabs.sendMessage(tabs[0].id, { type: "captureMood" });
  });*/

  // chrome.browserAction.setPopup({ popup: 'popup.html' });
});