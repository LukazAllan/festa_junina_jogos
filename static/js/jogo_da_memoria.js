function animate_card00() {
    document.getElementById('card00').className = 'card-wrapper pode-rodar';
    document.getElementById('card00').className = 'card-wrapper pode-rodar';
}

let Cards = [0,0,0]

const newspaperSpinning = [
  { transform: "rotate(0)" },
  { transform: "rotate(180deg)" },
];

const newspaperTiming = {
  duration: 2000,
  iterations: 1,
};

const newspaper = document.querySelector("#card00");

newspaper.addEventListener("click", () => {
    Cards[0] = 1;
  newspaper.animate(newspaperSpinning, newspaperTiming);
});