api_key = "963adb712062f1bd2057a6e4063a9c06";
account_id = "56a3986c957f400e00aa8ed2";
charity_list = [
    "American Diabetes Association",
    "Books for Africa",
    "Direct Relief",
    "Midwest Food Bank",
    "Step Up For Students",
    "MAP International",
    "World Food Bank",
    "Central Illinois Foodbank",
    "Central Pennsylvenia Foodbank",
    "Orphan Grain Train"
];

wishlist = [
    {image: "http://iosetc.com/wp-content/uploads/2015/07/IMG_3034_iphone6_spacegrey_portrait.png", item_name: "iPhone", item_policy: 50, item_progress: 73, chart_color: "F7464A"},
    {image: "http://www.cityhomebuyer.com/uploads/6/5/4/1/65416949/8841854_orig.png", item_name: "House", item_policy: 10, item_progress: 5, chart_color: "07004A"},
    {image: "https://cdn2.bigcommerce.com/server1900/xfluwv/product_images/uploaded_images/samsung-galaxy-gear-2.png", item_name: "Smartwatch", item_policy: 20, item_progress: 56, chart_color: "46BFBD"},
    {image: "http://www.michelbraunstein.com/wp-content/uploads/images/PNG/PNG33-2618.jpg", item_name: "Vacation", item_policy: 20, item_progress: 34, chart_color: "FDB45C"}
];

$(document).ready(function() {
    fill_template("#charities-template", ".charities-container-placeholder", {charities: charity_list});
    $(".fa-heart").click(function() {
        $(".charities-container-placeholder").fadeIn();
    });

    $(".charities li").click(function() {
        if ($(".charities-container-placeholder").is(":visible")) {
            $(".charities-container-placeholder").fadeOut();
        }
        var new_charity = $(this).html();
        $(".charity").html(new_charity);
    });

    instantiate_chart();

    $.when(get_account_info(), get_user_accounts()).done(function(user_info, account_info) {
        fill_template("#greetings-template", ".greetings-container-placeholder",
                        {timeofday: get_greeting_text(), firstname: user_info[0]["first_name"]});
        fill_template("#accounts-template", ".accounts-container-placeholder", account_info[0]);
        fill_template("#wishlist-template", ".wishlist-container-placeholder", wishlist);
        moveProgressBar(); 
        $("tr").hover(function() {
            var color = $(this).data("color");
            console.log(color);
            $(this).css("background", "#"+color);
        }, function() {
            $(this).css("background", "");
        });

    });

});

function moveProgressBar() {
    $('.progress-wrap').each(function() {
        var getPercent = ($(this).data('progress-percent') / 100);
        var getProgressWrapWidth = $('.progress-wrap').width();
        var progressTotal = getPercent * getProgressWrapWidth;
        var animationLength = 2500;
        // on page load, animate percentage bar to data percentage length
        $(this).find('.progress-bar').animate({
            left: progressTotal
        }, animationLength);
    });
    
}

function instantiate_chart() {
    var data = [
    {
        value: 50,
        color:"#F7464A",
        highlight: "#FF5A5E",
        label: "iPhone"
    },

    {
        value: 10,
        color:"#07004A",
        highlight: "#2E294E",
        label: "House"
    },

    {
        value: 20,
        color: "#46BFBD",
        highlight: "#5AD3D1",
        label: "Smartwatch"
    },
    {
        value: 20,
        color: "#FDB45C",
        highlight: "#FFC870",
        label: "Vacation"
    }
];
    var buyers = document.getElementById('buyers').getContext('2d');
    new Chart(buyers).Pie(data);
}

function fill_template(template_id, placeholder_id, context) {
    var source = $(template_id).html();
    var template = Handlebars.compile(source);
    $(placeholder_id).html(template(context));
}

function get_greeting_text() {
    var d = new Date();
    var current_hour = d.getHours();
    var time_of_day;
    if (current_hour > 0 && current_hour < 12)
        time_of_day = "Morning";
    else if (current_hour >= 12 && current_hour < 16)
        time_of_day = "Afternoon";
    else if (current_hour >= 16 && current_hour <= 19)
        time_of_day = "Evening";
    else
        time_of_day = "Night";
    return time_of_day;
}

function get_account_info() {
    return $.ajax({
        url: "http://api.reimaginebanking.com/customers/" + account_id + "?key=" + api_key
    });
}

function get_user_accounts() {
    return $.ajax({
        url: "http://api.reimaginebanking.com/customers/" + account_id + "/accounts?key=" + api_key
    });
}