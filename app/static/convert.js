$(document).ready(function() {
	// Takes amount/currency one as the source and gets the corresponding amount
	// for currency two.  Sets the fields accordingly.
	function conversionOne() {
		$.post('/ajax', {
			source_currency: $("#currency_one option:selected").text(), 
			target_currency: $("#currency_two option:selected").text(), 
			source_amount: $("#amount_one").val()
		}).done(function(response) {
			$("#currency_one select").val(response['source_currency']);
			$("#currency_two select").val(response['target_currency']);
			$("#amount_one").val(response['source_amount']);
			$("#amount_two").val(response['target_amount']);
		}).fail(function() {
			console.log("Error: could not connect to the server.");
		});
	}
	
	// Takes amount/currency two as the source and gets the corresponding amount
	// for currency one.  Sets the fields accordingly.
	function conversionTwo() {
		$.post('/ajax', {
			target_currency: $("#currency_one option:selected").text(), 
			source_currency: $("#currency_two option:selected").text(), 
			source_amount: $("#amount_two").val()
		}).done(function(response) {
			$("#currency_one select").val(response['target_currency']);
			$("#currency_two select").val(response['source_currency']);
			$("#amount_one").val(response['target_amount']);
			$("#amount_two").val(response['source_amount']);
		}).fail(function() {
			console.log("Error: could not connect to the server.");
		});
	}

	// 48-57 for the digits, 69 for E/e, 190 ., 189 -, 187 +, 8 backspace
	var allowedKeyCodes = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 69, 190, 189, 187, 8]
	function checkValidKey(code) {
		if (allowedKeyCodes.includes(code)) {
			return true;
		}
		return false;
	}
	
	$("#convert-button").click(function() {
		conversionOne();
	});
	
	var requestTimeout;

	$("#amount_one").keydown(function(e) {
		var code = e.keyCode || e.which;
		if (checkValidKey(code)) {
			clearTimeout(requestTimeout);
			requestTimeout = setTimeout(function() {
				conversionOne();
			}, 1000);
		}
	});
	
	$("#amount_two").keydown(function(e) {
		var code = e.keyCode || e.which;
		if (checkValidKey(code)) {
			clearTimeout(requestTimeout);
			requestTimeout = setTimeout(function() {
				conversionTwo();
			}, 1000);
		}
	});

	$("#currency_one").change(function () {
		console.log("CURRENCY ONE CHANGED.");
		clearTimeout(requestTimeout);
		requestTimeout = setTimeout(function() {
			conversionOne();
		}, 1000);
	});
	
	$("#currency_two").change(function () {
		console.log("CURRENCY TWO CHANGED.");
		clearTimeout(requestTimeout);
		requestTimeout = setTimeout(function() {
			//conversionTwo();
			conversionOne();
		}, 1000);
	});
});
