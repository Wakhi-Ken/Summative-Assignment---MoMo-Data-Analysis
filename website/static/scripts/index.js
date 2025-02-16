window.onload = function() {
    localStorage.clear();
};

const buttons = document.querySelectorAll('.widget-list-item');
if (buttons.length > 0) {
  buttons.forEach(button => {
    button.addEventListener('click', function(event) {
      console.log('A button clicked');
      //no event.preventDefault() here to let the page navigate
    });
  });
} else {
  console.log('could not find my element');
}

// Function to add event listener if element exists
function addEventListenerToElement(elementId, eventType, callback) {
  const element = document.getElementById(elementId);
  if (element) {
    element.addEventListener(eventType, function(event) {
      //no event.preventDefault() here to let the page navigate
      callback(); // Call the original callback function
    });
  } else {
    console.log(`Element with ID '${elementId}' not found.`);
  }
}

addEventListenerToElement('All', 'click', function() {
  localStorage.setItem('selectedType', 'All');
});

addEventListenerToElement('Incoming_Money', 'click', function() {
    localStorage.setItem('selectedType', 'Incoming_Money');
});

addEventListenerToElement('Payments_to_Code_Holders', 'click', function() {
    localStorage.setItem('selectedType', 'Payments_to_Code_Holders');
});

addEventListenerToElement('Transfers_to_Mobile_Numbers', 'click', function() {
    localStorage.setItem('selectedType', 'Transfers_to_Mobile_Numbers');
});

addEventListenerToElement('Bank_Deposits', 'click', function() {
    localStorage.setItem('selectedType', 'Bank_Deposits');
});

addEventListenerToElement('Airtime_Bill_Payments', 'click', function() {
    localStorage.setItem('selectedType', 'Airtime_Bill_Payments');
});

addEventListenerToElement('Cash_Power_Bill_Payments', 'click', function() {
    localStorage.setItem('selectedType', 'Cash_Power_Bill_Payments');
});

addEventListenerToElement('Transactions_Initiated_by_Third_Parties', 'click', function() {
    localStorage.setItem('selectedType', 'Transactions_Initiated_by_Third_Parties');
});

addEventListenerToElement('Withdrawals_from_Agents', 'click', function() {
    localStorage.setItem('selectedType', 'Withdrawals_from_Agents');
});

addEventListenerToElement('Bank_Transfers', 'click', function() {
    localStorage.setItem('selectedType', 'Bank_Transfers');
});

addEventListenerToElement('Internet_and_Voice_Bundle_Purchases', 'click', function() {
    localStorage.setItem('selectedType', 'Internet_and_Voice_Bundle_Purchases');
});

addEventListenerToElement('Other', 'click', function() {
    localStorage.setItem('selectedType', 'Other');
});