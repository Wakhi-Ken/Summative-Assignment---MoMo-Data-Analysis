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