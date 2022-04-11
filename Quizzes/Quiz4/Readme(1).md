# Quiz 4 - we came; we built; we interacted

This is the last `quiz`... you've made it through:

- Quiz 1: `setup and soundbeats`
  - do you remember your first template clone into robots?
  - what about your reaction to `how do I make an emotion with code`? 
  - or changing `just one thing`?

- Quiz 2: `classy robot family`
  - do you know where your `classy` children are?
  - what about their parents? 
  - do you remember how similar `OOP` is when we looked at `processing.py` vs `p5.js`?

- Quiz 3: `message in a bottle`
  - you are no longer limited to `one file - one location`!
  - smile! There will be a surprize sent to your `GPS` next week!
  - interacting digitally across space and time (in just a few lines..)

---

## Let's look back

Our notes from last class (_THE_ [`last class`](last-class.md)) might be helpful to reference while answering the `Quiz 4` questions.

Here we go! Just answer in this `readme.md` file - you can even do it online, remember? (grab a copy of the repo first though!). 

>
> You do not need to write long answers. In fact, keep them short, keep them clear. 
>
> Point-form, jot-notes, paraphrasing, snippets, links.
>

---

### Week 01

1. setup
   - What is a repo and why do we use them?
         A space where we can store our programming project.
         Public repo can be downloaded by everyone.
         It can record changes and if needed we can restore the previous state
2. version control
   - Why do we use version control? How did you manage making use of this? Be specific.
         Recording all the changes.
         If we made a huge mistake, we can find and use the older or orginal version.
3. processing
   - Why is processing similar across _at least_ three languages (Java, Python, JavaScript)? What might be the point of this?
         
---

### Week 02

1. IDEs
   - What IDEs did you use over the last 3.5 months?
         Processing and Visual Studio Code
2. UI & UI Elements
   - Give me a specific example of where you considered UI in any of your course content submissions?
         Since UI stands for user interface, then in Lab3, when creating a chating APP, the interface which user use to chat through is the UI
3. JSON
   - What _exactly_ is JSON? Decide how you want to answer this.
         JSON stands for JavaScript Object Notation, it is often used for data transmission from server to webpage, we usually use it when uploading an extension to web in this course.
4. CLI & GUI
   - Give me at least 3 ways we used GitHub and explain the difference between local and remote copies of a repo.
         —— 
         1.We use GitHub to upload assignments and download course content
         2.We use GitHub to establish groups
         3.We use GitHub to upload AR markers and generate QR code so that the user could jump directly into the VR interface without accessing to the development page
         ——
         Difference between local and remote copies of a repo: local repo can be edited at anytime with or without the internet, and no one else will see the changes until uploading to the remote computer, and local repo could 
   easily separated a secondary page with different files stored while the remote can't separate completely.
5. debug
   - What magical number-letter combo helps us debug in the browser? (What is a cross-origin error?) How can I display console content?
         —— Press F12 when using Windows, and Cmd+Opt+I in Mac.A corss-origin error(CORS) occured usually when the request was blocked due to violating the CORS security rules.
         —— Use method console.log() in HTML page to output contents into web.

---

### Week 03

1. Browsers, extensions
   - Interaction with the browser through extensions required at least 2 things. Tell me what you think they are. There is a correct answer, and I talked about it in a January video.
         —— a manifest.Json file, this is necessary for every extentions to communicate with web server.
         —— have at least a HTML file to support the extension
2. DOM, selectors, elements
   - How are these related? 
   DOM stands for 'Document object model', which let user to divide content they want easier, and the content could be distinguished by id, class, dev group or tag etc. Use selectors to sepcify the specific group that been created and 
   elements are some basic groups that the tag name can not be changed, for example <p>, <h1> <html>.
3. JavaScript OOP
   - Show me 2 specific ways you used an OOP style in your course content submissions. Where did I use OOP in my p5.js updates?
      —— LAb2: create different robot members with different object parameters, like in different color or shapes.
      —— AR mini game: when creating a character, set up character's characteristic like name, dialogue and tools.
         You used OOP in drawing those ellipse, set up the basic shape by using the ellipse method and repeat several times.
---

### Week 04

