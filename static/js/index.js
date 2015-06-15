var colors = [
  ['0x268bd2', '0x0d394f']
  ,['0xc93b3b', '0x561414']
  ,['0xe25e36', '0x79231b']
  ,['0x6c71c4', '0x393f6a']
  ,['0x58c73c', '0x30641c']
  ,['0xcac34c', '0x736a2c']
];

function initWorld(world, Physics) {

  // bounds of the window
  var viewWidth = window.innerWidth
    ,viewHeight = window.innerHeight
    ,viewportBounds = Physics.aabb(0, 0, window.innerWidth, 400)
    ,edgeBounce
    ,renderer
    ,styles = {
      'circle': {
        fillStyle: colors[0][0],
        lineWidth: 1,
        strokeStyle: colors[0][1],
        angleIndicator: colors[0][1]
      }
      ,'rectangle': {
        fillStyle: colors[1][0],
        lineWidth: 1,
        strokeStyle: colors[1][1],
        angleIndicator: colors[1][1]
      }
      ,'convex-polygon': {
        fillStyle: colors[2][0],
        lineWidth: 1,
        strokeStyle: colors[2][1],
        angleIndicator: colors[2][1]
      }
    }
    ;

  // create a renderer
  renderer = Physics.renderer('canvas', { el: 'physic-layer', 
      width: 500,
      height: 500,
      styles: styles });
  // add the renderer
  world.add(renderer);
  // render on each step
  world.on('step', function () {
    world.render();
  });
  
  // constrain objects to these bounds
  edgeBounce = Physics.behavior('edge-collision-detection', {
    aabb: viewportBounds
    ,restitution: 0.5
    ,cof: 0.8
  });

  // resize events
  window.addEventListener('resize', function () {

    // as of 0.7.0 the renderer will auto resize... so we just take the values from the renderer
    viewportBounds = Physics.aabb(0, 0, renderer.width, renderer.height);
    // update the boundaries
    edgeBounce.setAABB(viewportBounds);

  }, true);

  // add behaviors to the world
  world.add([
    Physics.behavior('constant-acceleration')
    ,Physics.behavior('body-impulse-response')
    ,Physics.behavior('body-collision-detection')
    ,Physics.behavior('sweep-prune')
    ,edgeBounce
  ]);  
}

function startWorld( world, Physics ){
  // subscribe to ticker to advance the simulation
  Physics.util.ticker.on(function( time ) {
    world.step( time );
  });
}

//
// Add some interaction
//
function addInteraction( world, Physics ){
  // add the mouse interaction
  world.add(Physics.behavior('interactive', { el: world.renderer().container }));
  // add some fun extra interaction
  var attractor = Physics.behavior('attractor', {
    order: 0,
    strength: 0.002
  });
  
  world.on({
    'interact:poke': function( pos ){
      world.wakeUpAll();
      attractor.position( pos );
      world.add( attractor );
    }
    ,'interact:move': function( pos ){
      attractor.position( pos );
    }
    ,'interact:release': function(){
      world.wakeUpAll();
      world.remove( attractor );
    }
  });
}

// helper function (bind "this" to Physics)
/* 
function makeBody( obj ){ 
  return this.body( obj.name, obj );
}
*/
//
// Add bodies to the world
//
function addBodies( world, Physics ){
    var v = Physics.geometry.regularPolygonVertices;
    /*
    
      var bodies = [
        { name: 'circle', x: 100, y: 100, vx: 0.1, radius: 60 }
    ,{ name: 'rectangle', x: 400, y: 100, vx: -0.1, width: 130, height: 130 }
    ,{ name: 'convex-polygon', x: 150, y: 300, vertices: v( 5, 90 ) }
      ];
    //world.add( bodies.map(makeBody.bind(Physics)) );
    */
      var python = Physics.body('circle', {
      // fixed: true,
      // hidden: true,
      mass: 10000,
      radius: 14,
      x: 400,
      y: 200
    });
    python.view = new Image();
    python.view.src = '/static/img/python.png';
    var php = Physics.body('circle', {
        // fixed: true,
        // hidden: true,
        mass: 40000,
        radius: 14,
        x: 600,
        y: 104
      });
    php.view = new Image();
    php.view.src = '/static/img/php.png';
    
    var django = Physics.body('rectangle', {
        // fixed: true,
        // hidden: true,
        mass: 90000,
        width: 84,
        height: 30,
        x: 200,
        y: 220
      });
    django.view = new Image();
    django.view.src = '/static/img/django.png';

    var mysql = Physics.body('rectangle', {
        // fixed: true,
        // hidden: true,
        mass: 9000,
        width: 58,
        height: 30,
        x: 200,
        y: 36
      });
    mysql.view = new Image();
    mysql.view.src = '/static/img/mysql.png';
    
    var gae = Physics.body('circle', {
        // fixed: true,
        // hidden: true,
        mass: 10000,
        radius: 18,
        x: 80,
        y: 100
      });
    gae.view = new Image();
    gae.view.src = '/static/img/google-app-engine.png';
    
    var scrum = Physics.body('rectangle', {
        // fixed: true,
        // hidden: true,
        mass: 11000,
        width: 66,
        height: 30,
        x: 150,
        y: 20
      });
    scrum.view = new Image();
    scrum.view.src = '/static/img/scrum.png';
    
    var cloud = Physics.body('circle', {
        // fixed: true,
        // hidden: true,
        mass: 10000,
        radius: 14,
        x: 80,
        y: 100
      });
    cloud.view = new Image();
    cloud.view.src = '/static/img/cloud.png';
    
    var angular = Physics.body('rectangle', {
        // fixed: true,
        // hidden: true,
        mass: 11000,
        width: 80,
        height: 80,
        x: 150,
        y: 20
      });
    angular.view = new Image();
    angular.view.src = '/static/img/tech_angular.png';
    
    var html = Physics.body('rectangle', {
        // fixed: true,
        // hidden: true,
        mass: 11000,
        width: 80,
        height: 80,
        x: 150,
        y: 20
      });
    html.view = new Image();
    html.view.src = '/static/img/tech_html.png';
    
    var css = Physics.body('rectangle', {
        // fixed: true,
        // hidden: true,
        mass: 11000,
        width: 66,
        height: 30,
        x: 150,
        y: 20
      });
    css.view = new Image();
    css.view.src = '/static/img/tech_css.png';
    
    var symfony = Physics.body('circle', {
        // fixed: true,
        // hidden: true,
        mass: 10000,
        radius: 14,
        x: 80,
        y: 100
      });
    symfony.view = new Image();
    symfony.view.src = '/static/img/symfony.png';
      // functional programming FTW
    world.add(symfony);
    world.add(css);
    world.add(html);
    world.add(angular);
    world.add(cloud);
    world.add(scrum);
    world.add(gae);
    
    world.add(mysql);
    world.add(django);
    world.add(python);
    world.add(php);
}

//
// Load the libraries with requirejs and create the simulation
//

  
var worldConfig = {
        // timestep
    timestep: 6,
    // maximum number of iterations per step
    maxIPF: 4,
    // default integrator
    integrator: 'verlet',
    // is sleeping disabled?
    sleepDisabled: false,
    // speed at which bodies wake up
    sleepSpeedLimit: 0.1,
    // variance in position below which bodies fall asleep
    sleepVarianceLimit: 2,
    // time (ms) before sleepy bodies fall asleep
    sleepTimeLimit: 500
};
      
Physics( worldConfig, [
    initWorld,
    addInteraction,
    addBodies,
    startWorld
]);


