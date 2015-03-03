$(function() {
	$.fn.latestTweets = function(options) {
			// jQuery Twitter Feed. Coded by Tom Elliott @ www.webdevdoor.com (2013) @ based on https://twitter.com/javascripts/blogger.js
			// Requires JSON output from authenticating script: http://www.webdevdoor.com/php/authenticating-twitter-feed-timeline-oauth/
			// Adapted by Bootstrap Hunter @ http://bootstrap-hunter.com (2013) @ to work as jQuery plugin

				var settings = $.extend({
			    	displaylimit: 3,
			    	showdirecttweets: false,
			    	showretweets: false,
			    	showtweetlinks: true,
					showretweetindicator: false,
					showavatar: false,
					showscreenname: false,
					showtwittername: false
				}, options );

				var element = this;

				var loadingHTML = '';

				loadingHTML += '<div id="loading-container">Loading tweets...</div>';
				
				this.html(loadingHTML);
				 
			    $.getJSON('http://192.168.1.69/themes/Spirito/php/gettweets.php', 
			        function(feeds) {   
					   //alert(feeds);
			            var feedHTML = '';
			            var displayCounter = 1;         
			            for (var i=0; i<feeds.length; i++) {
							var tweetscreenname = feeds[i].user.name;
			                var tweetusername = feeds[i].user.screen_name;
			                var profileimage = feeds[i].user.profile_image_url_https;
			                var status = feeds[i].text; 
							var isaretweet = false;
							var isdirect = false;
							var tweetid = feeds[i].id_str;
							
							//If the tweet has been retweeted, get the profile pic of the tweeter
							if(typeof feeds[i].retweeted_status != 'undefined'){
							   profileimage = feeds[i].retweeted_status.user.profile_image_url_https;
							   tweetscreenname = feeds[i].retweeted_status.user.name;
							   tweetusername = feeds[i].retweeted_status.user.screen_name;
							   tweetid = feeds[i].retweeted_status.id_str;
							   status = feeds[i].retweeted_status.text; 
							   isaretweet = true;
							 };
							 
							 
							 //Check to see if the tweet is a direct message
							 if (feeds[i].text.substr(0,1) == "@") {
								 isdirect = true;
							 }
							 
							//console.log(feeds[i]);
							 
							 //Generate twitter feed HTML based on selected options
							 if (((settings.showretweets == true) || ((isaretweet == false) && (settings.showretweets == false))) && ((settings.showdirecttweets == true) || ((settings.showdirecttweets == false) && (isdirect == false)))) { 
								if ((feeds[i].text.length > 1) && (displayCounter <= settings.displaylimit)) {             
									if (settings.showtweetlinks == true) {
										status = addlinks(status);
									}
												 
									feedHTML += '<div class="twitter-article" id="tw'+displayCounter+'">'; 	
									if (settings.showavatar) {									                 
										feedHTML += '<div class="twitter-pic"><a href="https://twitter.com/'+tweetusername+'" target="_blank"><img src="'+profileimage+'"images/twitter-feed-icon.png" width="42" height="42" alt="twitter icon" /></a></div>';
									}
									feedHTML += '<div class="twitter-text"><p>';
									if (settings.showscreenname) {
										feedHTML += '<span class="tweetprofilelink"><strong><a href="https://twitter.com/'+tweetusername+'" target="_blank">'+tweetscreenname+'</a></strong>';
									}
									if (settings.showtwittername) {
										feedHTML += '<a href="https://twitter.com/'+tweetusername+'" target="_blank">@'+tweetusername+'</a></span><br/>';
									}
									feedHTML += status+'<span class="tweet-time"><a href="https://twitter.com/'+tweetusername+'/status/'+tweetid+'" target="_blank">'+relative_time(feeds[i].created_at)+'</a></span></p>';
									
									if ((isaretweet == true) && (settings.showretweetindicator == true)) {
										feedHTML += '<div id="retweet-indicator"><i class="fa fa-retweet"></i></div>';
									}						
									
									feedHTML += '</div>';
									feedHTML += '</div>';
									displayCounter++;
								}   
							 }
			            }
			             
			            element.html(feedHTML);
						
						
			    }).error(function(jqXHR, textStatus, errorThrown) {
					var error = "";
						 if (jqXHR.status === 0) {
			               error = 'Connection problem. Check file path and www vs non-www in getJSON request';
			            } else if (jqXHR.status == 404) {
			                error = 'Requested page not found. [404]';
			            } else if (jqXHR.status == 500) {
			                error = 'Internal Server Error [500].';
			            } else if (exception === 'parsererror') {
			                error = 'Requested JSON parse failed.';
			            } else if (exception === 'timeout') {
			                error = 'Time out error.';
			            } else if (exception === 'abort') {
			                error = 'Ajax request aborted.';
			            } else {
			                error = 'Uncaught Error.\n' + jqXHR.responseText;
			            }	
			       		alert("error: " + error);
			    });
    	}

	    //Function modified from Stack Overflow
	    function addlinks(data) {
	        //Add link to all http:// links within tweets
	         data = data.replace(/((https?|s?ftp|ssh)\:\/\/[^"\s\<\>]*[^.,;'">\:\s\<\>\)\]\!])/g, function(url) {
	            return '<a href="'+url+'"  target="_blank">'+url+'</a>';
	        });
	             
	        //Add link to @usernames used within tweets
	        data = data.replace(/\B@([_a-z0-9]+)/ig, function(reply) {
	            return '<a href="http://twitter.com/'+reply.substring(1)+'" style="font-weight:lighter;" target="_blank">'+reply.charAt(0)+reply.substring(1)+'</a>';
	        });
			//Add link to #hastags used within tweets
	        data = data.replace(/\B#([_a-z0-9]+)/ig, function(reply) {
	            return '<a href="https://twitter.com/search?q='+reply.substring(1)+'" style="font-weight:lighter;" target="_blank">'+reply.charAt(0)+reply.substring(1)+'</a>';
	        });
	        return data;
	    }
	     
	     
	    function relative_time(time_value) {
	      var values = time_value.split(" ");
	      time_value = values[1] + " " + values[2] + ", " + values[5] + " " + values[3];
	      var parsed_date = Date.parse(time_value);
	      var relative_to = (arguments.length > 1) ? arguments[1] : new Date();
	      var delta = parseInt((relative_to.getTime() - parsed_date) / 1000);
		  var shortdate = time_value.substr(4,2) + " " + time_value.substr(0,3);
	      delta = delta + (relative_to.getTimezoneOffset() * 60);
	     
	      if (delta < 60) {
	        return 'a moment ago';
	      } else if(delta < 120) {
	        return '1 minute ago';
	      } else if(delta < (60*60)) {
	        return (parseInt(delta / 60)).toString() + ' minutes ago';
	      } else if(delta < (120*60)) {
	        return '1 hour ago';
	      } else if(delta < (24*60*60)) {
	        return (parseInt(delta / 3600)).toString() + ' hours ago';
	      } else if(delta < (48*60*60)) {
	        //return '1 day';
			return 'a day ago';
	      } else {
	        return shortdate;
	      }
	    }
});