1. Python
   - Show me where you completed the `try these` instructions from [Feb 3](https://github.com/robots-make-art-too/EECS_1720/tree/main/General-Content/Content_by_Week/Week04/Week04-live_code)

   https://github.com/BRANDDY/trythese

2. Describe and list common attributes of any object-oriented programming language.
          —— Encapsulation
            Put all var in a class. 
            And private var in a class that do not need to be provided externally.
            This way can restrict unreasonable change of var, then easy to modify and maintain.
         —— Inheritance
            An child class object can use the public functions from the parent class.
            Also, the child class can add more functions that the parent does not have.
         —— Polymorphism
            A same function, used in different ways, depending on different objects.
            such as: 
               parent.name();
               child.name();    

---

### Week 05

1. Python OOP
   - Write a python class for a `classy robot` that has the following: a name, an age, and can start and stop dancing when you clap. You can do it in under 10 lines (it can be pseudo-code like).

class classyRobot:
    def __init__(self,n,a):
       self.name = n
       self.age = a
       self.clap = False;

    def dance():
        //dance
robot=classyRobot(Jack,10)
def mouseClicked():
        if (clap):
            robot.clap = False
        else:
            robot.clap = True
            robot.dance()


2. APIs
   - What API did you connect with in Lab 2? Briefly explain how you integrated interactivity within your code. 
      —— tweepy
      —— Using the access_token of tweepy to apply for the data, account information and functions using permition from twitter. And then get the data return.
---

### Week 06

1. server-client
   - Give me an example of an interaction done `client-side` and an interaction done `server-side`.
      When loging into an account, we enter the user name and password on client-side, server will check for a match.

2. local hosting
   - what is the difference between dragging an index.html file into your browser and opening an index.html file using localhost? Do you remember the number equivalent to localhost? 
      —— 
      dragging:
         only display the page of the html
      localhost:
         connect html, js and other files, so this way can use the functions that are not from this index.html file. 
      —— 127.0.01:8000
   
---

### Week 07

1. GitHub pages
   - What is a `deployment` in this context? What is a branch and why are they used for contributing to repos? 
      —— deployment
         Creating and update the static web(github page)
      —— branch
         Branch is to fork and save the overall process of modifying records. 
         Branch is not affected by other branches, so multiple modifications can be made in the same database at the same time. 

2. Augmented Reality
   - What makes AR possible? What is needed in a code context?
      —— image and location base
      —— Ar.js API
      		<script src="https://raw.githack.com/AR-js-org/AR.js/master/aframe/build/aframe-ar-nft.js"></script>
		      <script src="https://unpkg.com/aframe-look-at-component@0.8.0/dist/aframe-look-at-component.min.js"></script>

---

### Week 08

1. aesthetics
   - Give me a specific example of where you considered aesthetic design in any of your course content?
         Quiz 3: A sculpture composed of multiple models
2. APIs for extending integration
   - Identify where in _your_ code, for Quiz 1, Quiz 2, Quiz 3, Lab 1, Lab 2, Lab 3 that either you used an API or where you _could_ integrate an API (it could be that we added API access in the lecture example and you used the same - still identify this).
         Quiz1: js API(Random)
         Quiz2: Processing API(arraylist)
         Quiz3: AR.js
         Lab 1: Windows API
         Lab 2: Tweepy
         Lab 3: js API(Element)


---

### Week 09

1. OOP elements & interactive JavaScript
   - How did we interact with webpage elements using code?
         In HTML file, using selectors to specify the behavior of specific elements in webpage, for instance the <p> or <h1> 
2. integrating multi-code & external content
   - What kind of event-based interactions are possible in web-based applications? 
         The user-action triggered event, timing event(date and time ), receive and send message from server to client site.
---

### Week 10

1. Levels of location - local to geo
   - How did we instantiate multiple geo-locations and dynamic object loading in our AR code?
         By setting up the x,y and z coordinates of each locations, and using a-scene to instantiate each model to provides basic recgonization informations.
2. app hosting
   - What is important about constructing an app? How does this relate to its `environment`?
         The purpose to write codes in app is to provide the user a better using experience and provide the coder a easier way to publish their project. 
         When publishing an app on internet, it's much more easier to collect clients using experience and tendentious resources so that the host could make corresponding changes fatser.
---

### Week 11

1. interaction along the virtuality-reality continuum
   - Why are `id`'s important for interaction?
      It represents the unique component.
      In the code we will use the component by calling the 'id'.

2. Tell me about 2 WEB-APIs and how you could integrate them into any of your course content submissions? Give me a line or two of code.
      —— Picture-in-Picture API
      function togglePictureInPicture() {
         if (document.pictureInPictureElement) {
                  document.exitPictureInPicture();
         }
      }
      —— Fullscreen API
      var Promise = Element.requestFullscreen(options);
---

### Week 12

1. tracking
   - Briefly describe how the complexity changes between image, facial, and hand, tracking? 
      image: finding edge points 
      Facial: Facemesh keypoints
      Hand: Hand motion contact points

2. OOP, ECS, DOM
   - What are these acronyms? How are they related?
      OOP：Object-oriented Programming
      ECS: Entity Component System
      DOM: Document Object Model
      OOP and ECS are two different foundations and approachs for game developers.
      In A-Frame, declarative DOM-Based ECS

3. How do you register a component in A-Frame, and show me how to relate this component to data flow, API, and useage. 
      <a-entity ${componentName}="${propertyName1}: ${propertyValue1}; ${propertyName2}: ${propertyValue2}">
      AFRAME.registerCoponent (name, definition) API
      Create component on the scene, and be listened by DOM.

---

## That's all!

(did you ever watch the movie trailer embedded somewhere in your Quiz 3 readme.md [files](https://github.com/robots-make-art-too/Quiz_3-message-in-a-bottle)?)

### Do you want a bonus? 

Do one, some, or all, of the following before the end of April:

Publish an A-Frame component.
- <https://www.npmjs.com/package/angle>

Publish your browser extension. 
- [microsoft](https://docs.microsoft.com/en-us/microsoft-edge/extensions-chromium/publish/create-dev-account)
- [chrome](https://developer.chrome.com/docs/extensions/)
- [firefox](https://addons.mozilla.org/en-CA/developers/)

Release a version of your Bot.
- <https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository>


---

Psst: Every 100 days _another_ `100 days of code` starts ... 