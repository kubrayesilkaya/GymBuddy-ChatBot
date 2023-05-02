function calculate() {
    const age = parseInt(document.getElementById("age").value);
    const weight = parseInt(document.getElementById("weight").value);
    const height = parseInt(document.getElementById("height").value);
    const neck = parseInt(document.getElementById("neck").value);
    const waist = parseInt(document.getElementById("waist").value);
    const hip = parseInt(document.getElementById("hip").value);
    const gender = document.querySelector('input[name="gender"]:checked').value;

    let factor;
    if (gender === "male") {
        factor = 1;
    } else {
        factor = 0;
    }

    const fatPercentage =
        495 / (1.29579 - 0.35004 * Math.log10(waist + hip - neck) + 0.221 * Math.log10(height)) - 450 * factor;

    const resultElement = document.getElementById("result");
    resultElement.innerHTML = `Your fat percentage is ${fatPercentage.toFixed(2)}%.`;
}