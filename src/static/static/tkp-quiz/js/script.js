// Open window
const baseOpenWindowHandler = (url) => {
  return window.open(url, '', 'width=600,height=700')
}

// Open Window and reload page when window closed
const openWindowAndReloadPage = (url) => {
  let window = baseOpenWindowHandler(url)
  setInterval(() => {
    if (window.closed) {
      location.reload();
    }
  }, 500);
}
