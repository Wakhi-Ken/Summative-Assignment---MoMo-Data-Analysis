// const xValues = ["Italy", "France", "Spain", "USA", "Argentina"];
// const yValues = [55, 49, 44, 24, 15];
// const barColors = ["#ffcc08", "#ffcc08","#ffcc08","#ffcc08","#ffcc08"];

// new Chart("myChart", {
//   type: "bar",
//   data: {
//     labels: xValues,
//     datasets: [{
//       backgroundColor: barColors,
//       data: yValues
//     }]
//   },
//   options: {
//     legend: {display: false},
//     title: {
//       display: true,
//       text: "Percentage of Transactions"
//     }
//   }
// });
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

fetchBalances();