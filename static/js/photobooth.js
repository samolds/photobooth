LAST_INDEX = 0;
PHOTOS = [];


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
  srcElm.src = PHOTOS[index].url;

  captionElm = document.getElementById("caption");
  captionElm.textContent = PHOTOS[index].caption;

  timeElm = document.getElementById("time");
  timeElm.textContent = PHOTOS[index].time;

  return index;
}

function approvePhoto(photoKey) {
  $.ajax({
    type: "POST",
    url: "/admin/approve/" + photoKey,
    success: function(data) {
      feedbackElm = document.getElementById(photoKey + "-feedback");
      feedbackElm.textContent = "successfully approved!";
    },
    error: function(xhr, status, error) {
      console.log('failed to approve photo ' + photoKey + ': ' + xhr.responseText);
    }
  })
}

function unapprovePhoto(photoKey) {
  $.ajax({
    type: "POST",
    url: "/admin/unapprove/" + photoKey,
    success: function(data) {
      feedbackElm = document.getElementById(photoKey + "-feedback");
      feedbackElm.textContent = "successfully unapproved!";
    },
    error: function(xhr, status, error) {
      console.log('failed to approve photo ' + photoKey + ': ' + xhr.responseText);
    }
  })
}
