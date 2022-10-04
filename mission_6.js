function statement(invoice, plays) {
  let totalAmount = 0;
  let result = `Statement for ${invoice.customer}\n`;

  const format = new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
    minimumFractionDigits: 2,
  }).format;

  for (let perf of invoice.performances) {
    // Split loops
    let thisAmount = amountFor(perf, playFor(perf)); // Inline function

    // print line for this order
    result += ` ${playFor(perf).name}: ${format(thisAmount / 100)} (${
      perf.audience
    } seats)\n`;
    totalAmount += thisAmount;
  }

  result += `Amount owed is ${format(totalAmount / 100)}\n`;
  result += `You earned ${totalVolumen(invoice)} credits\n`;

  return result;
}

function totalVolumen(invoice) {
  let volumenCredits = 0;

  for (let perf of invoice.performances) {
    volumenCredits += calculateVolumen(perf);
  }
  return volumenCredits;
}

function calculateVolumen(perf) {
  let volumenCredits = 0;

  // add frequent renter points
  volumenCredits += Math.max(perf.audience - 30, 0);
  // add extra credit for every ten comedy attendees
  if ("comedy" === playFor(perf).type)
    volumenCredits += Math.floor(perf.audience / 5);

  return volumenCredits;
}

function playFor(perf) {
  return plays[perf.playID];
}

function amountFor(perf, play) {
  let thisAmount = 0;

  switch (play.type) {
    case "tragedy":
      thisAmount = 40000;
      if (perf.audience > 30) {
        thisAmount += 1000 * (perf.audience - 30);
      }
      break;
    case "comedy":
      thisAmount = 30000;
      if (perf.audience > 20) {
        thisAmount += 10000 + 500 * (perf.audience - 20);
      }
      thisAmount += 300 * perf.audience;
      break;
    default:
      throw new Error(`unknown type: ${play.type}`);
  }

  return thisAmount;
}

invoice = {
  customer: "BigCo",
  performances: [
    {
      playID: "hamlet",
      audience: 55,
    },
    {
      playID: "aslike",
      audience: 35,
    },
    {
      playID: "othello",
      audience: 40,
    },
  ],
};

plays = {
  hamlet: { name: "Hamlet", type: "tragedy" },
  aslike: { name: "As You Like It", type: "comedy" },
  othello: { name: "Othello", type: "tragedy" },
};

result = statement(invoice, plays);
console.log(result);
