
let deadlift = document.getElementById("deadlift");
deadlift.addEventListener("input", function(){
    total("deadlift");
});
let squat = document.getElementById("squat");
squat.addEventListener("input", function(){
    total("squat");
});
let bench = document.getElementById("bench");
bench.addEventListener("input", function (){
    total("bench");
});
function total(liftId){
    let liftValue = document.getElementById(liftId).value.trim(); // Get the value and remove leading/trailing whitespaces
    let lift = isNaN(parseFloat(liftValue)) ? 0 : parseFloat(liftValue); // Parse the value, default to 0 if NaN
    lift *= 0.453592;
    let max = ((lift * 1.1307) + 0.6998);

    max = max / 0.453592;
    document.getElementById(liftId + "Max").textContent = max.toFixed(2) + " lbs";

    let deadliftValue = isNaN(parseFloat(deadlift.value.trim())) ? 0 : parseFloat(deadlift.value.trim());
    let squatValue = isNaN(parseFloat(squat.value.trim())) ? 0 : parseFloat(squat.value.trim());
    let benchValue = isNaN(parseFloat(bench.value.trim())) ? 0 : parseFloat(bench.value.trim());

    let total = document.getElementById("total");
    total.textContent = (deadliftValue + squatValue + benchValue).toString() + " lbs";
}


// (4 to 6 RM x 1.1307) + 0.6998





