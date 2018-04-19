let warned = false;

function requestListener() {
  const response = JSON.parse(this.responseText);
  console.log(response);
  if (!response.status && !warned) {
    warned = true;
    document.getElementById('status').src = 'images/cross.png';
    alert('status changed to bad!');
  }
}

function getStatus() {
  const xhttp = new XMLHttpRequest();
  xhttp.addEventListener("load", requestListener);
  xhttp.open('GET', 'http://localhost:8000/status');
  xhttp.setRequestHeader('Content-type', 'application/json');
  xhttp.send();
}

function getStatusAtInterval(time) {
  setInterval(getStatus, time);
}

window.onload = function() {
  getStatusAtInterval(3000);
};