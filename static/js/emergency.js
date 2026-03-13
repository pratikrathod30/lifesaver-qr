document.addEventListener("DOMContentLoaded",function(){

const loadingBox=document.getElementById("loadingBox");
const hospitalList=document.getElementById("hospitalList");

if(window.location.search.includes("lat=")){
loadingBox.style.display="none";
hospitalList.style.display="block";
}

if(navigator.geolocation){

navigator.geolocation.getCurrentPosition(function(position){

let lat=position.coords.latitude;
let lon=position.coords.longitude;

if(!window.location.search.includes("lat=")){

window.location.href=`/emergency/${window.profileUUID}?lat=${lat}&lon=${lon}`;

}

});

}

});