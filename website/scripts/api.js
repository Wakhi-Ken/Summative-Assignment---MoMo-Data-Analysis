// Fetch all transactions and populate the table
fetch('/api/transactions')
    .then(response => response.json())
    .then(data => {
        const tableBody = document.querySelector('#transactionTable tbody');
        data.forEach(transaction => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${transaction[0]}</td>
                <td>${transaction[1]}</td>
                <td>${transaction[2]}</td>
            `;
            tableBody.appendChild(row);
        });
    })
    .catch(error => console.error('Error fetching data:', error));

// Fetch the total amount for "incoming_money"
fetch('/api/total_amount?type=Incoming_Money')
    .then(response => response.json())
    .then(data => {
        document.getElementById('totalIncomingAmount').textContent = data.total_amount;
    })
    .catch(error => console.error('Error fetching total amount:', error));
