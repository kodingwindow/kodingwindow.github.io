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
$(document).ready(function()
{
    $(window).scroll(function()
    {
        if ($(this).scrollTop()>70) 
        {
            $('#back-to-top').fadeIn();
        } 
        else 
        {
            $('#back-to-top').fadeOut();
        }
    });
    $('#back-to-top').click(function() 
    {
        $('html,body').animate({scrollTop: 0}, 0);
    });
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



window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'UA-186316851-1');