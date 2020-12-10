// Converting a checkbox-table into ready-to-copy code
$(document).ready( function(){

  /* Add an element to 'bookings' when a checkbox is checked
   Remove an element from 'bookings' when a checkbox is unchecked */
  $( ":checkbox" ).click( function() {

    if (  bookings.includes( this.id )  ) {
      bookings = arrayRemove( bookings, this.id );

    } else { bookings.push( this.id ); };

    //show Python code in a respective space according to the day of booking
    $( "#code" ).html(
      setup +
      toPython( thuDays(bookings), "False" ) +
      toPython( friDays(bookings), "True" ) +
      pause );

  });

});

// Define array for checked bookings (checkbox)
var bookings = [];

const pause = "f.pause()"

const setup = `
#! python3
import fdefs as f

f.setup()
f.enterWolt()
f.autoStart()
f.refresh()
`



// FUNCTIONS //

// Removes a value from an array
function arrayRemove( arr, value ) {

  return arr.filter( function(ele) {
    return ele != value;
  }  );
}

/* Define function translating checkboxIDs array into Python code
  takes in array, returns a string */
function toPython(arr, onFriday) {
  let str = "", add, arg1, arg2;

  for (let i = 0; i < arr.length; i++) {

    arg1 = days[ arr[i].match(re)[1] ];
    arg2 = arr[i].match(re) [2];

    add = `f.booking(${arg1},${arg2},${onFriday})\n`;
    str = str.concat( add );
  };

  return str;
}

// Define object that matches the day with the corresponding position in WoltPartner App
const days = {
  "Mon": 4,
  "Tue": 5,
  "Wed": 6,
  "Thu": 7,
  "Fri": 5,
  "Sat": 6,
  "Sun": 7,
};

// Define regular expression to match checkbox ID's from 'bookings'
const re = /([A-Za-z]+)(\d)/;




/* Define function that filters through 'bookings' and returns array filled
  only with day that need to be booked on Thursday */
function thuDays(arr) {

  return arr.filter( function(ele) {
    let day = ele.match( re ) [1];

    if (day == "Fri" || day == "Sat" || day == "Sun") {
      return ele;
    }

  });
}

/* Define function that filters through 'bookings' and returns array filled
  only with day that need to be booked on Friday */
function friDays(arr) {

  return arr.filter( function(ele) {
    let day = ele.match( re ) [1];

    if (day == "Mon" || day == "Tue" || day == "Wed" || day == "Thu") {
      return ele;
    }

  });
}

// Define copying function
const copyToClipboard = str => {
  const el = document.createElement('textarea');
  el.value = str;
  el.setAttribute('readonly', '');
  el.style.position = 'absolute';
  el.style.left = '-9999px';
  document.body.appendChild(el);
  el.select();
  document.execCommand('copy');
  document.body.removeChild(el);
};

const copyCode = () => {
  copyToClipboard(document.getElementById("code").innerHTML)
}
