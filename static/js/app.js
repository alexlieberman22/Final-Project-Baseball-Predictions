function add_numbers(){
    let number1 = document.getElementById("number1").value;
    let number2 = document.getElementById("number2").value;
    console.log(number1);
    console.log(number2);

    fetch('/predict_1', {
        method: "POST", 
        body: JSON.stringify({
            number1: number1,
            number2: number2
        })
    }).then(function (response) {
          return response.json();
      }).then(resp=>{
        console.log(resp);

      });
}
