

	
		
Spirito = {

	i: 1,
	// Main initalize function
	// @param home: Default true, defines if this is home page or not
	init: function(home) {
		home = (home !== undefined ? home : true);
		this.homesize();
		this.animated_contents();

		if (home) {
			this.handleNav();
		}
		this.handleScroll();
		this.handleResize();
		this.blog();
		//this.parallax();

		return this;
	},

	// Function to handle rezie events
	handleResize: function() {
		$this = this;
		if($(window).width() < 1200) {
			$('#home').attr('style','');
		}
		
		if ($(window).width() >= 1200) {
			$('*[data-animate]').addClass('animate');
			if($('html').hasClass('no-cssanimations')) {
				$('*[data-animate]').css('opacity','1');
			} 
		}

		if($(window).width() < 768) {
			$('.menu-trigger a').click(function(){
				$this.toggleMenu();
				return false;
			});
		}

		$this.homesize();
		
		$(window).resize(function(){
			if($(window).width() >= 768) {
				$('.menu-trigger a').removeClass('open');
				$('nav > ul').removeAttr('style');
			}
			if($(window).width() < 768) {
				$('.menu-trigger a').click(function(){
					$this.toggleMenu();
					return false;
				});
			}
			$this.homesize();
		});
	},

	// Function to handle scroll events
	handleScroll: function() {
		var $this = Spirito;
		$(window).scroll(function(){
			if($(window).width() >= 1200) {
				$this.homeParallax();
				//$('.parallax').each(function(e) {
					/*$('.parallax:appeared').each(function() {
						$t = $(this);
						if($t.is(':appeared')) {
							$(this).addClass('pvisible');
							console.log('.parallax appeared');
						} else if($t.filter(':disappeared')) {
							$(this).removeClass('pvisible');

						}
					});*/
				//});
				$this.fadeHome();
				$this.animated_contents();
			}
		});

		$('*[data-scroll]').on('click',function(){
			var target = $(this).data('scroll');
			var off = $(window).width() < 401 ? 30 : 50;
			$this.scrollTo(target,off,1200);
			return false;
		});
	},

	// Function to control navigation
	handleNav: function() {
		$('nav').waypoint('sticky', {
			stuckClass: 'sticky'
		});

		$('nav>ul').onePageNav({
		    currentClass: 'active',
		    changeHash: false,
		    scrollSpeed: 700,
		    scrollOffset: 60,
		    easing: 'swing',
		    end: function() {
		        if($(window).width() < 768) {
		        	$('.menu-trigger a').removeClass('open');
					$('nav > ul').slideUp();
		        }
		    }
		});
	},

	// Functions for parallax effect on home main top bg 
	homeParallax: function(){
		if(!$('#home').hasClass('static')) {
 	    	var scrolled = $(window).scrollTop();
	    	$('#home #maximage .mc-image').css({'top':'auto','bottom': -(scrolled * 0.7) + 'px'});
	    }
	},

	// Function to hold sliders options and initializers
	initSliders: function() {
		$('.bxslider').bxSlider({
		  	mode: 'horizontal',
		  	pager: false,
		  	controls: false,
			auto: true
		});

		$('#maximage').maximage({
			cycleOptions: {
				fx: 'fade',
				speed: 1500,
				prev: '.img-prev',
				next: '.img-next'
			}
		});

		return this;
	},

	// Function to show or hide menu when screen width < 768
	toggleMenu: function() {
		if(!$('.menu-trigger').hasClass('open')) {
			$('.menu-trigger').addClass('open');
			$('nav > ul').stop(false,true).slideDown();			
		} else {
			$('.menu-trigger').removeClass('open');
			$('nav > ul').stop(false,true).slideUp();			
		}
	},

	// Function to hold portfolio sort functions and initializers
	initPortfolio: function(element) {
		element = element !== undefined ? element : "#portfolio";
		$(element).mixitup({
			targetSelector: ".portfolio-item",
			effects: ['fade','rotateX'],
			onMixStart: function() {
				$('.portfolio-item').css('height','');
				$('.portfolio-item').removeClass('og-expanded');
				$('.portfolio-item .og-expander').fadeOut('fast').remove();
			}
		});

		return this;
	},

	// Function to init maps
	initMaps: function(element) {
		element = element !== undefined ? element : "#google-map";
		$(element).gMap({
            controls: {
            	panControl: true,
            	zoomControl: true,
            	mapTypeControl: false,
                scaleControl: true,
                streetViewControl: false,
                overviewMapControl: true
            },
            address: "Paris, France",
            zoom: 15,
            markers:[
                {
                    address: "Paris, France",
                    html: "Our office is here!"
                }
            ]
        });

		return this;
	},

	// Function to initialize fade effect on scroll for main home wrapper
	fadeHome: function() {
	    //Get scroll position of window
	    //windowScroll = $(this).scrollTop() - 50;
	    //Fade the .home-wrapper
	    /*$('.home-wrapper').css({
		   'opacity' : 1-(windowScroll/400)
		});*/
		var ws = $(window).scrollTop(), offset = ws/2;
		$('.home-wrapper, .fullscreen-controls').css({transform: 'translateY('+offset+'px)', opacity: 1-(ws/700)});
		
	},

	// Function to correct main home wrapper dimensions
	homesize: function() {
		windowHeight = $(window).height();
		windowWidth = $(window).width();
		elements = $("#home, #maximage, .mc-cycle, #maximage > .mc-image, #home .pattern");
		elements.css({'height':'auto'});
		elements.css({ 'height': windowHeight+"px", "max-height": windowHeight+"px"});
		if($('body').hasClass('boxed')) {
			$('#maximage, .bxslider li').css({'width': "100%"});
		} else {
			$('.bxslider li').css({'width': windowWidth+"px"});
		}
	},

	// Function for parallax effect
	parallax: function() {
		/*
		var scrolled = $(window).scrollTop();
		$('.parallax').each(function() {
			if(!$(this).hasClass('static')) {
				$(this).css({'background-position': '0px ' + -(scrolled * 0.05) + 'px'});
			}
		});*/

		 
        /* Dont user paralax for tablet and mobile devices. */
        $('#quote').parallax("50%", 0.2);
        $('#clients').parallax("50%", 0.2);
        $('#contact-details').parallax("50%", 0.2);
        //$('#page-features').parallax("0%", 0.07);
        //$('#page-twitter').parallax("0%", 0.1);
    
	},

	parallaxMove: function() {

	},

	// Function to scroll with animation to desired element
	scrollTo: function(hash,offset,speed) {
		speed = (speed !== undefined ? speed : 2000);
		offset = (offset !== undefined ? offset : 0);
		var target_offset = $(hash).offset().top - offset;
		$('html, body').animate({
		    scrollTop: target_offset
		}, speed);
	},

	// Function to control animatons events and classes
	animated_contents: function() {
		$(".animate:appeared").each(function(i) {
			var $this = $(this),
			animated = $(this).data('animate'),	
			delay = 0, 
			del = '';
			if($(this).data('delay')) {
				del = $(this).data('delay');
				if($.isNumeric(del)) {
					delay = $(this).data('delay');
				}
			}
			if(del == 'none') {
				setTimeout(function () {
					$this.addClass(animated);
				}, 200);
				i = i+1;
			} else {
				setTimeout(function () {
					$this.addClass(animated);
				}, (150 * i) + delay);
			}
		});
	},

	blog: function() {
		$('.blog-more-posts').click(function(){
			var btn = $(this);
			var output = {}
			$.getJSON('http://192.168.1.69/themes/Spirito/php/posts.php', 
				function(posts) {
					for (var i=0; i<posts.length; i++) {
						post = '<div class="col-xs-12 col-sm-12 col-md-4 col-lg-4"><article data-animate="fade-in-bottom" class="post animate fade-in-bottom"><a class="post-image" href="'+posts[i].link+'"><img alt="" src="'+posts[i].img+'"><div class="overlay"><i class="fa fa-'+posts[i].type+'"></i></div></a><h3 class="post-title"><a href="'+posts[i].link+'">'+posts[i].title+'</a></h3><p class="post-meta"><span class="meta-date">'+posts[i].date+'</span><span class="meta-by"><a href="#">'+posts[i].author+'</a></span></p><p class="post-content">'+posts[i].content+'</p><p class="post-read-more"><a class="btn btn-primary btn-sm" href="'+posts[i].link+'">Read More</a></p></article></div>';
						output[i] = post;
					}
					$.each(output, function(i,value){
						setTimeout(function(){
							$('.posts').append(value);
						}, (200 * i));
					});
					btn.animate({'opacity': '0','height': '0'},function(){
						btn.remove();
					});
				}
			);
			return false;
		});
	}
}