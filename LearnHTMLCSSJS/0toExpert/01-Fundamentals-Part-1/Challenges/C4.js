let bills = [275, 40, 430];

for (bill of bills) {
  console.log(bill);
  let tip = (bill >= 50 && bill <= 300 ? 0.15 : 0.2) * bill;
  console.log(`Bill is ${bill}, tip is ${tip}, have to pay: ${bill + tip}`);
}
