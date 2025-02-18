const selectedType = localStorage.getItem("selectedType");
console.log(selectedType);

function fetchTotalAmount(type) {
    if (!type) {
        const TotalAmount = document.getElementById("TotalAmount");
        if (TotalAmount) {
            TotalAmount.textContent = "Invalid type";
        } else {
            console.log("Element with id 'TotalAmount' not found");
        }
        return;
    }
    const SelectedType = document.getElementById("SelectedType");
    if (SelectedType) {
        SelectedType.textContent = type;
    } else {
        console.log("Element with id 'SelectedType' not found");
    }

    fetch(`/api/total_amount?transaction_type=${encodeURIComponent(type)}`)
        .then((response) => response.json())
        .then((data) => {
            const TotalAmount = document.getElementById("TotalAmount");
            if (TotalAmount) {
                TotalAmount.textContent = data.total_amount;
            } else {
                console.log("Element with id 'TotalAmount' not found");
            }
        })
        .catch((error) => console.error("Error fetching total amount:", error));
}

let globalData; 

function displayMessages(messages, tableName) {
    const messagesContainer = document.getElementById("TopMessages");

    const messageItems = messages.map((msg) => {
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

    messagesContainer.innerHTML = messageItems.join("");
}

function displayAllMessages(messages, tableName) {
    const messagesContainer = document.getElementById("TopMessages");

    const messageItems = messages.map((msg) => {
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

    messagesContainer.innerHTML += messageItems.join("");
}

function fetchAllEntries(tableName) {
    const messagesContainer = document.getElementById("TopMessages");

    if (!tableName) {
        messagesContainer.textContent = "Invalid table name";
        console.log("Invalid table name provided");
        return;
    }

    return fetch(`/api/mobile_money?table_name=${encodeURIComponent(tableName)}`)
        .then((response) => response.json())
        .then((data) => {
            if (!data || !Array.isArray(data.tmessages) || data.tmessages.length === 0) {
                globalData = data;
                return false;
            }

            globalData = data;

            if (selectedType === "All") {
                displayAllMessages(data.tmessages, tableName);}
                else {
                    displayMessages(data.tmessages, tableName);
                }
            return true;
        })
        .catch((error) => {
            messagesContainer.textContent = "Error fetching messages";
            console.error("Error fetching entries:", error);
            return false;
        });
}

function fetchAllTables() {
    const messagesContainer = document.getElementById("TopMessages");

    fetch("/api/messages")
        .then((response) => {
            if (!response.ok) {
                throw new Error(`Network response was not ok, status ${response.status}`);
            }
            return response.json();
        })
        .then((data) => {
            console.log("Response from /api/messages:", data);
            globalData = data;
            if (!data || !data.tables || !Array.isArray(data.tables) || data.tables.length === 0) {
                messagesContainer.textContent = "No tables available";
                console.log("No tables found");
                return;
            }

            data.tables.forEach((tableName) => {
                fetchAllEntries(tableName).then((hasMessages) => {
                    if (!hasMessages) {
                        console.log(`No messages for table: ${tableName}`);
                    }
                });
            });
        })
        .catch((error) => {
            messagesContainer.textContent = "Error fetching tables";
            console.error("Error fetching tables:", error);
        });
}



document.querySelectorAll("#sortLink").forEach(link => {
    link.addEventListener("click", function (event) {
        event.preventDefault();

        if (!globalData || !globalData.tmessages) {
            console.log("No data available for sorting");
            return;
        }

        let sortType = event.target.textContent;
        let sortedMessages = [...globalData.tmessages];

        if (sortType.includes("Amount")) {
            sortedMessages.sort((a, b) => {
                let amountA = parseInt(a.amount.replace(/\D/g, '')); 
                let amountB = parseInt(b.amount.replace(/\D/g, ''));
                return sortType.includes("Asc") ? amountA - amountB : amountB - amountA;
            });
        } else if (sortType.includes("Date")) {
            sortedMessages.sort((a, b) => {
                let dateA = new Date(a.date_sent);
                let dateB = new Date(b.date_sent);
                return sortType.includes("Asc") ? dateA - dateB : dateB - dateA;
            });
        }

        displayMessages(sortedMessages, selectedType);
    });
});

fetchTotalAmount(selectedType);

if (selectedType === "All") {
    var element = document.querySelector(".dropbtn");
        element.remove();
    var element = document.querySelector(".info-container");
        element.remove();
    fetchAllTables();
    
} else {
    fetchAllEntries(selectedType);
}
