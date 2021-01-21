this.top.location !== this.location && (this.top.location = this.location);

$(function()
{
    $('[data-bs-toggle="leftsidebar"]').on('click', function() 
    {
        $('.rightsidebar-collapse').removeClass('open')
        $('.leftsidebar-collapse').toggleClass('open')
    })
    $('[data-bs-toggle="rightsidebar"]').on('click', function() 
    {
        $('.leftsidebar-collapse').removeClass('open')
        $('.rightsidebar-collapse').toggleClass('open')
    })
    $('[data-bs-toggle="collapseall"]').on('click', function() 
    {
        $('.leftsidebar-collapse').removeClass('open')
        $('.rightsidebar-collapse').removeClass('open')
    })
});
$(document).keydown(function(event) 
{
    if(event.keyCode==123) 
    {
        return false;
    }
});
function kwdate()
{
    const months = ["January", "February", "March","April", "May", "June", "July", "August", "September", "October", "November", "December"];
    const day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    var dt = new Date()
    var date =  day[dt.getDay()]+", "+months[dt.getMonth()]+" "+dt.getDate()+", "+dt.getFullYear();
    return date;
}
function kwtime()
{
    var dt = new Date()
    var time = dt.getHours() + ":" + dt.getMinutes() + ":" + dt.getSeconds();
    return time;
}
function validate_comments(e)
{
    var validate = /[A-Za-z0-9.,?-_ :;=!&^+/%*|@]/.test(String.fromCharCode(e.charCode));
    if(!validate)
        e.preventDefault();
}

$(document).ready(function()
{
    $('#back-to-top').click(function() 
    {
        $('body,html').animate({scrollTop: 0}, 1500);
    });
});
$(document).ready(function()
{
    $('#scroll').click(function() 
    {
        if($(window).scrollTop()+$(window).height()>=$(document).height()/2) 
        {
            $('body,html').animate({scrollTop: 0}, 1500);
        }
        else
        {
            $('body,html').animate({scrollTop: $(document).height()-$(window).height()+50}, 1500);
        }
    });  
});
window.onscroll = function() 
{
    scrollFunction()
};
function scrollFunction() 
{
    if (document.body.scrollTop > 70 || document.documentElement.scrollTop > 70) 
    {
        document.getElementById("back-to-top").style.display = "block";
    } 
    else 
    {
        document.getElementById("back-to-top").style.display = "none";
    }
}

window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'UA-186316851-1');