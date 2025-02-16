const selectedType = localStorage.getItem('selectedType');
console.log(selectedType);

function fetchTotalAmount(type) {
    if (!type) {
        const TotalAmount = document.getElementById('TotalAmount');
        if(TotalAmount){
            TotalAmount.textContent = 'Invalid type';
        } else {
            console.log("Element with id 'TotalAmount' not found");
        }
        return;
    }
    const SelectedType = document.getElementById('SelectedType');
    if(SelectedType){
        SelectedType.textContent = type;
    } else {
        console.log("Element with id 'SelectedType' not found");
    }

    fetch(`/api/total_amount?transaction_type=${encodeURIComponent(type)}`)
        .then(response => response.json())
        .then(data => {
            const TotalAmount = document.getElementById('TotalAmount');
            if(TotalAmount){
                TotalAmount.textContent = data.total_amount;
            } else {
                console.log("Element with id 'TotalAmount' not found");
            }
        })
        .catch(error => console.error('Error fetching total amount:', error));
}
fetchTotalAmount(selectedType);

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
                messagesContainer.textContent = 'No messages available';
                return;
            }

            const messageItems = data.tmessages.map(msg => {
                // Check if the table is "Incoming Money" to use the 'sender' field
                const isIncomingMoneyTable = tableName === "Incoming_Money";

                // Get the appropriate field (recipient or sender)
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

            messagesContainer.innerHTML = messageItems.join('');
        })
        .catch(error => {
            messagesContainer.textContent = 'Error fetching messages';
            console.error('Error fetching entries:', error);
        });
}



fetchAllEntries(selectedType);