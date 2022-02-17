chrome.alarms.onAlarm.addListener(state);

function state() {
    chrome.browserAction.setBadgeText({ text: '' });
    chrome.storage.sync.get(['long'], function (item) {
        switch (item.long) {
            case 0.1:
                chrome.notifications.create({
                    type: 'basic',
                    iconUrl: 'img/T48.png',
                    title: 'Test',
                    message: 'Click To Reapt',
                    buttons: [
                        { title: 'Reapt' }
                    ]
                })
                stateType = 'ON';
            break;
            case 0.2:
                chrome.notifications.create({
                    type: 'basic',
                    iconUrl: 'img/T48.png',
                    title: 'Welcome Back',
                    message: 'Time To Work\! 25 Minutes Countdown Start',
                    buttons: [
                        { title: 'Start' }
                    ]
                })
                chrome.storage.sync.set({long: 0.3});
                stateType = 'WORK';
            break;
            case 0.3:
                chrome.notifications.create({
                    type: 'basic',
                    iconUrl: 'img/T48.png',
                    title: 'Rest Time',
                    message: 'Let\'s Take a Break\!',
                    buttons: [
                        { title: 'Back Soon' }
                    ]
                })
                chrome.storage.sync.set({long: 0.2});
                stateType = 'REST';
            break;
        }
    });
}

chrome.notifications.onButtonClicked.addListener(function() {
    chrome.storage.sync.get(['long'], function(item) {
      chrome.browserAction.setBadgeText({text: stateType});
      chrome.alarms.create({delayInMinutes: item.long});
    });
  });