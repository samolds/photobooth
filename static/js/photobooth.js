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
  var index = (lastIndex + 1) % PHOTOS.length;
  var srcElm = document.getElementById("carousel");
  var downloadingImage = new Image();

  downloadingImage.onload = function() {
    srcElm.src = this.src;

    var captionElm = document.getElementById("caption");
    captionElm.textContent = PHOTOS[index].caption;

    var timeElm = document.getElementById("time");
    timeElm.textContent = PHOTOS[index].time;
  };

  downloadingImage.src = PHOTOS[index].url;

  return index;
}

function approvePhoto(photoKey) {
  $.ajax({
    type: "POST",
    url: "/admin/approve/" + photoKey,
    success: function(data) {
      var feedbackElm = document.getElementById(photoKey + "-feedback");
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
      var feedbackElm = document.getElementById(photoKey + "-feedback");
      feedbackElm.textContent = "successfully unapproved!";
    },
    error: function(xhr, status, error) {
      console.log('failed to approve photo ' + photoKey + ': ' + xhr.responseText);
    }
  })
}
