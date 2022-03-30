//run when web page open
window.onload = () => {
    //run finction render
    render();
  };
  
  //create array "models"
  const models = [
    //create a object that the first element's content in "models"
    {
      url: './assets/myModel/scene.gltf',//model site
      scale: '0.5 0.5 0.5',//scale value
      rotation: '0 225 0'//rotation value
    },
  ];
  
  let modelIndex = 0;
  //model: the one we set the value from "models"
  //entity: the type that will be created in html
  //two vars will be imported to setModel when this function is run
  const setModel = (model, entity) => {
    //create and add position and gltf value of model under <entity>
    if (model.position) {
      entity.setAttribute('position', model.position);
    }
  
    entity.setAttribute('gltf-model', model.url);
  };
  
  function render() {
    //find the <a-scene> from html and set it to "scene"
    const scene = document.querySelector('a-scene');
    //get current position and set value to "latitude" and "longitude"
    navigator.geolocation.getCurrentPosition(function (position) {
      const latitude = position.coords.latitude;
      const longitude = position.coords.longitude;
  
      //create the model that we set before to our current location
      const model = document.createElement('a-entity');
      model.setAttribute('gps-entity-place', `latitude: ${latitude}; longitude: ${longitude};`);
  
      setModel(models[modelIndex], model);//get the first element from the array "models"
  
      model.setAttribute('animation-mixer', '');
        //appends model as the child of scene
      scene.appendChild(model);
    });
  }



  /*
    All models thay we want create are under the array "models" (line 10-14)
    The details such as scale are the content of the each element(line 12 and 13)
  */