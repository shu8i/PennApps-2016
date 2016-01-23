api_key = "963adb712062f1bd2057a6e4063a9c06";
account_id = "56a3986c957f400e00aa8ed2";

$(document).ready(function() {
	$.when(get_account_info(), get_user_accounts()).done(function(user_info, account_info) {
		console.log(account_info[0]);
		fill_template("#greetings-template", ".greetings-container-placeholder",
						{timeofday: get_greeting_text(), firstname: user_info[0]["first_name"]});
		fill_template("#accounts-template", ".accounts-container-placeholder", account_info[0]);
		
	});
});

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