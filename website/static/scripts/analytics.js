async function fetchBalances() {
    const response = await fetch("http://127.0.0.1:5000/balances");
    const data = await response.json();
    
    const labels = data.map(item => item.transaction_type);
    const values = data.map(item => item.amount);
  
    const ctx = document.getElementById("balanceChart").getContext("2d");
    new Chart(ctx, {
        type: "bar",
        data: {
            labels: labels,
            datasets: [{
                label: "Total Transactions",
                data: values,
                backgroundColor: ["#ffcc08", "#ffcc08", "#ffcc08", "#ffcc08", "#ffcc08", "#ffcc08", "#ffcc08", "#ffcc08", "#ffcc08", "#ffcc08", "#ffcc08"],
                borderColor: '#01668e',
                    borderWidth: 1
            }]
        }
    });
  }
  fetchBalances()
  
  function fetchAllEntries(tableName) {
      const messagesContainer = document.getElementById('TopMessages');
  
      if (!tableName) {
          messagesContainer.textContent = 'Invalid table name';
          console.log("Invalid table name provided");
          return;
      }
  
      fetch(`/api/mobile_money?table_name=${encodeURIComponent(tableName)}`)
          .then(response => response.json())
          .then(data => {
              if (!data || !Array.isArray(data.tmessages) || data.tmessages.length === 0) {
                console.log('No messages available');
                  return;
              }

              data.tmessages.sort((a, b) => b.amount - a.amount);
  
              const topMessages = data.tmessages.slice(0, 3);
  
              const messageItems = topMessages.map(msg => {
                  const isIncomingMoneyTable = tableName === "Incoming_Money";
                  const transactionPerson = isIncomingMoneyTable ? msg.sender : msg.recipient;
  
                  return `
                      <div class="trans-header">
                          <div>
                              <h2>${tableName}</h2>
                              <p>Amount: ${msg.amount}</p>
                              <p>New Balance: ${msg.new_balance}</p>
                          </div>
                          <div class="trans-info">
                              <h3>Transaction Details:</h3>
                              <p><strong>Date Sent:</strong> ${msg.date_sent}</p>
                              <p><strong>${isIncomingMoneyTable ? "Sender" : "Recipient"}:</strong> ${transactionPerson}</p>
                              <p><strong>Service Center:</strong> ${msg.service_center}</p>
                          </div>
                      </div>
                  `;
              });
  
              messagesContainer.innerHTML += `<div class='table-container'>${messageItems.join('')}</div>`;
          })
          .catch(error => {
              messagesContainer.textContent = 'Error fetching messages';
              console.error('Error fetching entries:', error);
          });
  }
  
  function fetchAllTables() {
      const messagesContainer = document.getElementById('TopMessages');
      messagesContainer.innerHTML = "";
  
      fetch('/api/all_messages')
          .then(response => {
              if (!response.ok) {
                  throw new Error(`Network response was not ok, status ${response.status}`);
              }
              return response.json();
          })
          .then(data => {
              console.log('Response from /api/all_messages:', data);
  
              if (!data) {
                  messagesContainer.textContent = 'No data received from server';
                  console.log("no data provided by server");
                  return;
              }
  
              if (Object.keys(data).length === 0) {
                  messagesContainer.textContent = 'No tables available';
                  console.log("No tables available");
                  return;
              }
              
              const tableNames = Object.keys(data);
  
              tableNames.forEach(tableName => {
                  fetchAllEntries(tableName);
              });
          })
          .catch(error => {
              messagesContainer.textContent = 'Error fetching tables';
              console.error('Error fetching tables:', error);
          });
  }
  
  fetchAllTables()