/**
 * Created on Sun May 22 16:43:23 2015
 * @author: HarshSharma12
 * 
 * Sends emojis to a user on web.whatsapp.com
 * 	1) Select a user/group/list
 * 	2) Paste script in console
*/

var msgCount = 100;
var delay = 10;
var emojiTab = 1;	/* From 1 to 8 */
var emojiNumber = 1  ;	/* 0 not allow */

function getElementByXpath(path) { return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; }

var counter = 0;

function sendMessage() {         
	setTimeout(function () {
		var emojiButton = getElementByXpath('//*[@id="main"]/footer/div/button[1]');
		emojiButton.click(); // Click on the emoji buuton
			setTimeout(function () {
				var emojiTab = Math.floor(Math.random() * 8) + 1; // Randomize emoji tab selection
				var tab = getElementByXpath('//*[@id="main"]/footer/span/div/div[1]/button[' + emojiTab + ']');
				tab.click(); // Select the tab
				setTimeout(function () {
					var emojiNumber = Math.floor(Math.random() * 5) + 1  //Randomize the emaoji to be selected
					var emoji = getElementByXpath('//*[@id="main"]/footer/span/div/span/div/div/span[' + emojiNumber + ']');
					emoji.click(); //Insert the emoji
					setTimeout(function () {	
						var sendButton = getElementByXpath('//*[@id="main"]/footer/div/button[2]');
						sendButton.click(); // Click on send button
						setTimeout(function () {
							counter++;
							if (counter < msgCount) {
								sendMessage(); 
							}
						}, delay);
					}, delay);
				}, delay);
			}, delay);
		}, delay);
	}

sendMessage();
