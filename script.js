function arrayRemove( arr, value ) {
  // Removes a value from an array
  return arr.filter(  function( ele ){
    return ele != value;
  }  );
}

// define array for checked bookings (checkbox)
var bookings = [];

// define string for ready python code
var code = "";

//define regular expression to match checkbox ID's from 'bookings'
const re = /([A-Za-z]+)(\d)/;

// Define object that matches the day with the corresponding position in WoltPartner App
var days = {
  "Mon": 4,
  "Tue": 5,
  "Wed": 6,
  "Thu": 7,
  "Fri": 5,
  "Sat": 6,
  "Sun": 7,
};

// Putting a checkbox-table into code
$(document).ready( function(){

  $( ":checkbox" ).click( function() {
    // Add an element to 'bookings' when a checkbox is checked
    // Remove an element from 'bookings' when a checkbox is unchecked
    console.log( this.id );

    if (  bookings.includes( this.id )  ) {
      bookings = arrayRemove( bookings, this.id );

    } else { bookings.push( this.id ); };

    $( "#thuCode" ).innerHTML = bookings;
  });

});

//define regular expression to match checkbox ID's from 'bookings'
const re = /([A-Za-z]+)(\d)/;
