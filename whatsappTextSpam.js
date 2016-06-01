/**
 * Created on Tue May 24 11:23:12 2015
 * @author: HarshSharma12
 * 
 * Randomly selects a String from arr and
 * sends it to the selected user on web.whatsapp.com
 */

var arr = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
var total = arr.length;

var inputElement = document.getElementsByClassName("input")[1]; // Grabs the input field
var counter = 0;

var msgCount = 4;
var delay = 100;

function dispatch(target, eventType, char) {
   var evt = document.createEvent("TextEvent");    
   evt.initTextEvent(eventType, true, true, window, char, 0, "en-US");
   target.focus();
   target.dispatchEvent(evt);
}

function sendMessage(){
	if (counter<msgCount){
		var i = Math.floor(Math.random() * total);
		dispatch(inputElement, "textInput", arr[i]);
		
		var input = document.getElementsByClassName("icon btn-icon icon-send"); //Grabs the send button
		input[0].click();// Clicks the send button
		
		counter++;
		setTimeout(sendMessage,delay);
		console.log(counter)
	}
	else {
		dispatch(inputElement, "textInput", "Spamming end"); // Msg when the loop finish
		var input = document.getElementsByClassName("icon btn-icon icon-send");
		input[0].click();
	}
}

sendMessage();
