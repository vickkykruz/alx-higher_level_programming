// Attach a click event handler to the DIV#add_item element
$('#add_item').click(function() {
      // Create a new <li> element with the content "Item"
    var newItem = $('<li>Item</li>');
      
      // Append the new <li> element to the UL.my_list
    $('ul.my_list').append(newItem);
});
