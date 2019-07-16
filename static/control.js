function showGameStartDialog(){
  updateHighscores()
  var tg=document.getElementById("userNameInput");
  var currentState = tg.style.display
  if(currentState === "inline-block"){
    tg.style.display="none";
  }
  else{
    tg.style.display="inline-block";
  }
}
function getUsername(){
  var username = document.getElementById("username").value;
  return username;

}
function getEmail(){
  var email = document.getElementById("email").value;
  return email;
}
function buildJsonString(username, email,commandText){
  var jsonData = {'command':{'action':commandText,'username':username, 'email':email}};
  var jsonString = JSON.stringify(jsonData);
  return jsonString;
}
function startTetris(){
  var username = getUsername();
  var email = getEmail();
  if(IsNullOrUndefined(username)&&IsNullOrUndefined(email)){
    username = ""
    email =""
  }
  var jsonStringToSend = buildJsonString(username,email,"switch to tetris");
  showGameStartDialog();
  xhr = new XMLHttpRequest();
  xhr.open('POST', '/');
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send(jsonStringToSend);
}
function abortAndShowStartScreen(){
  var jsonStringToSend = JSON.stringify({command:{action:"switch to startscreen"}})
  xhr = new XMLHttpRequest();
  xhr.open('POST', '/tetris_message');
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send(jsonStringToSend);
  updateHighscores()
}

function updateHighscores(){
  xhr = new XMLHttpRequest();
  xhr.open('GET', '/highscores');
   xhr.onload = function(){
    if(xhr.status === 200){
      var html = "";
      data = JSON.parse(xhr.responseText);
      data = data["score_list"];
      for(var i=0;i<data.length;i++){
        html+="<tr><td>"+data[i].name+"</td><td>"+data[i].score+"</td></tr>";
      }
      document.getElementById("table-data").innerHTML=html;
    }
  } 
  xhr.send();
}

function IsNullOrUndefined(str) {
  return (!str || 0 === str.length);
}
function IsStringEmpty(str){
  return(str.length ===0 || !str.trim());
}