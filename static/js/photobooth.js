LAST_INDEX = 0;
PHOTOS = [];

window.setInterval(function() {
  getLatestPhotoSet();
  if (PHOTOS.length > 0) {
    LAST_INDEX = updatePhoto(LAST_INDEX);
  }
}, 10000);

function getLatestPhotoSet() {
  $.ajax({
    type: "GET",
    url: "/api/allapprovedphotos",
    success: function(data) {
      PHOTOS = data;
    },
    error: function(xhr, status, error) {
      console.log('failed to get photos: ' + xhr.responseText);
    }
  })
}

function updatePhoto(lastIndex) {
  index = (lastIndex + 1) % PHOTOS.length;
  srcElm = document.getElementById("carousel");
  srcElm.src = PHOTOS[index];
  return index;
}
