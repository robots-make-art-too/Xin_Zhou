function setAlarm(event){
    l = parseFloat(event.target.value);
    switch (l){
        case 0.1 :chrome.browserAction.setBadgeText({text: 'ON'});  break;
        case 0.3 :chrome.browserAction.setBadgeText({text: 'WORK'}); break;
    }
    chrome.alarms.create({delayInMinutes: l});
    chrome.storage.sync.set({long: l});
    window.close();
}
function clearAlarm(){
    chrome.browserAction.setBadgeText({text: ''});
    chrome.alarms.clearAll();
    window.close();
}

document.getElementById('tryMe').addEventListener('click', setAlarm);
document.getElementById('startMe').addEventListener('click', setAlarm);
document.getElementById('cancel').addEventListener('click', clearAlarm);
