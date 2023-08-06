// Function to fetch and display the translation
function translateHello() {
  const languageCode = $('#language_code').val();
  const apiUrl = `https://www.fourtonfish.com/hellosalut/?lang=${languageCode}`;

  $.getJSON(apiUrl, function (data) {
    const translation = data.hello;
    $('#hello').text(translation);
  });
}

// Event listener for the Translate button click
$('#btn_translate').click(translateHello);
