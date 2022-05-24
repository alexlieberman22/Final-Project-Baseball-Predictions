function add_numbers(){
    var select_1 = document.getElementById('number_1');
    var option_1 = select_1.options[select_1.selectedIndex];
    var select_2 = document.getElementById('number_2');
    var option_2 = select_2.options[select_2.selectedIndex];
    let number1 = option_1.value;
    let number2 = option_2.value;

    console.log(number1);
    console.log(number2);

    fetch('/predict_1', {
        method: "POST", 
        body: JSON.stringify({
            number1: number1,
            number2: number2
        }),
        headers : {
            'Content-Type' : 'application/json'
        }
    }).then(function (response) {
          return response.json();
      }).then(resp=>{
        console.log(resp);
        document.getElementById('prediction_1').value = resp.prediction;
      });
}